import ast
import json
import operator
import os
from openai import OpenAI
from ddgs import DDGS

SYSTEM_PROMPT = """You are a careful AI research agent.
Use web_search when current facts, references, or external information are needed.
Use calculator for arithmetic. Do not invent sources or claim a search happened if it did not.
After using tools, synthesize a clear answer. Cite web results inline using [1], [2], etc.,
and finish with a short Sources list containing the URLs returned by search.
If evidence is uncertain or conflicting, say so. Prefer concise, useful answers."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for recent or factual information. Returns snippets and URLs.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string", "description": "Search query"}},
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a basic arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"]
            }
        }
    }
]

_ALLOWED_BINOPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv
}
_ALLOWED_UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}

def _eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BINOPS:
        left, right = _eval_node(node.left), _eval_node(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 10:
            raise ValueError("Exponent too large")
        return _ALLOWED_BINOPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARY:
        return _ALLOWED_UNARY[type(node.op)](_eval_node(node.operand))
    raise ValueError("Only basic arithmetic is allowed.")

def calculator(expression):
    tree = ast.parse(expression, mode="eval")
    return str(_eval_node(tree.body))

def web_search(query):
    results = DDGS().text(query, max_results=5)
    if not results:
        return "No search results found."
    formatted = []
    for i, result in enumerate(results, 1):
        formatted.append(
            f"[{i}] {result.get('title', 'Untitled')}\n"
            f"Snippet: {result.get('body', '')}\n"
            f"URL: {result.get('href', '')}"
        )
    return "\n\n".join(formatted)

class ResearchAgent:
    def __init__(self, model=None):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")
        self.client = OpenAI(api_key=api_key)
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def run(self, question, max_tool_rounds=5):
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
        trace = []
        for _ in range(max_tool_rounds):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
                temperature=0.2
            )
            message = response.choices[0].message
            if not message.tool_calls:
                return message.content or "I could not generate an answer.", trace

            messages.append(message)
            for tool_call in message.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments or "{}")
                try:
                    if name == "web_search":
                        result = web_search(args["query"])
                        trace.append(f"🔎 Searched: {args['query']}")
                    elif name == "calculator":
                        result = calculator(args["expression"])
                        trace.append(f"🧮 Calculated: {args['expression']} = {result}")
                    else:
                        result = "Unknown tool."
                except Exception as exc:
                    result = f"Tool error: {exc}"
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })
        messages.append({"role": "user", "content": "Give the best answer you can using the tool results so far."})
        final = self.client.chat.completions.create(
            model=self.model, messages=messages, temperature=0.2
        )
        return final.choices[0].message.content or "No answer generated.", trace

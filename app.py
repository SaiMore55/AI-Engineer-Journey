import streamlit as st
from dotenv import load_dotenv
from agent import ResearchAgent

load_dotenv()
st.set_page_config(page_title="AI Research Agent", page_icon="🤖", layout="wide")
st.title("🤖 AI Research Agent")
st.caption("A tool-using assistant that searches the web, calculates, and synthesizes answers with sources.")

with st.sidebar:
    st.header("Settings")
    model = st.text_input("Model", value="gpt-4o-mini", help="Change this to a model available to your API key.")
    st.markdown("---")
    st.markdown("**Available tools**")
    st.write("🔎 Web search")
    st.write("🧮 Calculator")
    st.info("Add your API key to `.env` before starting the app.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask the agent to research something...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            agent = ResearchAgent(model=model)
            with st.spinner("Thinking and using tools..."):
                answer, trace = agent.run(prompt)
            st.markdown(answer)
            if trace:
                with st.expander("Agent activity"):
                    for item in trace:
                        st.markdown(f"- {item}")
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as exc:
            message = f"**Error:** {exc}"
            st.error(message)
            st.session_state.messages.append({"role": "assistant", "content": message})

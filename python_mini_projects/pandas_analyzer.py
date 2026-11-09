import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha",
             "Rohan", "Neha", "Karan", "Pooja"],
    "Age": [20, 21, 19, 20, 22, 19, 21, 20],
    "Marks": [85, 72, 95, 48, 65, 88, 55, 91],
    "City": ["Nashik", "Pune", "Mumbai", "Nashik",
             "Pune", "Mumbai", "Nashik", "Pune"],
    "Department": ["Computer", "IT", "Computer", "IT",
                   "Computer", "IT", "Computer", "IT"]
}

df = pd.DataFrame(data)

print("First five records: ",df.head())
print("Number of rows and columns: ",df.shape)
print("Average: ",df["Marks"].mean())
print("Maximum: ",df["Marks"].max())
print("Mininum: ",df["Marks"].min())
print("Score above 80: ",df[df["Marks"]>80])
print("Student's from nashik: ",df[df["City"]=="Nashik"])
print("Marks wise sorted: ",df.sort_values(by="Marks",ascending=False))
print("Average marks department-wise: ",df.groupby("Department")["Marks"].mean())
df.groupby("City").size()
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)
df.to_csv("student_analysis.csv", index=False)
print(df)
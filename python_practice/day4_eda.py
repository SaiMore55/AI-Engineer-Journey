import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 108, 110],
    "Name": [
        "Amit", "Rahul", "Priya", "Sneha", "Rohan",
        "Neha", "Karan", "Pooja", "Pooja", "Arjun"
    ],
    "Age": [20, 21, 19, 20, None, 19, 21, 20, 20, 65],
    "Marks": [85, 72, 95, None, 65, 88, 55, 91, 91, 150],
    "Attendance": [90, 85, 95, 80, 75, None, 70, 92, 92, 40],
    "Department": [
        "Computer", None, "Computer", "IT", "Computer",
        "IT", "Computer", "IT", "IT", "Computer"
    ]
}

df = pd.DataFrame(data)

# print(df)
print()

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# print(df["Department"].value_counts())

# missing_percentage = (df.isnull().sum() / len(df)) * 100

# print(missing_percentage)

df_clean = df.dropna()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Marks"].median())
df["Department"] = df["Department"].fillna("Unknown")
# print(df)

# print(df[df.duplicated()]) # To display duplicate values

df = df.drop_duplicates()
# print(df[df.duplicated(subset=["Student_ID"], keep=False)]) TO get duplicate by a specific column

#Remove records with duplicate student IDs:
# df = df.drop_duplicates(
#     subset=["Student_ID"],
#     keep="first"
# )

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * (IQR)
upper_bound = Q3 + 1.5 * (IQR)

outliers = df[
    (df["Marks"]<lower_bound) &
    (df["Marks"]>upper_bound) 
]

# print(outliers)

#Histogram
# plt.figure(figsize=(8, 5))

# plt.hist(df["Marks"].dropna(), bins=5)

# plt.title("Distribution of Student Marks")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")

# plt.show()

#Boxplot
# plt.figure(figsize=(7, 4))

# sns.boxplot(x=df["Marks"])

# plt.title("Marks Outlier Detection")

# plt.show()

#Bar Chart
# department_avg = df.groupby("Department")["Marks"].mean()

# department_avg.plot(
#     kind="bar",
#     figsize=(7, 4),
#     title="Average Marks by Department"
# )

# plt.ylabel("Average Marks")
# plt.show()


#Scatter plot
# sns.scatterplot(
#     data=df,
#     x="Attendance",
#     y="Marks"
# )

# plt.title("Attendance vs Marks")
# plt.show()

correlation = df[["Age", "Marks", "Attendance"]].corr()

# print(correlation)

plt.figure(figsize=(7, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()
# print(df)
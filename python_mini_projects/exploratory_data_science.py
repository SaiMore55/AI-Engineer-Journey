from statistics import correlation

import pandas as pd
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
        "Computer", "Mechanical", "Computer", "IT", "Computer",
        "IT", "Computer", "IT", "IT", "Computer"
    ]
}

df = pd.DataFrame(data)

print("Complete Dataset:\n",df)

# Part A – Data investigation

# 1. Display the first five rows.
print(df.head())

# 2. Display dataset shape and information.
print("Shape: ",df.shape)
print("DataFrame Information\n",df.info())

# 3. Calculate descriptive statistics.
print("Descriptive Statistics: \n",df.describe())

# 4. Find missing values and their percentages.
missing_values = df.isnull().sum()
percentage_of_missing_values = (missing_values / len(df)) * 100
print(percentage_of_missing_values)

# 5. Identify duplicate Student IDs.
duplicate_values = df[df.duplicated(subset="Student_ID")]
print(duplicate_values)

# Part B – Data cleaning

# 6. Remove duplicate Student IDs, keeping the first record after investigating.
df = df.drop_duplicates(keep="first")
print(df)

# 7. Fill missing Age values using the median.
df["Age"] = df["Age"].fillna(df["Age"].median())

# 8. Fill missing Marks values using the median.
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# 9. Fill missing Attendance values using the median.
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())

# 10. Identify invalid marks, ages and attendance values. Don't silently remove them; report and handle them using documented validation rules.
invalid_age = df[(df["Age"]<15) | (df["Age"] > 50)]
invalid_marks = df[(df["Marks"] < 0) | (df["Marks"] > 100)]
invalid_attendance = df[(df["Attendance"] < 0) | (df["Attendance"] > 100)]

print(invalid_age)
print(invalid_marks)
print(invalid_attendance)


# Part C – Exploratory analysis

# 11. Calculate average marks by department.
avg_by_dept = df.groupby("Department")["Marks"].mean()
print(avg_by_dept)

# 12. Calculate average attendance by department.
avg_att = df.groupby("Department")["Attendance"].mean()
print(avg_att)

# 13. Create a histogram of marks.
plt.figure(figsize=(8,5))
plt.hist(df["Marks"].dropna(),bins=5)
plt.title("Student's Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# 14. Create a boxplot of marks.
plt.figure(figsize=(7,4))

sns.boxplot(x=df["Marks"])

plt.title("Marks Box Plot")

plt.show()


# 15. Create an attendance-versus-marks scatter plot.
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks",
)

plt.title("Attendance vs Marks")
plt.show()

# 16. Generate a correlation heatmap.

correlation = df[["Age","Marks","Attendance"]].corr()

plt.figure(figsize=(7,5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation heatmap")

plt.show()

df.to_csv("cleaned_student_dataset.csv",index=False)
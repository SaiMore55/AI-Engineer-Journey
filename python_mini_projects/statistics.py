import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha",
             "Rohan", "Neha", "Karan", "Pooja",
             "Arjun", "Meera"],
    "Marks": [85, 72, 95, 48, 65, 88, 55, 91, 78, 82],
    "Study_Hours": [5, 3, 7, 2, 4, 6, 2, 7, 5, 6]
}

df = pd.DataFrame(data)

# Part A – Descriptive statistics

# 1. Calculate mean, median and mode of marks.
marks = df["Marks"]
print("Mean: ",marks.mean())
print("Median: ",marks.median())
print("Mode: ",marks.mode())

# 2. Calculate minimum, maximum and range.
print("Maximum: ",marks.max())
print("Minimum: ",marks.min())
print("Range: ",marks.max()-marks.min())

# 3. Calculate population variance and standard deviation using NumPy.
print("Population variance: ",np.var(marks, ddof=0))  # Population variance
print("Population std",np.std(marks, ddof=0)) # Population standard deviation


# 4. Calculate sample variance and standard deviation using NumPy.
print("Sample variance: ",np.var(marks, ddof=1))  # Sample variance
print("Sample std: ",np.std(marks, ddof=1))  # Sample standard deviation


# Part B – Statistical analysis
# 5. Calculate the Z-score for every student's marks.

df["Z_Score"] = (
    marks - marks.mean()
) / marks.std()

print(df)

# 6. Identify students whose Z-score is greater than 1.
print(df[df["Z_Score"]>=1])

# 7. Calculate the correlation between study hours and marks.
correlation = df["Study_Hours"].corr(df["Marks"])
print(correlation)

# 8. Determine whether the relationship is positive or negative.
if correlation > 0:
    print("Positive relationship")
elif correlation < 0:
    print("Negative relationship")
else:
    print("No linear correlation")
# Part C – Probability
# 9. Calculate the probability of randomly selecting a student who scored at least 80.
atleast_eighty = df[df["Marks"]>=80]
print("Probability: ",len(atleast_eighty)/len(df))

# 10. Simulate 10,000 random selections of a student and estimate that probability. Use NumPy's random functions.
rand = np.random.choice(marks, size=10000)
probability = np.mean(rand >= 80)
print("Estimated Probability:", probability)

# Part D – Visualization
# 11. Plot a histogram of marks.
df["Marks"].plot(kind="hist", bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()
# 12. Plot a boxplot of marks.
# Basic Box Plot
df["Marks"].plot(kind="box")
plt.ylabel("Marks")
plt.title("Box Plot of Marks")
plt.show()
# 13. Plot a scatter plot of study hours versus marks.
# Basic Scatter Plot
df.plot(kind="scatter", x="Study_Hours", y="Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
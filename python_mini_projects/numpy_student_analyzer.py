import numpy as np

students = ["Amit", "Rahul", "Priya", "Sneha", "Rohan"]
students = np.array(students)
marks = np.array([85, 72, 95, 48, 65])

print("="*10," STUDENT MARKS ANALYZER ","="*50,end="\n\n")

print("Original Marks: ",marks)

print("Average: ",np.mean(marks))
print("Median:  ",np.median(marks))
print("Highest Marks: ",np.max(marks))
print("Lowest Marks:  ",np.min(marks))

print()

print("Student scoring 75 or above:")

print(students[marks>=75] )

updated_marks = marks + 5
print("Updated Marks: ",updated_marks)
print("Updated Average: ",np.mean(updated_marks))
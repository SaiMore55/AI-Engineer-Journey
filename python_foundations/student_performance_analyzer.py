students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Priya", "marks": 95},
    {"name": "Sneha", "marks": 48},
    {"name": "Rohan", "marks": 65}
]

print()
print("="*10, "STUDENT PERFORMANCE REPORT","="*10,end="\n\n")

total_students = len(students)
print("Total Students : ",total_students)

total_marks = sum(student["marks"] for student in students)
average_marks = (total_marks/500)*100

print("Average Marks : ",average_marks,end="\n\n")

highest_scorer = max(students, key=lambda student: student["marks"])

print("Highest Scorer:", highest_scorer["name"],"-",highest_scorer["marks"])

lowest_marks = min(students, key=lambda student: student["marks"])
print("Lowest Scorer :",lowest_marks["name"],"-",lowest_marks["marks"],end="\n\n")

print("Student Results:")

for student in students:
    
    if student["marks"]>=85:
        student_grade = "Excellent"
        print(student["name"]," - ",student["marks"]," - ",student_grade)
        
    elif student["marks"] < 85 and student["marks"] >= 70:
        student_grade = "Good"
        print(student["name"]," - ",student["marks"]," - ",student_grade)
    
    elif student["marks"] < 70 and student["marks"] >= 50:
        student_grade = "Average"
        print(student["name"]," - ",student["marks"]," - ",student_grade)
    
    else :
        student_grade = "Needs Improvement"
        print(student["name"]," - ",student["marks"]," - ",student_grade)
      

# 1. Take student details as input
name = input("Enter student name: ")
student_class = input("Enter class: ")

# 2. Take five subject marks (converted to float for decimal accuracy)
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# 3. Calculate total and percentage (assuming each subject is out of 100)
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100

# 4. Display the formatted result
print("\n--- Student Result ---")
print("Name:", name)
print("Class:", student_class)
print(f"Percentage: {percentage:.2f}%")

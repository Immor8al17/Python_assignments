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


#Strings
# 1. Input two strings and concatenate them
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
text = str1 + " " + str2  # Added a space between them for readability
print("Concatenated String:", text)
print("-" * 30)

# 2. Case Conversion Methods
print("1. lower():", text.lower())                 # Converts to lowercase
print("2. upper():", text.upper())                 # Converts to uppercase
print("3. title():", text.title())                 # Capitalizes first letter of each word
print("4. swapcase():", text.swapcase())           # Inverts lower and upper cases
print("5. capitalize():", text.capitalize())       # Capitalizes only the very first letter
print("6. casefold():", text.casefold())           # Aggressive lowercase for matching

# 3. Alignment and Analysis Methods
print("7. center(40, '*'):", text.center(40, "*")) # Centers text inside a width of 40
print("8. count('a'):", text.count('a'))           # Counts occurrences of the character 'a'
print("9. endswith('!'):", text.endswith('!'))     # Checks if string ends with '!'
print("10. find('python'):", text.find('python'))   # Returns starting index of 'python' (-1 if not found)

# 4. String Validation Methods (Returns True/False)
print("11. isalnum():", text.isalnum())             # True if all characters are alphanumeric (no spaces)
print("12. isdigit():", text.isdigit())             # True if all characters are digits
print("13. isnumeric():", text.isnumeric())         # True if all characters are numeric characters
print("14. isspace():", text.isspace())             # True if string contains only whitespace

# 5. Modification Methods
print("15. replace(' ', '-'):", text.replace(' ', '-')) # Replaces all spaces with dashes


# Initial tuple
original_tuple = (1, 2, 3)

# Repeat 3 times
repeated_tuple = original_tuple * 3

print("Original:", original_tuple)
print("Repeated:", repeated_tuple)


# 2 . Join 3 seperate tuples
t1 = (10, 20)
t2 = (30, 40)
t3 = (50, 60)

# Join tuples
combined_tuple = t1 + t2 + t3

print("Combined Tuple:", combined_tuple)



#3. Check existence
fruits = ("apple", "banana", "cherry")
search_item = "banana"

# Check existence
if search_item in fruits:
    print(f"Yes, '{search_item}' exists in the tuple.")
else:
    print(f"No, '{search_item}' does not exist in the tuple.")






#4.  Math Operations Without Built-in Functions

numbers = (15, 42, 7, 23, 91, 18)

# Initialize variables using the first element
total = 0
highest = numbers[0]
lowest = numbers[0]

# Loop to calculate metrics
for num in numbers:
    total += num
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print("Tuple:", numbers)
print("Total Sum:", total)
print("Highest Value:", highest)
print("Lowest Value:", lowest)



#5.. Filter a Tuple (Values > 10)
n = (3, 14, 7, 22, 9, 41, 18, 5)

# Filter items
filtered_tuple = tuple(item for item in n if item > 10)

print("Original:", n)
print("Filtered (Greater than 10):", filtered_tuple)


#6. Count Set Elements Without len()
s = {"cat", "dog", "bird", "fish"}
count = 0

# Count elements manually
for item in s:
    count += 1

print("Set:", s)
print("Number of elements:", count)




#7.  Combine Two Sets (All Unique Elements)
set_a = {"apple", "banana"}
set_b = {"cherry", "banana", "date"}

# Combine sets
unique_combined = set_a.union(set_b)
# Alternative: unique_combined = set_a | set_b

print("Combined Unique Set:", unique_combined)



#8. Find Common Elements (Intersection)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Find common elements
common_elements = s1.intersection(s2)
# Alternative: common_elements = s1 & s2

print("Common Elements:", common_elements)


#9. Elements in Either Set, But Not Both (Symmetric Difference)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Find non-overlapping elements
exclusive_elements = s1.symmetric_difference(s2)
# Alternative: exclusive_elements = s1 ^ s2

print("Elements in either but not both:", exclusive_elements)




#10. Add Multiple Elements from a List into a Set
existing_set = {10, 20, 30}
new_elements_list = [30, 40, 50, 60] # 30 is a duplicate and will be ignored

# Add elements from list
existing_set.update(new_elements_list)

print("Updated Set:", existing_set)





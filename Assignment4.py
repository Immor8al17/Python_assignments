#1. Maximum of Three Numbers
def find_max(a, b, c):
    return max(a, b, c)

# Example usage:
print(find_max(10, 45, 23))  # Output: 45



#2. Distinct Elements from a List
def get_unique(lst):
    return list(set(lst))

# Example usage:
print(get_unique([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

#3. Multiply All Numbers in a List
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage:
print(multiply_list([2, 3, 4]))  # Output: 24


#4. Factorial of a Non-Negative Integer
def factorial(n):
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
print(factorial(5))  # Output: 120


#5.Reverse a String


def reverse_string(s):
    return s[::-1]

# Example usage:
print(reverse_string("Python"))  # Output: nohtyP


#6. Check if Number Falls Within Range (10 to 50)


def is_in_range(num):
    return 10 <= num <= 50

# Example usage:
print(is_in_range(25))  # Output: True
print(is_in_range(5))   # Output: False



# 7. Print Even Numbers from a Given List
def print_even_numbers(lst):
    for i in range(len(lst)):
      if lst[i] % 2 == 0:
        print(lst[i] , end = " ")

# Example usage:
print_even_numbers([1, 2, 3, 4, 5, 6])  # Output: Even numbers: [2, 4, 6]


#8. Check if a Number is Prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False


#9. Count Upper and Lower Case Letters

def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    print(f"Uppercase: {upper_count}, Lowercase: {lower_count}")

# Example usage:
count_case("Hello World!")  # Output: Uppercase: 2, Lowercase: 8

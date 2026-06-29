def find_maximum(a, b, c):
    return max(a, b, c)


def get_distinct_elements(input_list):
    return list(set(input_list))


def multiply_list_numbers(input_list):
    result = 1
    for number in input_list:
        result *= number
    return result


def calculate_factorial(n):
    if n < 0:
        raise ValueError("Number must be a non-negative integer.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def reverse_string(text):
    return text[::-1]


def is_in_range(number):
    return 10 <= number <= 50


def get_even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def count_case_letters(text):
    counts = {"upper": 0, "lower": 0}
    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
    return counts


if __name__ == "__main__":
    print("Max of 4, 9, 2:", find_maximum(4, 9, 2))
    print("Distinct list:", get_distinct_elements([1, 2, 2, 3, 4, 4, 5]))
    print("Multiplied list:", multiply_list_numbers([2, 3, 4]))
    print("Factorial of 5:", calculate_factorial(5))
    print("Reversed string:", reverse_string("Python"))
    print("Is 35 in range 10-50?:", is_in_range(35))
    print("Evens from list:", get_even_numbers([1, 2, 3, 4, 5, 6]))
    print("Is 17 prime?:", is_prime(17))
    print("Case counts:", count_case_letters("Hello World!"))

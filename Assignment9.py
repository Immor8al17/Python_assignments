def get_kaprekar_steps(number):
    if not (1000 <= number <= 9999):
        return ["Error: Number must be a 4-digit number."]

    if len(set(f"{number:04d}")) == 1:
        return ["Error: Number cannot have all identical digits."]

    steps = []
    current = number

    while current != 6174:
        digits = list(f"{current:04d}")

        desc_str = "".join(sorted(digits, reverse=True))
        asc_str = "".join(sorted(digits))

        desc_num = int(desc_str)
        asc_num = int(asc_str)

        next_num = desc_num - asc_num
        steps.append(f"{desc_num} - {asc_str} = {next_num}")

        current = next_num

        if current == 0:
            break

    return steps


if __name__ == "__main__":
    test_number = 3524
    results = get_kaprekar_steps(test_number)
    for index, step in enumerate(results, 1):
        print(f"Step {index}: {step}")

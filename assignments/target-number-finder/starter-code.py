"""Starter code for Algorithmic Calculator - Target Number Finder."""


def find_target_pair(numbers: list[int], target: int):
    """Return (index1, index2, value1, value2) for the first pair that sums to target.

    Return None if no valid pair exists.
    """
    # TODO: Loop through pairs of numbers and return a matching pair.
    # Hint: Use nested loops and make sure the same index is not reused.
    return None


def print_result(numbers: list[int], target: int):
    """Print a student-friendly message for the search result."""
    result = find_target_pair(numbers, target)

    if result is None:
        print(f"No pair found for target {target} in {numbers}")
        return

    i, j, a, b = result
    print(f"Found pair at indexes {i} and {j}: {a} + {b} = {target}")


if __name__ == "__main__":
    # TODO: Add more test cases, including one where no pair exists.
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([5, 5, 3, 8], 10),
        ([1, 2, 4], 20),
    ]

    for numbers, target in test_cases:
        print_result(numbers, target)

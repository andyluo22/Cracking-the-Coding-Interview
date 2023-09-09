# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def isUniqueNoDS(s: str) -> bool:
    left: int = 0
    right: int = 1

    while left < len(s):
        while right < len(s):
            if s[left] == s[right]:
                return False

            right += 1

        left += 1
        right = left + 1

    return True


# Space Complexity: O(1) Constant space usage
# Time Complexity: O(n^2) Nested loops
# Example usage:
result = isUniqueNoDS("abcdefg")
print(result)  # Sh


def isUniqueNoDSOptimized(s: str) -> bool:
    sorted_string = sorted(s)

    last_char = None

    for char in sorted_string:
        if last_char == char:
            return False

        last_char = char

    return True


result = isUniqueNoDSOptimized("abdcdefg")
print(result)

# Time Complexity: O(nlogn)
# Space Complexity: O(1)


def isUniqueDS(s: str) -> bool:
    char_set = set()

    for char in s:
        if char in char_set:
            return False
        char_set.add(char)

    return True


result = isUniqueDS("abcdeffg")
print(result)

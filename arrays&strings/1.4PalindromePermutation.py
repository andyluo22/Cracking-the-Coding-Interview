# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

# CASE: ODD LENGTH, EVEN LENGTH

# Cannot use built in functions like lower or upper to change it to common case for iteration
# Built in functions do not create iterable objects
# Rather look below - use ord() to change to ascii numbers and change to a-z integers 0-25 in table

def char_number(c: chr) -> int:
    a = ord("a")
    z = ord("z")
    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a

    if upper_a <= val <= upper_z:
        return val - upper_a

    return -1


def is_palindrome_permutation(s: str) -> bool:
    char_table = [0 for i in range(ord("z") - ord("a") + 1)]
    # or:      = [0] * (ord('z') - ord('a') + 1)
    odd_counter: int = 0

    for c in s:
        char = char_number(c)

        if char != -1:
            char_table[char] += 1
            if char_table[char] % 2:
                odd_counter += 1
            else:
                odd_counter -= 1

    return odd_counter


print(is_palindrome_permutation("Tact coa"))
print(is_palindrome_permutation("Tacs coa"))
print(is_palindrome_permutation("abcd"))

import string


def clean_phrase(phrase: str) -> list:
    # return [c for c in phrase.lower() if c in string.ascii_lowercase]
    return [
        c for c in phrase.lower() if c in string.ascii_lowercase
    ]  # string.ascii_lowercase cuts everything else like whitespace
    # Output: 'ABc D' -> ['a','b','c','d']


def is_palindrome_bit_vector(phrase):
    """checks if a string is a permutation of a palindrome"""
    r = 0  # Bit vector - keeps track of characters in input string
    for c in clean_phrase(phrase):
        val = ord(c)
        mask = 1 << val

        print(mask)
        if r & mask:
            r &= ~mask
        else:
            r |= mask
    return (r - 1) & r == 0


def is_palindrome_bit_vector2(phrase):
    """checks if a string is a permutation of a palindrome using XOR operation"""
    count_odd = 0
    for c in phrase:
        val = char_number(c)
        if val == -1:
            continue
        count_odd ^= 1 << val

    return count_odd & count_odd - 1 == 0


def iterate_clean_phrase(clean_phrase):
    for c in clean_phrase:
        print(c)


print(clean_phrase("As cd"))
iterate_clean_phrase(["a", "s", "c", "d"])

# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"


def Urlify(s: str, trueLength: int) -> str:

    change_to_list = list(s)
    non_true_length = len(change_to_list) - 1

    for i in reversed(range(trueLength)):
        char = s[i]

        if char == " ":
            change_to_list[non_true_length] = "0"
            change_to_list[non_true_length - 1] = "2"
            change_to_list[non_true_length - 2] = "%"

            non_true_length -= 3

        else:
            change_to_list[non_true_length] = char

            non_true_length -= 1

    return str(change_to_list)


response = Urlify("Mr John Smith    ", 13)
print(response)


def urlify_pythonic(text, length):
    # """solution using standard library"""
    return text[:length].replace(" ", "%20")

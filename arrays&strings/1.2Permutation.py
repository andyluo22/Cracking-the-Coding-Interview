# : Given two strings, write a method to decide if one is a permutation of the other


def isPermutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    for i in range(len(s1)):
        if sorted_s1[i] != sorted_s2[i]:
            return False

    return True


def isPermutationNoSort(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    char_table = [0] * 256

    for c in s1:
        char_table[ord(c)] += 1
    for c in s2:
        if char_table[ord(c)] == 0:
            return False
        char_table[ord(c)] -= 1

    return True

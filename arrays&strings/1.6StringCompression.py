# Implement a method to perform basic string compression using the counts 
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
# "compressed" string would not become smaller than the original string, your method should return 
# the original string. You can assume the string has only uppercase and lowercase letters (a - z)

print(sorted('aAaaaaBAaCZzzDSE'))

def stringCompression(s:str) -> str:
    new_string: list = []
    counter: int = 0
    
    for i in range(len(s)):
        if i != 0 and s[i] != s[i-1]:
            new_string.append(s[i-1] + str(counter))
            counter = 0
        
        counter += 1
    
    if counter:
        new_string.append(s[-1] + str(counter))
        
    return min(s, "".join(new_string), key=len)
    

import time
import unittest


def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
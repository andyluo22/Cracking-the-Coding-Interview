import unittest

def isUniqueString(s:str) -> bool:
    sorted_string = sorted(s)
    prev_string = None
    
    for char in sorted_string:
        if prev_string == char:
            return False
        
        prev_string = char
    
    return True

def isUniqueExtraDS(s: str) -> bool:
    char_set = set()
    
    for char in s:
        if char in char_set:
            return False
        
        char_set.add(char)
    
    
    return True

# Define a test class that inherits from unittest.TestCase
class TestIsUniqueFunctions(unittest.TestCase):

    def test_isUniqueString(self):
        self.assertTrue(isUniqueString("abcdefg"))
        self.assertFalse(isUniqueString("aabbcc"))

    def test_isUniqueExtraDS(self):
        self.assertTrue(isUniqueExtraDS("abcdefg"))
        self.assertFalse(isUniqueExtraDS("aabbcc"))

if __name__ == '__main__':
    unittest.main()
    

def isPermutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    s1, s2 = sorted(s1), sorted(s2)
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    
    return True

def isPermutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    char_table = [0] * 256
    
    for char in s1:
        char_table[ord(char)] += 1
    
    for char in s2:
        if char_table[ord(char)] == 0:
            return False
        char_table[ord(char)] -= 1
        
    return True

def URLify(s: str, trueLength: int):
    list_string = list(s)
    length_of_entire_string = len(list_string) - 1
    
    for i in reversed(range(trueLength)):
        if s[i] == ' ':
            list_string[length_of_entire_string] = '0'
            list_string[length_of_entire_string - 1] = '2'
            list_string[length_of_entire_string - 2] = '%'
            
            length_of_entire_string -= 3
        else:
            list_string[length_of_entire_string] = s[i]
            
            length_of_entire_string -= 1

    return str(list_string)

def pythonURLify(s: str, trueLength: int):
    return s[:trueLength].replace(' ', '%20')
# Implement a function to check if a linked list is a palindrome.

from LinkedList import LinkedList

LOWER_CASE_CONVERSION = 32

# Only works for chars and ints: What about strings and other types with equality comparisons
#  Does not work, only works for permutations of palindroms
# Since this is stricter, we need to have a method to compare both ends at the same time and work inwards 
def isPalindrome(l1: LinkedList) -> bool:
    
    char_table = [0] * 256
    
    current = l1.head
    odd_counter: int = 0
    
    while current:
        current.value = str(current.value)
        char_val = ord(current.value)
        char_table[char_val] += 1

        if char_table[char_val] % 2:
            odd_counter += 1
        
        else:
            odd_counter -= 1
        
        current = current.next
    
    return odd_counter <= 1

def lower_case_convert(c: chr) -> int:
    char_val = str(ord(c))
    
    if ord('A') <= char_val <= ord('Z'):
        char_val += LOWER_CASE_CONVERSION
    
    return char_val
        

l1 = LinkedList()
l1.add_multiple([1,1,2,3,3])

print(isPalindrome(l1))

l2 = LinkedList()
l2.add_multiple([1,1,2,1,2])
print(isPalindrome(l2))

l3 = LinkedList()
l3.add_multiple(['a','a','b','a','a'])
print(isPalindrome(l3))

print(ord('A'))
print(ord('a'))
print(ord('Z'))
print(ord('z'))

#
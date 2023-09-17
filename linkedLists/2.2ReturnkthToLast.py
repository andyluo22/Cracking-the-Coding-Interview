# Implement an algorithm to find the kth to last element of a singly linked list

from LinkedList import  LinkedList

# My own implementation
def returnKtoLast(l1, k: int):
    size: int = 0
    counter: int = 0
    
    current = l1.head
    
    # Just get the length first
    while current:
        size += 1
        current = current.next
        
    current = l1.head
    k_counter = size - k + 1
        
    while current:
        counter += 1
        
        if counter == k_counter:
            return current
        
        current = current.next

# The best one:  Strategy is the have two pointers: leader and follower
# When we reach count >= k, this means follower and leader are k nodes apart
# This means that when we iterate to the end and reach null, the follower is k nodes
# from last of leader which is at the end because we iterate both at the same time 
def kth_to_last(l1, k):
    leader = follower = l1.head
    count = 0
    
    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = leader.next
    
    return follower           

# Use recursion to iterate to the end of the list and do k counts from there
def kth_to_last_recursive(l1, k: int):
    head = l1.head
    counter: int = 0    
    
    def helper(head, k):
        nonlocal counter
        if not head:
            return None
        helper_node = helper(head.next, k)
        counter = counter + 1
        if counter == k:
            return head
        return helper_node

    return helper(head, k)
        
import unittest

class TestKthToLastRecursive(unittest.TestCase):
    def test_kth_to_last_recursive_basic(self):
        # Test case 1: Basic test with a single-node linked list
        l1 = LinkedList([5])
        self.assertEqual(kth_to_last_recursive(l1, 1).value, 5)

        # Test case 2: Basic test with a multi-node linked list
        l2 = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(kth_to_last_recursive(l2, 2).value, 4)

    def test_kth_to_last_recursive_edge_cases(self):
        # Test case 3: k is greater than the length of the linked list
        l3 = LinkedList([1, 2, 3])
        self.assertIsNone(kth_to_last_recursive(l3, 5))

        # Test case 4: k is 0
        l4 = LinkedList([1, 2, 3])
        self.assertIsNone(kth_to_last_recursive(l4, 0))

        # Test case 5: k is negative
        l5 = LinkedList([1, 2, 3])
        self.assertIsNone(kth_to_last_recursive(l5, -1))

    def test_kth_to_last_recursive_middle(self):
        # Test case 6: Middle of the linked list
        l6 = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(kth_to_last_recursive(l6, 2).value, 4)

if __name__ == '__main__':
    unittest.main()
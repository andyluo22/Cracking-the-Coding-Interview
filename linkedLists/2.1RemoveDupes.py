# Write code to remove duplicates from an unsorted linked list. 
# FOLLOW UP 
# How would you solve this problem if a temporary buffer is not allowed?

from linkedLists import LinkedList

def removeDupes(l1: LinkedList):
    current = l1.head
    prev = None
    seen = set()
    
    while current:
        if current.value in seen:
            prev.next = current.next
        else:
            seen.add(current.value)
            prev = current

        current = current.next
    
    l1.tail = prev
    
    return l1

# The runner technique 
# means that you iterate through the linked list with two pointers simultaneously, with one ahead of the 
# other. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each 
# one node that the "slow" node iterates through.
def removeDupesRunnerTechnique(l1: LinkedList):
    runner = current = l1.head
    while current:
        runner = current
        while runner.next:
            if runner
    


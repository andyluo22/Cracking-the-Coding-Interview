# Write code to partition a linked list around a value x, such that all nodes less than x come 
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need 
# to be after the elements less than x (see below). The partition element x can appear anywhere in the 
# "right partition"; it does not need to appear between the left and right partitions

from LinkedList import LinkedList

def lr_partition(l1: LinkedList, val: int) -> LinkedList:
    left_partition = LinkedList()
    right_partition = LinkedList()
    
    current = l1.head
    
    while current:
        if current.value < val:
            left_partition.add(current.value)
        else:
            right_partition.add(current.value)
        
        current = current.next

    left_partition.tail.next = right_partition.head
    
    return left_partition

test_list = LinkedList()
test_list.add_multiple([3,5,8,5,10,2,1])
print(lr_partition(test_list, 5))   

def partition(l1: LinkedList, val: int) -> LinkedList:
    current = l1.tail = l1.head 
    
    while current:
        if current.value < val:
            l1.head.next = 
        else:
            
        
        current = current.next
    
    





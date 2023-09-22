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

# The ordering is different but they are still correct since partitioning
# doesn't require a specific order for left and right sides 
def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current

        current = next_node

    return ll

    
test_list = LinkedList()
test_list.add_multiple([3,5,8,5,10,2,1])
print(partition(test_list, 5)) 

def test_lr_partition():
    partitioners = [partition, lr_partition]
    for partition_func in partitioners:
        # book example
        ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
        assert not is_partitioned(ll, x=5)
        ll = partition_func(ll, 5)
        assert is_partitioned(ll, x=5), f"{partition_func} did not partition {ll}"

        # random example
        ll = LinkedList.generate(10, 0, 99)
        x = ll.head.value
        ll = partition_func(ll, x)
        assert is_partitioned(ll, x=x), f"{partition_func} did not partition"


def is_partitioned(ll, x):
    seen_gt_partition = False
    for node in ll:
        if node.value >= x:
            seen_gt_partition = True
            continue
        if seen_gt_partition and node.value < x:
            return False
    return True


if __name__ == "__main__":
    test_lr_partition()



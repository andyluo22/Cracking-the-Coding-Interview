# You have two numbers represented by a linked list, where each node contains a single 
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a 
# function that adds the two numbers and returns the sum as a linked list

from LinkedList import LinkedList


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = NumericLinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
            
        print(result)

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)
        

    return ll


def sum_lists_recursive(ll_a, ll_b) -> "NumericLinkedList":
    def sum_lists_helper(ll1_head, ll2_head, remainder, summed_list):
        if ll1_head is None and ll2_head is None:
            if remainder != 0:
                summed_list.add(remainder)
            return summed_list
        elif ll1_head is None:
            result = ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head, ll2_head.next, result // 10, summed_list)
        elif ll2_head is None:
            result = ll1_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head.next, ll2_head, result // 10, summed_list)
        else:
            result = ll1_head.value + ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(
                ll1_head.next, ll2_head.next, result // 10, summed_list
            )

    return sum_lists_helper(ll_a.head, ll_b.head, 0, NumericLinkedList())


class NumericLinkedList(LinkedList):
    def __init__(self, values=None):
        """handle integer as input"""
        if isinstance(values, int):
            values = [int(c) for c in str(values)]
            values.reverse()
        elif isinstance(values, list):
            values = values.copy()

        super().__init__(values)

    def numeric_value(self):
        number = 0
        for place, node in enumerate(self):
            number += node.value * 10**place
        return number
    

l1 = LinkedList()
l2 = LinkedList()

l1.add_multiple([7,3,9])
l2.add_multiple([9,1,2])

print(l1)
print(l2)
print(sum_lists(l1,l2))


print(l1)
print(l2)
print(sum_lists_recursive(l1,l2))

l1 = LinkedList()
l2 = LinkedList()

l1.add_multiple([7,3,9])
l2.add_multiple([9,1])

print(l1)
print(l2)
print(sum_lists(l1,l2))



print(l1)
print(l2)
print(sum_lists_recursive(l1,l2))


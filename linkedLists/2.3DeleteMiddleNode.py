# Implement an algorithm to delete a node in the middle (i.e., any node but 
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to 
# that node

# Super easy but need to think outside the box:  Alter value and then point next appropriately
def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def compare(a, b):
    """which compares the two trees defined by TreeNodes a and b 
    and returns true if they are equal in structure and in value 
    and false otherwise."""
    if a == b:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False
    return compare(a.left, b.left) and compare(a.right, b.right)

a_node = Node(2, None, None)
b_node = Node(2, None, None)


print(compare(a_node, None))
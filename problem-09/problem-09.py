# Problem 9: Node Sum 

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def sum(node):
    # if the node is None, return 0
    if node is None:
        return 0
    
    total_sum = node.value
    # Recursively add the values of all children nodes
    for child in node.children:
        total_sum += sum(child)
    
    return total_sum
    

# Example usage:
if __name__== "__main__" :
    # Create a sample tree
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    child3 = Node(4)
    child4 = Node(5)


    root.children.append(child1)
    root.children.append(child2)
    child1.children.append(child3)
    child1.children.append(child4)
    child2.children.append(Node(6))
    child2.children.append(Node(7))
    child3.children.append(Node(8)) 

    print(sum(root))  # Output: 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
    # Test cases
    assert sum(root) == 36
    assert sum(Node(10)) == 10 
    assert sum(Node(0)) == 0
    assert sum(Node(-5)) == -5


    print("All test cases passed!")




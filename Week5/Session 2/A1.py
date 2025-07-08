# Problem 1: Greatest Node
# Write a function find_max() that takes in the head of a linked list and returns the maximum value in the linked list. You can assume the linked list will contain only numeric values.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_max(head):
#     pass  
# Example Usage:

# head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))
# Expected Output:

# 8
# 8


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    if not head:
        return None
    mx = head.value
    while head:
        mx = max(mx, head.value)
        head = head.next
    return mx


head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))



# Problem 2: Remove Tail
# The following code incorrectly implements the function remove_tail(). When correctly implemented, remove_tail() accepts the head of a singly linked list and removes the last node (the tail) in the list. The function should return the head of the modified list.

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against. Use print statements, print_linked_list(), and the stack trace to identify and fix any bugs so that the function correctly removes the last node from the list.

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
        
# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def remove_tail(head):
#     if head is None:
#         return None
#     if head.next is None:
#         return None 
        
#     current = head
#     while current.next: 
#         current = current.next

#     current.next = None 
#     return head
# Example Usage:

# head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# # Linked List: Isabelle -> Alfonso -> Cyd
# print_linked_list(remove_tail(head))
# Expected Output:

# Isabelle -> Alfonso


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head


head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

print("------REMOVE TAIL TEST CASES------")

# Test case 1: Three nodes
head1 = Node("Isabelle", Node("Alfonso", Node("Cyd")))
print("Test case 1:")
print_linked_list(remove_tail(head1))  # Expected: Isabelle -> Alfonso

# Test case 2: Two nodes
head2 = Node("Mario", Node("Luigi"))
print("Test case 2:")
print_linked_list(remove_tail(head2))  # Expected: Mario

# Test case 3: One node
head3 = Node("Peach")
print("Test case 3:")
print_linked_list(remove_tail(head3))  # Expected: (prints nothing, returns None)

# Test case 4: Empty list
head4 = None
print("Test case 4:")
print_linked_list(remove_tail(head4))  # Expected: (prints nothing, returns None)

# Test case 5: Four nodes
head5 = Node("A", Node("B", Node("C", Node("D"))))
print("Test case 5:")
print_linked_list(remove_tail(head5))  # Expected: A -> B -> C



# Problem 3: Delete Duplicates in a Linked List
# Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). The resulting list should maintain sorted order. Return the head of the linked list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_dupes(head):
#     pass
# Example Usage:

# head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))
# Example Output:

# 1 -> 2 -> 4 -> 5

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next
# #           curr,   curr1        
# #    1 -> 2 -> 3 -> 3 -> 4 -> 5
# #         pc 
# def delete_dupes(head):
#     curr = head
#     dummy = Node(None)
#     dummy.next = head
#     prev = dummy
#     while curr:
#         while curr.next and curr.next.value == curr.value:
#             curr = curr.next
            
#         prev.next = curr
#         prev = curr
#         curr = curr.next
#     return head

# head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))



#    1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
#         p                   c 
#  d
def delete_dupes(head):
    dummy = Node(None)
    dummy.next = head

    curr = head
    prev = dummy

    while curr:
        while curr.next and curr.next.value == curr.value:
            curr = curr.next
        
        if prev.next == curr: # no duplicate
            prev = prev.next
        else: # yes duplicate
            prev.next = curr.next


        curr = curr.next

    return dummy.next

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
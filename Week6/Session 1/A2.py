# Problem 1: Linked List Game
# As the judge of the game show, you are given the head of a linked list of even length containing integers.

# Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer.

# We call each even-indexed node and its next node a pair, e.g., the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.

# For every pair, we compare the values of the nodes in the pair:

# If the odd-indexed node is higher, the "Odd" team gets a point.
# If the even-indexed node is higher, the "Even" team gets a point.
# Write a function game_result() that returns the name of the team with the higher points, if the points are equal, return "Tie".

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# # For testing
# def print_linked_list(head):
# 	current = head
# 	while current:
# 		print(current.value, end=" -> " if current.next else "\n")
# 		current = current.next

# def game_result(head):
#     pass


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

def game_result(head):
    even = 0
    odd = 0
    temp = head

    while temp and temp.next:
        if temp.value > temp.next.value:
            even += 1
        else:
            odd += 1

        temp = temp.next.next

    if even > odd:
          return "Even"
    elif even < odd:
          return "Odd"
    else:
          return "Tie"



game1 = Node(2, Node(1))
game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
game3 = Node(4, Node(5, Node(2, Node(1))))

print(game_result(game1))
print(game_result(game2))
print(game_result(game3))

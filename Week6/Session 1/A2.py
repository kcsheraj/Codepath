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



# Problem 2: Cycle Start
# On your marks, get set, go! Contestants in the game show are racing along a path that contains a loop, but there's a hidden mini challenge: they aren't told where along the path the loop begins. Given the head of a linked list, path_start where each node represents a point in the path, return the value of the node at the start of the loop. If no loop exists in the path, return None.

# A linked list has a cycle or loop if at some point in the list, the node’s next pointer points back to a previous node in the list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    slow = fast = path_start

    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No cycle found
        return None

    # Phase 2: Find cycle start
    slow = path_start
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.value

path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))





# Problem 3: Fastest Wins!
# Contestants, today's challenge is to sort a linked list of items the fastest! The catch - you have to follow a certain technique or you're disqualified from the round. You’ll start with an unsorted lineup, and with each step, you’ll move one item at a time into its proper position until the entire lineup is perfectly ordered.

# Given the head of a linked list, sort the items using the following procedure:

# Start with the first item: The sorted section initially contains just the first item. The rest of the items await their turn in the unsorted section.
# Pick and Place: For each step, pick the next item from the unsorted section, find its correct spot in the sorted section, and place it there.
# Repeat: Continue until all items are in the sorted section.
# Return the head of the sorted linked list.

# As a preview, here is a graphical example of the required technique (also known as the insertion sort algorithm). The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

# Sorting unordered list of integers using insertion sort technique

# When you have finished your sorting, receive bonus points for evaluating the time and space complexity of your solution. To get full points, you must define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

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

def sort_list(head):
    dummy = Node(None)
    dummy.next = head

    sortedPtr = head
    
    while sortedPtr and sortedPtr.next:
        nextPtr = sortedPtr.next

        traverser = dummy
        
        while True:
            if traverser.next.value >= nextPtr.value:
                #insert
                sortedPtr.next = sortedPtr.next.next

                temp = traverser.next
                traverser.next = nextPtr
                nextPtr.next = temp

                if nextPtr.value >= sortedPtr.value:
                     sortedPtr = sortedPtr.next

                break
            else:
                traverser = traverser.next

    return dummy.next

head1 = Node(4, Node(2, Node(1, Node(3))))
head2 = Node(-1, Node(5, Node(3, Node(4, Node(0)))))
head3 = Node(3, Node(2, Node(1, Node(0))))

print_linked_list(sort_list(head1))
print_linked_list(sort_list(head2))
print_linked_list(sort_list(head3))



# Problem 4: Calculate Prize Money
# In the game show, contestants win prize money for each of the challenges they participate in. Write a function get_total_prize() that accepts the heads of two non-empty linked lists, prize_a and prize_b, representing two non-negative integers. The digits are stored in reverse order and each node represents a single digit. The function should add the two numbers and return the sum of the prize money as a linked list.

# The digits of the sum should also be stored in reverse order with each node containing a single digit.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

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

def add_two_numbers(head_a, head_b):
    dummy = Node(None)
    placePtr = dummy

    carry = 0

    aPtr = head_a
    bPtr = head_b

    while aPtr or bPtr or carry:
        curSum = carry

        if aPtr:
            curSum += aPtr.value
            aPtr = aPtr.next
        if bPtr:
            curSum += bPtr.value
            bPtr = bPtr.next

        carry = 0
        
        if curSum > 9:
             carry = (curSum//10)
        
        placePtr.next = Node(curSum%10,None)
        placePtr = placePtr.next

    
    return dummy.next

print("Problem 4")
print("Test 1: 342 + 465 = 807")
head_a = Node(2, Node(4, Node(3)))
head_b = Node(5, Node(6, Node(4)))
print_linked_list(add_two_numbers(head_a, head_b))  # 7 -> 0 -> 8

print("\nTest 2: 123 + 456 = 579")
head_a = Node(3, Node(2, Node(1)))
head_b = Node(6, Node(5, Node(4)))
print_linked_list(add_two_numbers(head_a, head_b))  # 9 -> 7 -> 5

print("\nTest 3: 999 + 1 = 1000")
head_a = Node(9, Node(9, Node(9)))
head_b = Node(1)
print_linked_list(add_two_numbers(head_a, head_b))  # 0 -> 0 -> 0 -> 1

print("\nTest 4: 1 + 999 = 1000")
head_a = Node(1)
head_b = Node(9, Node(9, Node(9)))
print_linked_list(add_two_numbers(head_a, head_b))  # 0 -> 0 -> 0 -> 1

print("\nTest 5: 0 + 0 = 0")
head_a = Node(0)
head_b = Node(0)
print_linked_list(add_two_numbers(head_a, head_b))  # 0

print("\nTest 6: 95 + 17 = 112")
head_a = Node(5, Node(9))
head_b = Node(7, Node(1))
print_linked_list(add_two_numbers(head_a, head_b))  # 2 -> 1 -> 1

print("\nTest 7: 9999999 + 1 = 10000000")
head_a = Node(9, Node(9, Node(9, Node(9, Node(9, Node(9, Node(9)))))))
head_b = Node(1)
print_linked_list(add_two_numbers(head_a, head_b))  # 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 1


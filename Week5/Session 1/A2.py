# Problem 5: Linked Up
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

# A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.

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

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# # Add code here to link the above nodes
# Example Usage:

# print_linked_list(kk_slider)
# Example Output:

# K.K. Slider -> Harriet -> Saharah -> Isabelle


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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

arr = [kk_slider, harriet,saharah,isabelle]
head = kk_slider

for i in range(len(arr)-1):
    curr = arr[i]
    curr.next = arr[i+1]


# print_linked_list(head)




# Problem 6: Got One!
# Imagine that behind the scenes, Animal Crossing uses a linked list to represent the order fish will appear to a player who is fishing in the river. The head of the list represents the next fish that a player will catch if they keep fishing.

# Write a function catch_fish() that accepts the head of a list. The function should:

# Print the name of the fish in the head node using the format "I caught a <fish name>!".
# Remove the first node in the list.
# The function should return the new head of the list. If the list is empty, print "Aw! Better luck next time!" and return None.

# A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided for testing purposes.

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def catch_fish(head):
#     pass
# Example Usage:

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))
# Example Output:

# Carp -> Dace -> Cherry Salmon
# I caught a Carp!
# Dace -> Cherry Salmon
# Aw! Better luck next time!
# None



class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head): # delte, print, return new head

    if head == None:
        print("Aw! Better luck next time!")
        return None

    nextHead = head.next

    deleted = head
    deleted.next = None

    print(f"I caught a {deleted.fish_name}!")


    return nextHead


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))



# Problem 7: Fishing Probability
# Imagine that Animal Crossing is still using a linked list to represent the order fish will appear to a player who is fishing in the river! The head of the list represents the next fish that a player will catch if they keep fishing.

# Write a function fish_chances() that accepts the head of a list and a string fish_name. Return the probability rounded down to the nearest hundredth that the player will catch a fish of type fish_name.

# A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided for testing purposes.

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def fish_chances(head, fish_name):
#     pass
# Example Usage:

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))
# Example Output:

# 0.33
# 0.00

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):

    #caculate length
    #count finish_name ocurr

    fishFound = 0
    length = 0

    temp = head
    while temp:
        if temp.fish_name == fish_name:
            fishFound += 1
        
        length += 1

        temp = temp.next

    return round(fishFound/length,2)

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(f"{fish_chances(fish_list, "Rainbow Trout"):.2f}")

# print(f"{fish_chances(fish_list, 'Dace'):.2f}")
# print(f"{fish_chances(fish_list, 'Rainbow Trout'):.2f}")



# Problem 8: Restocking the Lake
# Imagine that Animal Crossing is still using a linked list to represent the order fish will appear to a player who is fishing! The head of the list represents the next fish that a player will catch if they keep fishing.

# Write a function restock() that accepts the head of a linked list and a string new_fish, and adds a Node with the fish_name new_fish to the end of the list. Return the head of the modified list.

# A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided for testing purposes.

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def restock(head, new_fish):
#     pass
# Example Usage:

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print_linked_list(restock(fish_list, "Rainbow Trout"))
# Example Output:

# Carp -> Dace -> Cherry Salmon -> Rainbow Trout


class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):

    if head == None:
        return Node(new_fish, None)

    temp = head

    while temp.next != None:
        temp = temp.next

    temp.next = Node(new_fish, None)

    return head


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))
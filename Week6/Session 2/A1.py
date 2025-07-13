class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

'''
a-1, b+1
traverse to a-1 --> save the node object
keep traversing to b+1 --> save also

linking 2nd list to the both ends
'''
def merge_playlists(playlist1, playlist2, a, b):

    temp_head = playlist1
    athminus1_node = None
    bthminus1_node = None
    for x in range(b+2):
        if x == a-1:
            athminus1_node = playlist1
        if x == b+1:
            bthminus1_node = playlist1
        
        playlist1= playlist1.next
    
    
    athminus1_node.next = playlist2

    #traverse list 2
    ptrLst2 = playlist2
    while ptrLst2.next != None:
        ptrLst2 = ptrLst2.next
    
    ptrLst2.next = bthminus1_node

    return temp_head
    
    
    

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))

# '''('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant')-> ('Empty', 'Kevin Abstract')'''


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def shuffle_playlist(playlist):
    #get second list
    to_be_reverse_list = has_cycle(playlist)
    
    # reverse at mid
    to_be_reverse_list = reverseList(to_be_reverse_list)

    dummy = Node(None,None)

    while to_be_reverse_list and playlist

        dummy.next = Node(playlist.value, to_be_reverse_list)
        dummy = dummy.next

    




def has_cycle(head):
    slow = head  # Starts at the head
    fast = head  # Also starts at the head

    while fast and fast.next:
        slow = slow.next          # Move slow pointer by one
        fast = fast.next.next     # Move fast pointer by two

    return slow

def reverseList(ListNode):
    """
    Reverses a singly linked list iteratively.

    Args:
        head: The head node of the linked list.

    Returns:
        The new head node of the reversed linked list.
    """
    prev = None  # Pointer to the previous node, initially None
    current = head  # Pointer to the current node, initially the head of the list

    while current is not None:
        # Store the next node before modifying the current node's next pointer
        next_temp = current.next
        
        # Reverse the current node's next pointer to point to the previous node
        current.next = prev
        
        # Move prev to the current node
        prev = current
        
        # Move current to the next node (which was stored in next_temp)
        current = next_temp
        
    # After the loop, prev will be the new head of the reversed list
    return prev
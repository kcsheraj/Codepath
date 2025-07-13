# Problem 1: Selective DNA Deletion
# As a biologist, you are working on editing a long strand of DNA represented as a linked list of nucleotides. Each nucleotide in the sequence is represented as a node in the linked list, where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.

# Given the head of the linked list dna_strand and two integers m and n, write a function edit_dna_sequence() that simulates the selective deletion of nucleotides in a DNA sequence. You will: - Start at the beginning of the DNA strand. - Retain the first m nucleotides from the current position. - Remove the next n nucleotides from the sequence. - Repeat the process until the end of the DNA strand is reached.

# Return the head of the modified DNA sequence after removing the mentioned nucleotides.

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

def edit_dna_sequence(dna_strand, m, n):

    curr = dna_strand


    while curr:

        #move m
        for _ in range(m-1):
            curr = curr.next

            if curr == None:
                break
        
        if curr != None:
            traverser = curr
            #delte n
            for _ in range(n+1):
                traverser = traverser.next

                if traverser == None:
                    break
            
            curr.next = traverser
            curr = curr.next
        

    return dna_strand


dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

print("------EDGE CASES FOR SELECTIVE DNA DELETION------")

# Helper to build a linked list from a string (for DNA)
def build_dna_list(s):
    head = None
    for c in reversed(s):
        head = Node(c, head)
    return head

# Edge Case 1: DNA shorter than m (should return the original list)
dna1 = build_dna_list("AT")
print("Edge Case 1 (DNA shorter than m):")
print_linked_list(edit_dna_sequence(dna1, 3, 2))  # Expected: A -> T

# Edge Case 2: DNA length == m (should return the original list)
dna2 = build_dna_list("ATC")
print("Edge Case 2 (DNA length == m):")
print_linked_list(edit_dna_sequence(dna2, 3, 2))  # Expected: A -> T -> C

# Edge Case 3: DNA length == m + n (should return only the first m nodes)
dna3 = build_dna_list("ATCG")
print("Edge Case 3 (DNA length == m + n):")
print_linked_list(edit_dna_sequence(dna3, 2, 2))  # Expected: A -> T

# Edge Case 4: DNA length == m + n + 1 (should return first m, then last node if not deleted)
dna4 = build_dna_list("ATCGA")
print("Edge Case 4 (DNA length == m + n + 1):")
print_linked_list(edit_dna_sequence(dna4, 2, 2))  # Expected: A -> T -> A

# Edge Case 5: DNA length is a multiple of m + n
dna5 = build_dna_list("ATCGATCG")
print("Edge Case 5 (multiple of m+n):")
print_linked_list(edit_dna_sequence(dna5, 2, 2))  # Expected: A -> T -> A -> T

# Edge Case 6: DNA length is not a multiple of m + n
dna6 = build_dna_list("ATCGATCGA")
print("Edge Case 6 (not a multiple of m+n):")
print_linked_list(edit_dna_sequence(dna6, 2, 2))  # Expected: A -> T -> A -> T -> A

# Edge Case 7: Only one nucleotide
dna7 = build_dna_list("A")
print("Edge Case 7 (single nucleotide):")
print_linked_list(edit_dna_sequence(dna7, 1, 1))  # Expected: A

# Edge Case 8: All nucleotides deleted after first m
dna8 = build_dna_list("ATCG")
print("Edge Case 8 (delete all after first m):")
print_linked_list(edit_dna_sequence(dna8, 2, 10))  # Expected: A -> T

# Edge Case 9: m = 1, n = 1 (alternate keep/delete)
dna9 = build_dna_list("ATCGATCG")
print("Edge Case 9 (alternate keep/delete):")
print_linked_list(edit_dna_sequence(dna9, 1, 1))  # Expected: A -> C -> A -> C




# # Problem 2: Protein Folding Loop Detection
# # As a biochemist, you're studying the folding patterns of proteins, which are represented as a sequence of amino acids linked together. These proteins sometimes fold back on themselves, creating loops that can impact their function.

# # Given the head of a linked list protein where each node in the linked list represents an amino acid in the protein, return an array with the values of any cycle in the list. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

# # The values may be returned in any order.

# # Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next

# # def cycle_length(protein):
# #     pass
# # Example Usage:

# # Linked list with 4 nodes and a cycle where 4th node points to 2nd node

# # protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
# # protein_head.next.next.next.next = protein_head.next 

# # print(cycle_length(protein_head))
# # Example Output:

# # ['Gly', 'Leu', 'Val']



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    ans = []

    #find loop -> remeber place where meet does not mean start of loop
    fast = protein
    slow = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    fast = fast.next
    while fast != slow:
        ans.append(fast.value)
        fast = fast.next
    
    ans.append(fast.value) #start

    return ans


protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print("problem 2")
print(cycle_length(protein_head))

print("------PROTEIN FOLDING LOOP DETECTION TEST CASES------")

# Helper to build a linked list from a list of values, with optional cycle
def build_protein(values, cycle_pos=None):
    head = Node(values[0])
    current = head
    nodes = [head]
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
    if cycle_pos is not None:
        current.next = nodes[cycle_pos]
    return head

# Test case 1: Example from prompt (cycle: Val -> Gly)
protein1 = build_protein(['Ala', 'Gly', 'Leu', 'Val'], cycle_pos=1)
print("Test case 1:", cycle_length(protein1))  # Expected: ['Gly', 'Leu', 'Val'] (order may vary)

# Test case 3: Cycle of length 1 (node points to itself)
protein3 = Node('Met')
protein3.next = protein3
print("Test case 3:", cycle_length(protein3))  # Expected: ['Met']

# Test case 4: Cycle includes all nodes
protein4 = build_protein(['A', 'B', 'C', 'D'], cycle_pos=0)
print("Test case 4:", cycle_length(protein4))  # Expected: ['A', 'B', 'C', 'D'] (order may vary)

# Test case 5: Cycle at the end (last node points to itself)
protein5 = build_protein(['X', 'Y', 'Z'])
protein5.next.next.next = protein5.next.next
print("Test case 5:", cycle_length(protein5))  # Expected: ['Z']


# Test case 7: Two nodes, cycle between them
protein7 = Node('A')
protein7.next = Node('B')
protein7.next.next = protein7
print("Test case 7:", cycle_length(protein7))  # Expected: ['A', 'B'] (order may vary)

# Test case 8: Three nodes, cycle starts at second node
protein8 = build_protein(['Phe', 'Tyr', 'Trp'], cycle_pos=1)
print("Test case 8:", cycle_length(protein8))  # Expected: ['Tyr', 'Trp'] (order may vary)


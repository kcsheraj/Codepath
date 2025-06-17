# Problem 1: Transpose Matrix
# Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

# 3x3 matrix before and after being transposed

# def transpose(matrix):
#     pass
# Example Usage

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose(matrix)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# transpose(matrix)
# Example Output:

# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]



def transpose(matrix):
    ansArr = []
    origRows = len(matrix)
    origCols = len(matrix[0])

    for r in range(origCols):
        newRow = []
        for c in range(origRows):
            newRow.append(matrix[c][r])

        ansArr.append(newRow)
        

    return ansArr




# Test case 1: 3x3 matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Test case 1 (3x3):")
print(transpose(matrix1))  # Expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Test case 2: 2x3 matrix
matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Test case 2 (2x3):")
print(transpose(matrix2))  # Expected: [[1, 4], [2, 5], [3, 6]]

# Test case 3: 1x3 matrix
matrix3 = [
    [1, 2, 3]
]
print("Test case 3 (1x3):")
print(transpose(matrix3))  # Expected: [[1], [2], [3]]

# Test case 4: 3x1 matrix
matrix4 = [
    [1],
    [2],
    [3]
]
print("Test case 4 (3x1):")
print(transpose(matrix4))  # Expected: [[1, 2, 3]]
# ...existing code...




# Problem 2: Two-Pointer Reverse List
# Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

# Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

# def reverse_list(lst):
#     pass
# Example Usage

# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# reverse_list(lst)
# Example Output:

# ["eeyore", "roo", "piglet", "christopher robin", "pooh"]

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:

        lst[left], lst[right] = lst[right], lst[left]



        left += 1
        right -= 1

    return lst


# ...existing code...

print("-----PROBLEM 2------")

print("Test case 1 (strings):")
lst1 = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst1))  # Expected: ["eeyore", "roo", "piglet", "christopher robin", "pooh"]

print("Test case 2 (numbers):")
lst2 = [1, 2, 3, 4, 5]
print(reverse_list(lst2))  # Expected: [5, 4, 3, 2, 1]

print("Test case 3 (single element):")
lst3 = [42]
print(reverse_list(lst3))  # Expected: [42]

print("Test case 4 (empty list):")
lst4 = []
print(reverse_list(lst4))  # Expected: []

print("Test case 5 (even number of elements):")
lst5 = [10, 20, 30, 40]
print(reverse_list(lst5))  # Expected: [40, 30, 20, 10]
# ...existing code...


# Problem 3: Remove Duplicates
# Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

# def remove_dupes(items):
#     pass
# Example Usage

# items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
# remove_dupes(items)

# items = ["extract of malt", "haycorns", "honey", "thistle"]
# remove_dupes(items)
# Example Output:

# 4
# 4

def remove_dupes(items):
    length = len(items)
    count_dupes = 0
    i = 0
    j = i + 1
    last = length - 1
    while i < last:
        while j  < last:
            if items[i] == items[j]:
              items[j], items[last] = items[last], items[j]
              last -= 1
            if items[j] != items[i]: 
              j+=1
            
        i += 1
    return last + 1



# def remove_dupes(items):
#     if not items:
#         return 0
    
#     i = 0  # Pointer for the position of the last unique element
    
#     for j in range(1, len(items)):
#         if items[j] != items[i]:
#             i += 1
#             items[i] = items[j]
    
#     return i + 1


# ...existing code...

print("-----PROBLEM 3------")

# Test case 1: With duplicates at the end
items1 = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
length1 = remove_dupes(items1)
print(f"Test case 1: {items1[:length1]}, Length: {length1}")  # Expected: ['extract of malt', 'haycorns', 'honey', 'thistle'], Length: 4

# Test case 2: No duplicates
items2 = ["extract of malt", "haycorns", "honey", "thistle"]
length2 = remove_dupes(items2)
print(f"Test case 2: {items2[:length2]}, Length: {length2}")  # Expected: ['extract of malt', 'haycorns', 'honey', 'thistle'], Length: 4

# Test case 3: All elements are duplicates
items3 = ["honey", "honey", "honey"]
length3 = remove_dupes(items3)
print(f"Test case 3: {items3[:length3]}, Length: {length3}")  # Expected: ['honey'], Length: 1

# Test case 4: Empty list
items4 = []
length4 = remove_dupes(items4)
print(f"Test case 4: {items4[:length4]}, Length: {length4}")  # Expected: [], Length: 0

# Test case 5: Single element
items5 = ["pooh"]
length5 = remove_dupes(items5)
print(f"Test case 5: {items5[:length5]}, Length: {length5}")  # Expected: ['pooh'], Length: 1

# Test case 6: Duplicates in the middle
items6 = ["a", "b", "b", "c", "d", "d", "e"]
length6 = remove_dupes(items6)
print(f"Test case 6: {items6[:length6]}, Length: {length6}")  # Expected: ['a', 'b', 'c', 'd', 'e'], Length: 5
# ...existing code...
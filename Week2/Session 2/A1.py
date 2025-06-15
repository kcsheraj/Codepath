# Problem 1: Balanced Art Collection
# As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

# Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

# A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

# def find_balanced_subsequence(art_pieces):
#     pass
# Example Usage:

# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))
# Example Output:

# 5
# Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

# 2
# 0

# art_pieces1 = [1,3,2,2,5,2,3,7]

# 1 - 1
# 2 - 3
# 3 - 2
# 5 - 1
# 7 - 1

# 0
# 4
# 5
from collections import Counter 
def find_balanced_subsequence(art_pieces):
    hashMap = Counter(art_pieces)
    maxSubLen = 0
    
    for piece in hashMap:
        if piece + 1 in hashMap:
            maxSubLen = max(maxSubLen, hashMap[piece] + hashMap[piece + 1])
    
    return maxSubLen

print("------PROBLEM 1 TEST CASES------")

# Test case 1: Example from prompt
art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
print(f"Test case 1: {art_pieces1} -> {find_balanced_subsequence(art_pieces1)}")  # Expected: 5

# Test case 2: Consecutive numbers
art_pieces2 = [1, 2, 3, 4]
print(f"Test case 2: {art_pieces2} -> {find_balanced_subsequence(art_pieces2)}")  # Expected: 2

# Test case 3: All the same number
art_pieces3 = [1, 1, 1, 1]
print(f"Test case 3: {art_pieces3} -> {find_balanced_subsequence(art_pieces3)}")  # Expected: 0

# Test case 4: Two numbers, difference is 1
art_pieces4 = [5, 6, 5, 6, 5]
print(f"Test case 4: {art_pieces4} -> {find_balanced_subsequence(art_pieces4)}")  # Expected: 5

# Test case 5: No balanced subsequence
art_pieces5 = [1, 3, 5, 7]
print(f"Test case 5: {art_pieces5} -> {find_balanced_subsequence(art_pieces5)}")  # Expected: 0

# Test case 6: Multiple possible pairs
art_pieces6 = [2, 2, 3, 3, 3, 4, 4]
print(f"Test case 6: {art_pieces6} -> {find_balanced_subsequence(art_pieces6)}")  # Expected: 5

# Test case 7: Single element
art_pieces7 = [10]
print(f"Test case 7: {art_pieces7} -> {find_balanced_subsequence(art_pieces7)}")  # Expected: 0

# ...existing code...




# Problem 2: Verifying Authenticity
# Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].

# The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

# Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.

# Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.

# def is_authentic_collection(art_pieces):
#     pass
# Example Usage:

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# [1, 2, 3, 3]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))
# Example Output:

# False
# Example 1 Explanation: Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# However, base[3] has four elements but array collection1 has three. Therefore, 
# it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

# True
# Example 2 Explanation:  Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# It can be seen that collection2 is a permutation of base[3] = [1, 2, 3, 3] 
# (by swapping the second and fourth elements in nums, we reach base[3]).
#  Therefore, the answer is true.

# True
# Example 3 Explanation; Since the maximum element of the array is 1, 
# the only candidate n for which this array could be a permutation of base[n], 
# is n = 1. It can be seen that collection3 is a permutation of base[1] = [1, 1].
#  Therefore, the answer is true.

from collections import Counter

def is_authentic_collection(art_pieces):
    if not art_pieces:
        return False
    
    n = max(art_pieces)
    
    if len(art_pieces) != n + 1:
        return False
    
    counter = Counter(art_pieces)
    
    # Check 1 to n-1 each occurs once
    for i in range(1, n):
        if counter[i] != 1:
            return False
    
    # Check n occurs exactly twice
    if counter[n] != 2:
        return False
    
    return True



print("------PROBLEM 2 TEST CASES------")

collection1 = [2, 1, 3]
print(f"Test case 1: {collection1} -> {is_authentic_collection(collection1)}")  # Expected: False

collection2 = [1, 3, 3, 2]
print(f"Test case 2: {collection2} -> {is_authentic_collection(collection2)}")  # Expected: True

collection3 = [1, 1]
print(f"Test case 3: {collection3} -> {is_authentic_collection(collection3)}")  # Expected: True

# Additional test cases
collection4 = [1, 2, 2]
print(f"Test case 4: {collection4} -> {is_authentic_collection(collection4)}")  # Expected: True (base[2] = [1,2,2])

collection5 = [1, 2, 3, 4, 4]
print(f"Test case 5: {collection5} -> {is_authentic_collection(collection5)}")  # Expected: True (base[4] = [1,2,3,4,4])

collection6 = [1, 2, 3, 4]
print(f"Test case 6: {collection6} -> {is_authentic_collection(collection6)}")  # Expected: False (length should be 5 for n=4)

collection7 = [1, 2, 3, 3, 4]
print(f"Test case 7: {collection7} -> {is_authentic_collection(collection7)}")  # Expected: False (should be [1,2,3,4,4] for n=4)

# ...existing code...
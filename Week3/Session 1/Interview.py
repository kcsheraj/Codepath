# Problem 1: Balanced Art Collection

# As the curator of an art gallery, you are organizing a new exhibition.
#  You must ensure the collection of art pieces are balanced to attract
#  the right range of buyers. A balanced collection is one where the difference between
#  the maximum and minimum value of the art pieces is exactly 1.

# Given an integer array art_pieces representing the value of each art piece
# write a function find_balanced_subsequence() that returns the length of the
# longest balanced subsequence.

# A subsequence is a sequence derived from the array by deleting some or no
# elements without changing the order of the remaining elements.



# def find_balanced_subsequence(art_pieces):
#     pass




# Example Usage:

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces1.5 = [1,3,2,2,5,6,3,7, 5, 6, 5] => 5
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

# 3, 2, 2, 2, 3
# 3, 1, 1, 1, 3




# Example Output:

# 5
# Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

# 2
# 0

from collections import Counter
def find_balanced_subsequence(art_pieces):
    # num : occurence
    # {1 : 1, 
    #  3 : 2, 
    #  2 : 3, 
    #  5 : 1, 
    #  7 : 1}

    price_freq = dict(Counter(art_pieces))

    output = 0
    for price in list(set(art_pieces)): #[1, 3, 2, 5, 7]

        if price in price_freq.keys() and price+1 in price_freq.keys():
            output = max(price_freq[price] + price_freq[price + 1], output)
        

        if price in price_freq.keys() and price-1 in price_freq.keys():
            output = max(price_freq[price] + price_freq[price - 1], output)
    
    return output







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

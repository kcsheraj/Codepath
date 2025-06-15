# Problem 3: Find All Duplicate Treasure Chests in an Array
# Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

# def find_duplicate_chests(chests):
#     pass
# Example Usage:

# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))
# Example Output:

# [2, 3]
# [1]
# []
def find_duplicate_chests(chests):
    ans = []
    mySet = set()
    for num in chests:
        if num in mySet:
            ans.append(num)
        else:
            mySet.add(num)
    
    return ans

print("-------PROBELM 3-------")

# Test cases for find_duplicate_chests
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
print("Test case 1:", find_duplicate_chests(chests1))  # Expected: [2, 3]

chests2 = [1, 1, 2]
print("Test case 2:", find_duplicate_chests(chests2))  # Expected: [1]

chests3 = [1]
print("Test case 3:", find_duplicate_chests(chests3))  # Expected: []

chests4 = [2, 2, 2, 2]
print("Test case 4:", find_duplicate_chests(chests4))  # Expected: [2, 2, 2]

chests5 = [5, 4, 3, 2, 1]
print("Test case 5:", find_duplicate_chests(chests5))  # Expected: []
# ...existing code...


# Problem 4: Booby Trap
# Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

# Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

# def is_balanced(code):
#     pass
# Example Usage:

# code1 = "arghh"
# code2 = "haha"

# print(is_balanced(code1)) 
# print(is_balanced(code2)) 
# Example Output:

# True
# Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

# False
# Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2,

def is_balanced(code):

    hashMap = {}
    for char in code:
        hashMap[char] = hashMap.get(char, 0) + 1
    
    for key in hashMap:
        hashMap[key] -= 1
        ocurr = hashMap[key]

        #find see if all frequences are equal - true
        
        freqs = []
         # Step 2: Loop through all values in hashMap
        for v in hashMap.values():
            # Step 3: Only consider frequencies greater than 0 (ignore zeros)
            if v > 0:
                freqs.append(v)

        # Step 4: Check if all frequencies in the list are the same
        # This is true if the set of freqs has only one unique value
        if len(freqs) > 0 and len(set(freqs)) == 1:
            return True

            
        hashMap[key] += 1

    return False



print("-------PROBELM 4-------")

# Test case 1: Example from prompt, should be True
code1 = "arghh"
print(f"Test case 1: {code1} -> {is_balanced(code1)}")  # Expected: True

# Test case 2: Example from prompt, should be False
code2 = "haha"
print(f"Test case 2: {code2} -> {is_balanced(code2)}")  # Expected: False


code3 = "abcd"
print(f"Test case 3: {code3} -> {is_balanced(code3)}")  # Expected: False

# Test case 4: Remove one to balance, should be True
code4 = "aabbccddc"
print(f"Test case 4: {code4} -> {is_balanced(code4)}")  # Expected: True

# Test case 5: Only one letter, should be True (removing one leaves all equal)
code5 = "a"
print(f"Test case 5: {code5} -> {is_balanced(code5)}")  # Expected: True

# Test case 6: Two of the same letter, should be True
code6 = "aa"
print(f"Test case 6: {code6} -> {is_balanced(code6)}")  # Expected: True

# Test case 7: Impossible to balance, should be False
code7 = "aabbccc"
print(f"Test case 7: {code7} -> {is_balanced(code7)}")  # Expected: False

# Test case 8: Remove one to balance, should be True
code8 = "aabbccdde"
print(f"Test case 8: {code8} -> {is_balanced(code8)}")  # Expected: True
# ...existing code...





# Problem 5: Overflowing With Gold
# Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on their ship.

# Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, return the indices of the two locations whose gold amounts add up to the target.

# Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

# def find_treasure_indices(gold_amounts, target):
#     pass
# Example Usage:

# gold_amounts1 = [2, 7, 11, 15]
# target1 = 9

# gold_amounts2 = [3, 2, 4]
# target2 = 6

# gold_amounts3 = [3, 3]
# target3 = 6

# print(find_treasure_indices(gold_amounts1, target1))  
# print(find_treasure_indices(gold_amounts2, target2))  
# print(find_treasure_indices(gold_amounts3, target3))  
# Example Output:

# [0, 1]
# [1, 2]
# [0, 1]

print("-------PROBELM 5-------")
def find_treasure_indices(gold_amounts, target):

    hashMap = {}

    index1 = 0
    for num in gold_amounts:
        hashMap[num] = index1
        index1 += 1

    ans = []
    index2 = 0
    for num in gold_amounts:
        look = target - num

        if look in hashMap:
            ans.append(index1)
            ans.append(index2)
            reu
        
        index2 += 1


    return ans

    

    

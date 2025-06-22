# Problem 1: Arrange Guest Arrival Order
# You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.

# You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

# guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
# If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
# If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
# Return the lexicographically smallest possible string guest_order that meets the conditions.

# def arrange_guest_arrival_order(arrival_pattern):
#   pass
# Example Usage:

# print(arrange_guest_arrival_order("IIIDIDDD"))  
# print(arrange_guest_arrival_order("DDD"))  
# Example Output:

# 123549876
# 4321

# DDD
# Gest_order -> 4,3,2,1


# III
# Gest_order -> 1,2,3,4

# DIII
# Gest_order -> 2,1,3,4,5

#stackIndices -> 
#IIIID
# nextSmallest- > 1,2,3,4,5, 6,7,8,9
#                 i
def arrange_guest_arrival_order(arrival_pattern):

    guest_order = []
    stack = []

    for i in range(len(arrival_pattern)+1):

        nextNum = i+1

        stack.append(nextNum)

       # Only access patternLetter if within bounds or you reach a I
        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while len(stack) != 0:
                top = stack.pop()
                guest_order.append(str(top))
    


    return "".join(guest_order)


print("------PROBLEM 1 TEST CASES------")

# Test case 1: Example from prompt
pattern1 = "IIIDIDDD"
print(f"Test case 1: {pattern1} -> {arrange_guest_arrival_order(pattern1)}")  # Expected: 123549876

# Test case 2: All 'D'
pattern2 = "DDD"
print(f"Test case 2: {pattern2} -> {arrange_guest_arrival_order(pattern2)}")  # Expected: 4321

# Test case 3: All 'I'
pattern3 = "III"
print(f"Test case 3: {pattern3} -> {arrange_guest_arrival_order(pattern3)}")  # Expected: 1234

# Test case 4: 'DIII'
pattern4 = "DIII"
print(f"Test case 4: {pattern4} -> {arrange_guest_arrival_order(pattern4)}")  # Expected: 21345

# Test case 5: Alternating 'IDID'
pattern5 = "IDID"
print(f"Test case 5: {pattern5} -> {arrange_guest_arrival_order(pattern5)}")  # Expected: 13254

# Test case 6: Single 'I'
pattern6 = "I"
print(f"Test case 6: {pattern6} -> {arrange_guest_arrival_order(pattern6)}")  # Expected: 12

# Test case 7: Single 'D'
pattern7 = "D"
print(f"Test case 7: {pattern7} -> {arrange_guest_arrival_order(pattern7)}")  # Expected: 21

# Test case 8: Empty pattern
pattern8 = ""
print(f"Test case 8: '{pattern8}' -> {arrange_guest_arrival_order(pattern8)}")  # Expected: 1
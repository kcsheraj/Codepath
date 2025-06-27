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


# Problem 2: Reveal Attendee List in Order
# You are organizing an event where attendees have unique registration numbers. These numbers are provided in the list attendees. You need to arrange the attendees in a way that, when their registration numbers are revealed one by one, the numbers appear in increasing order.

# The process of revealing the attendee list follows these steps repeatedly until all registration numbers are revealed:

# Take the top registration number from the list, reveal it, and remove it from the list.
# If there are still registration numbers in the list, take the next top registration number and move it to the bottom of the list.
# If there are still unrevealed registration numbers, go back to step 1. Otherwise, stop.
# Return an ordering of the registration numbers that would reveal the attendees in increasing order.

# def reveal_attendee_list_in_order(attendees):
#   pass
# Example Usage:

# print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
# print(reveal_attendee_list_in_order([1,1000]))  
# Example Output:

# [2,13,3,11,5,17,7]
# [1,1000]

from collections import deque
def reveal_attendee_list_in_order(attendees):
    sortedArr = sorted(attendees)
    queue = deque()

    for i in range(len(sortedArr) - 1, -1, -1):
        if queue:
            queue.appendleft(queue.pop())
        
        queue.appendleft(sortedArr[i])
    return list(queue)


print("------PROBLEM 2 TEST CASES------")

# Test case 1: Example from prompt
attendees1 = [17, 13, 11, 2, 3, 5, 7]
print(f"Test case 1: {attendees1} -> {reveal_attendee_list_in_order(attendees1)}")  # Expected: [2, 13, 3, 11, 5, 17, 7]

# Test case 2: Example from prompt (two attendees)
attendees2 = [1, 1000]
print(f"Test case 2: {attendees2} -> {reveal_attendee_list_in_order(attendees2)}")  # Expected: [1, 1000]

# Test case 3: Already sorted
attendees3 = [1, 2, 3, 4]
print(f"Test case 3: {attendees3} -> {reveal_attendee_list_in_order(attendees3)}")  # Expected: [1, 3, 2, 4]

# Test case 4: Reverse order
attendees4 = [4, 3, 2, 1]
print(f"Test case 4: {attendees4} -> {reveal_attendee_list_in_order(attendees4)}")  # Expected: [1, 3, 2, 4]

# Test case 5: Single attendee
attendees5 = [42]
print(f"Test case 5: {attendees5} -> {reveal_attendee_list_in_order(attendees5)}")  # Expected: [42]

# Test case 6: Empty list
attendees6 = []
print(f"Test case 6: {attendees6} -> {reveal_attendee_list_in_order(attendees6)}")  # Expected: []

# Test case 7: Five attendees
attendees7 = [10, 20, 30, 40, 50]
print(f"Test case 7: {attendees7} -> {reveal_attendee_list_in_order(attendees7)}")  # Expected: [10, 30, 20, 40, 50]



# Problem 3: Arrange Event Attendees by Priority
# You are organizing a large event and need to arrange the attendees based on their priority levels. You are given a 0-indexed list attendees, where each element represents the priority level of an attendee, and an integer priority that indicates a particular level of priority.

# Your task is to rearrange the attendees list such that the following conditions are met:

# Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
# Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
# The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
# Return the attendees list after the rearrangement.

# def arrange_attendees_by_priority(attendees, priority):
#   pass
# Example Usage:

# print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
# print(arrange_attendees_by_priority([-3,4,3,2], 2)) 
# Example Output:

# [9,5,3,10,10,12,14]
# [-3,2,4,3]


def arrange_attendees_by_priority(attendees, priority):
    left = 0
    right = len(attendees) - 1
    i = 0

    while i <= right:
        if attendees[i] < priority:
            attendees[left], attendees[i] = attendees[i], attendees[left]
            left += 1
            i += 1
        elif attendees[i] > priority:
            attendees[right], attendees[i] = attendees[i], attendees[right]
            right -= 1
        else:
            i += 1


    return attendees




#     Problem 4: Rearrange Guests by Attendance and Absence
# You are organizing an event, and you have a 0-indexed list guests of even length, where each element represents either an attendee (positive integers) or an absence (negative integers). The list contains an equal number of attendees and absences.

# You should return the guests list rearranged to satisfy the following conditions:

# Every consecutive pair of elements must have opposite signs, indicating that each attendee is followed by an absence or vice versa.
# For all elements with the same sign, the order in which they appear in the original list must be preserved.
# The rearranged list must begin with an attendee (positive integer).
# Return the rearranged list after organizing the guests according to the conditions.

# def rearrange_guests(guests):
#   pass
# Example Usage:

# print(rearrange_guests([3,1,-2,-5,2,-4]))  
# print(rearrange_guests([-1,1])) 
# Example Output:

# [3,-2,1,-5,2,-4]
# [1,-1]


def rearrange_guests(guests):

    return None
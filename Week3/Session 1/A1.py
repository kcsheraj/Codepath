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


from collections import deque

def rearrange_guests(guests):

    ansArr = []

    pos = deque()
    neg = deque()

    for num in guests:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
        
    while pos and neg:
        ansArr.append(pos.popleft())
        ansArr.append(neg.popleft())

    while pos:
        ansArr.append(pos.popleft())

    while neg:
        ansArr.append(neg.popleft())

    return ansArr

print("------PROBLEM 4 TEST CASES------")

# Test case 1: Example from prompt
guests1 = [3, 1, -2, -5, 2, -4]
print(f"Test case 1: {guests1} -> {rearrange_guests(guests1)}")  # Expected: [3, -2, 1, -5, 2, -4]

# Test case 2: Example from prompt (only one attendee and one absence)
guests2 = [-1, 1]
print(f"Test case 2: {guests2} -> {rearrange_guests(guests2)}")  # Expected: [1, -1]

# Test case 3: Already arranged
guests3 = [1, -1, 2, -2]
print(f"Test case 3: {guests3} -> {rearrange_guests(guests3)}")  # Expected: [1, -1, 2, -2]

# Test case 4: Reverse order
guests4 = [-2, 2, -1, 1]
print(f"Test case 4: {guests4} -> {rearrange_guests(guests4)}")  # Expected: [2, -2, 1, -1]

# Test case 5: Single attendee
guests5 = [42]
print(f"Test case 5: {guests5} -> {rearrange_guests(guests5)}")  # Expected: [42]

# Test case 6: Empty list
guests6 = []
print(f"Test case 6: {guests6} -> {rearrange_guests(guests6)}")  # Expected: []

# Test case 7: Consecutive attendees and absences
guests7 = [1, 2, 3, -1, -2, -3]
print(f"Test case 7: {guests7} -> {rearrange_guests(guests7)}")  # Expected: [1, -1, 2, -2, 3, -3]



# Problem 5: Minimum Changes to Make Schedule Balanced
# You are organizing a series of events, and each event is represented by a parenthesis in the string schedule, where an opening parenthesis ( represents the start of an event, and a closing parenthesis ) represents the end of an event. A balanced schedule means every event that starts has a corresponding end.

# However, due to some scheduling issues, the current schedule might not be balanced. In one move, you can insert either a start or an end at any position in the schedule.

# Return the minimum number of moves required to make the schedule balanced.

# def min_changes_to_make_balanced(schedule):
#   pass
# Example Usage:

# print(min_changes_to_make_balanced("())"))
# print(min_changes_to_make_balanced("(((")) 
# Example Output:

# 1
# 3


def min_changes_to_make_balanced(schedule):

    numOp = 0
    stack = []

    for bracket in schedule:
        if bracket == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                numOp += 1
            else:
                stack.pop()
    
    if stack:
        numOp += len(stack)

    return numOp

print("------PROBLEM 5 TEST CASES------")

# Test case 1: Example from prompt
schedule1 = "())"
print(f"Test case 1: {schedule1} -> {min_changes_to_make_balanced(schedule1)}")  # Expected: 1

# Test case 2: Example from prompt
schedule2 = "((("
print(f"Test case 2: {schedule2} -> {min_changes_to_make_balanced(schedule2)}")  # Expected: 3

# Test case 3: Already balanced
schedule3 = "()()"
print(f"Test case 3: {schedule3} -> {min_changes_to_make_balanced(schedule3)}")  # Expected: 0

# Test case 4: All closing
schedule4 = "))))"
print(f"Test case 4: {schedule4} -> {min_changes_to_make_balanced(schedule4)}")  # Expected: 4

# Test case 5: All opening
schedule5 = "(((("
print(f"Test case 5: {schedule5} -> {min_changes_to_make_balanced(schedule5)}")  # Expected: 4

# Test case 6: Alternating, needs one change
schedule6 = "(()))("
print(f"Test case 6: {schedule6} -> {min_changes_to_make_balanced(schedule6)}")  # Expected: 2

# Test case 7: Empty string
schedule7 = ""
print(f"Test case 7: '{schedule7}' -> {min_changes_to_make_balanced(schedule7)}")  # Expected: 0




# Problem 6: Marking the Event Timeline
# You are organizing a large event, and you need to mark the timeline for a series of scheduled activities.

# You are given two strings:

# event: A short string representing an event name.
# timeline: A longer string representing the full timeline for the event.
# Initially, the timeline is empty and represented by a string t of the same length as timeline, where every character is '?'.

# In one turn, you can "mark" the timeline by placing the event string over any valid position in t and copying its letters onto t. This replaces the corresponding '?' characters in t.

# Rules:

# You can only place event where it fully fits within t.
# Each time you mark the timeline, the corresponding letters in t are updated.
# Your goal is to perform a sequence of marks so that t becomes exactly equal to timeline.
# You may use at most 10 * len(timeline) marks.
# Return a list of the starting indices where you placed the event string during each mark. If it is impossible to turn t into timeline following these rules, return an empty list.

# def mark_event_timeline(event, timeline):
#   pass
# Example Usage:

# print(mark_event_timeline("abc", "ababc"))  
# print(mark_event_timeline("abca", "aabcaca")) 
# Example Output:

# [0, 2]
# [3, 0, 1]
# Explanation

# For "ababc":

# Start with t = "?????"
# Place "abc" at index 0 → t = "abc??"
# Place "abc" at index 2 → t = "ababc" — timeline is complete.

# timeline - ababc
# abc??
# ?abc?
# ??abc

# def mark_event_timeline(event, timeline):

#     t = "?" * len(timeline)

#     queue = deque()

#     queue.append((t,[]))

#     while queue:
#         tupleElement = queue.popleft()
        
#         currTState = tupleElement[0]

#         for i in range(len(currTState)-len(event) + 1):
#             temp = currTState

#             for j in range(i, i+len(event)):
#                 temp[j] = event[j-i]
            









#     return None

# mark_event_timeline("abc", "ababc")
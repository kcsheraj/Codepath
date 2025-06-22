# Problem 1: Extra Treats
# In a pet adoption center, there are two groups of volunteers: the "Cat Lovers" and the "Dog Lovers."

# The center is deciding on which type of pet should be receive extra treats that week, and the voting takes place in a round-based procedure. In each round, each volunteer can exercise one of the two rights:

# Ban one volunteer's vote: A volunteer can make another volunteer from the opposite group lose all their rights in this and all the following rounds.
# Announce the victory: If a volunteer finds that all the remaining volunteers with the right to vote are from the same group, they can announce the victory for their group and prioritize their preferred pet for extra treats.
# Given a string votes representing each volunteer's group affiliation. The character 'C' represents "Cat Lovers" and 'D' represents "Dog Lovers". The length of the given string represents the number of volunteers.

# Predict which group will finally announce the victory and prioritize their preferred pet for extra treats. The output should be "Cat Lovers" or "Dog Lovers".

# def predictAdoption_victory(votes):
#   pass
# Example Usage:

# print(predictAdoption_victory("CD")) 
# print(predictAdoption_victory("CDD")) 
# Example Output:

# Cat Lovers
# Dog Lovers

from collections import deque

def predictAdoption_victory(votes):
    votesLen = len(votes)
    
    CQueue = deque()
    DQueue = deque()

    #create queues
    for i, char in enumerate(votes):
        if char == "C":
            CQueue.append(i)
        else:
            DQueue.append(i)

    # simulate voting
    while len(CQueue) != 0 and len(DQueue) != 0:

        #smaller index votes
        Ctop = CQueue[0]
        Dtop = DQueue[0]

        if Ctop < Dtop:
            DQueue.popleft()
        
            CQueue.append(CQueue.popleft() + votesLen)
        else:
            CQueue.popleft()

            DQueue.append(DQueue.popleft() + votesLen)
    
    if len(CQueue) != 0:
        return "Cat Lovers"
    else:
        return "Dog Lovers"





print("------PROBLEM 1 TEST CASES------")

# Test case 1: Cat wins
votes1 = "CD"
print(f"Test case 1: {votes1} -> {predictAdoption_victory(votes1)}")  # Expected: Cat Lovers

# Test case 2: Dog wins
votes2 = "CDD"
print(f"Test case 2: {votes2} -> {predictAdoption_victory(votes2)}")  # Expected: Dog Lovers

# Test case 3: Cat wins with more cats
votes3 = "CCDDC"
print(f"Test case 3: {votes3} -> {predictAdoption_victory(votes3)}")  # Expected: Cat Lovers

# Test case 4: Dog wins with more dogs
votes4 = "DCCDD"
print(f"Test case 4: {votes4} -> {predictAdoption_victory(votes4)}")  # Expected: Dog Lovers

# Test case 5: All cats
votes5 = "CCCC"
print(f"Test case 5: {votes5} -> {predictAdoption_victory(votes5)}")  # Expected: Cat Lovers

# Test case 6: All dogs
votes6 = "DDDD"
print(f"Test case 6: {votes6} -> {predictAdoption_victory(votes6)}")  # Expected: Dog Lovers

# Test case 7: Alternating, starts with dog
votes7 = "DCDCD"
print(f"Test case 7: {votes7} -> {predictAdoption_victory(votes7)}")  # Expected: Dog Lovers





# Problem 1: Blueprint Approval Process
# You are in charge of overseeing the blueprint approval process for various architectural designs. Each blueprint has a specific complexity level, represented by an integer. Due to the complex nature of the designs, the approval process follows a strict order:

# Blueprints with lower complexity should be reviewed first.
# If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
# Your task is to simulate the blueprint approval process using a queue. You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

# Return the order in which the blueprints are approved.

# def blueprint_approval(blueprints):
#     pass
# Example Usage:

# print(blueprint_approval([3, 5, 2, 1, 4])) 
# print(blueprint_approval([7, 4, 6, 2, 5])) 
# Example Output:

# [1, 2, 3, 4, 5]
# [2, 4, 5, 6, 7]


from collections import deque

def blueprint_approval(blueprints):
    queue = deque(blueprints)
    approved = []
    
    while queue:
        # Step 1: Manually find the smallest number in queue
        smallest = queue[0]
        for val in queue:
            if val < smallest:
                smallest = val
        
        # Step 2: Rotate queue until we find and remove the smallest
        size = len(queue)
        for _ in range(size):
            current = queue.popleft()
            if current == smallest:
                approved.append(current)  # Approve it!
                break
            else:
                queue.append(current)  # Rotate to the back

    return approved

print("------PROBLEM 1 TEST CASES------")

# Test case 1: Example from prompt
blueprints1 = [3, 5, 2, 1, 4]
print(f"Test case 1: {blueprints1} -> {blueprint_approval(blueprints1)}")  # Expected: [1, 2, 3, 4, 5]

# Test case 2: Example from prompt
blueprints2 = [7, 4, 6, 2, 5]
print(f"Test case 2: {blueprints2} -> {blueprint_approval(blueprints2)}")  # Expected: [2, 4, 5, 6, 7]

# Test case 3: Already sorted
blueprints3 = [1, 2, 3, 4, 5]
print(f"Test case 3: {blueprints3} -> {blueprint_approval(blueprints3)}")  # Expected: [1, 2, 3, 4, 5]

# Test case 4: Reverse order
blueprints4 = [5, 4, 3, 2, 1]
print(f"Test case 4: {blueprints4} -> {blueprint_approval(blueprints4)}")  # Expected: [1, 2, 3, 4, 5]

# Test case 5: Single blueprint
blueprints5 = [42]
print(f"Test case 5: {blueprints5} -> {blueprint_approval(blueprints5)}")  # Expected: [42]

# Test case 6: Empty list
blueprints6 = []
print(f"Test case 6: {blueprints6} -> {blueprint_approval(blueprints6)}")  # Expected: []

# Test case 7: Duplicates (should handle if allowed)
blueprints7 = [2, 3, 2, 1]
print(f"Test case 7: {blueprints7} -> {blueprint_approval(blueprints7)}")  # Expected: [1, 2, 2, 3]


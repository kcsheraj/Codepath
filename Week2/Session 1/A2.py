# Problem 1: The Library of Alexandria
# In the ancient Library of Alexandria, a temporal rift has scattered several important scrolls
#  across different rooms. You are given a dictionary library_catalog that maps room names to
#  the number of scrolls that room should have and a second dictionary actual_distribution that
#  maps room names to the number of scrolls found in that room after the temporal rift.

# Write a function analyze_library() that determines if any room has more or fewer scrolls than
#  it should. The function should return a dictionary where the keys are the room names and the
#  values are the differences in the number of scrolls (actual number of scrolls - expected number
#  of scrolls). You must loop over the dictionaries to compute the differences.

# def analyze_library(library_catalog, actual_distribution):
#     pass
# Example Usage:

# library_catalog = {
#     "Room A": 150,
#     "Room B": 200,
#     "Room C": 250,
#     "Room D": 300
# }

# actual_distribution = {
#     "Room A": 150,
#     "Room B": 190,
#     "Room C": 260,
#     "Room D": 300
# }


# print(analyze_library(library_catalog, actual_distribution))
# Example Output:

# {'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}


def analyze_library(library_catalog, actual_distribution):
    ans = {}

    for key in library_catalog:

        diff = actual_distribution[key] - library_catalog[key]

        ans[key] = diff

    return ans

# Test cases for analyze_library
library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}

print("Test case 1:")
print(analyze_library(library_catalog, actual_distribution))  # Expected: {'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}

# Additional test case: all rooms have correct scrolls
library_catalog2 = {
    "Room X": 100,
    "Room Y": 200
}
actual_distribution2 = {
    "Room X": 100,
    "Room Y": 200
}
print("Test case 2:")
print(analyze_library(library_catalog2, actual_distribution2))  # Expected: {'Room X': 0, 'Room Y': 0}

# Additional test case: all rooms have more scrolls
library_catalog3 = {
    "Room Z": 50,
    "Room W": 75
}
actual_distribution3 = {
    "Room Z": 60,
    "Room W": 80
}
print("Test case 3:")
print(analyze_library(library_catalog3, actual_distribution3))  # Expected: {'Room Z': 10, 'Room W': 5}



# Problem 2: Grecian Artifacts
# You've spent your last few trips exploring different periods of Ancient Greece. During your travels, you discover several interesting artifacts. Some artifacts appear in multiple time periods, while others in just one.

# You are given two lists of strings artifacts1 and artifacts2 representing the artifacts found in two different time periods. Write a function find_common_artifacts() that returns a list of artifacts common to both time periods.

# def find_common_artifacts(artifacts1, artifacts2):
#     pass
# Example Usage:

# artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
# artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

# print(find_common_artifacts(artifacts1, artifacts2))
# Example Output:

#  ["Golden Vase", "Bronze Shield"]

print("-----PROBLEM 2------")
def find_common_artifacts(artifacts1, artifacts2):
    myMap = {}
    ans = []

    for artifact in artifacts1:
        myMap[artifact] = artifact
    
    for artifact in artifacts2:
        if artifact in myMap:
            ans.append(artifact)


    return ans



# Test Case 1: Basic Case with Common Artifacts
artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]
print(find_common_artifacts(artifacts1, artifacts2))  # ["Golden Vase", "Bronze Shield"]

# Test Case 2: No Common Artifacts
artifacts1 = ["Marble Helmet", "Ivory Comb"]
artifacts2 = ["Clay Bowl", "Iron Spear"]
print(find_common_artifacts(artifacts1, artifacts2))  # []

# Test Case 3: All Artifacts Are Common
artifacts1 = ["Mask", "Scroll", "Lyre"]
artifacts2 = ["Mask", "Scroll", "Lyre"]
print(find_common_artifacts(artifacts1, artifacts2))  # ["Mask", "Scroll", "Lyre"]

# Test Case 4: Case Sensitivity Check
artifacts1 = ["Bronze Shield"]
artifacts2 = ["bronze shield"]
print(find_common_artifacts(artifacts1, artifacts2))  # []

# Test Case 5: One List is Empty
artifacts1 = []
artifacts2 = ["Sword", "Helmet"]
print(find_common_artifacts(artifacts1, artifacts2))  # []

# Test Case 6: Both Lists Are Empty
artifacts1 = []
artifacts2 = []
print(find_common_artifacts(artifacts1, artifacts2))  # []

# Test Case 7: Duplicates in Input Lists
artifacts1 = ["Coin", "Coin", "Amphora"]
artifacts2 = ["Amphora", "Amphora", "Coin"]
print(find_common_artifacts(artifacts1, artifacts2))  # ["Amphora", "Amphora", "Coin"]



# Problem 3: Souvenir Declutter
# As a time traveler, you've collected a mountain of souvenirs over the course of your travels. You're running out of room to store them all and need to declutter. Given a list of strings souvenirs and a integer threshold, declutter your souvenirs by writing a function declutter() that returns a list of souvenirs strictly below threshold.

# def declutter(souvenirs, threshold):
#     pass
# Example Usage:

# souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
# threshold1 = 3

# souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
# threshold = 2
# Example Output:

# ["alien egg", "map", "map", "statue"]
# ["sword"]


def declutter(souvenirs, threshold):
    hashMap = {}
    ans = []

    for string in souvenirs:
        if string in hashMap:
            hashMap[string] += 1
        else:
            hashMap[string] = 1
    
    for string in souvenirs:
        
        occurance = hashMap[string]

        if occurance < threshold:
            ans.append(string)
        


    return ans


print("-----PROBLEM 3------")

# Test Case 1: Standard case with duplicates and some below threshold
souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3
print(declutter(souvenirs1, threshold1))
# Expected: ['alien egg', 'map', 'map', 'statue']

# Test Case 2: Only one souvenir meets the condition
souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2
print(declutter(souvenirs2, threshold2))
# Expected: ['sword']

# Test Case 3: No souvenirs below threshold
souvenirs3 = ["badge", "badge", "badge"]
threshold3 = 1
print(declutter(souvenirs3, threshold3))
# Expected: []

# Test Case 4: All souvenirs below threshold
souvenirs4 = ["ticket", "map", "coin"]
threshold4 = 2
print(declutter(souvenirs4, threshold4))
# Expected: ['ticket', 'map', 'coin']

# Test Case 5: Mixed duplicates and singles
souvenirs5 = ["pin", "pin", "pin", "photo", "photo", "cup"]
threshold5 = 3
print(declutter(souvenirs5, threshold5))
# Expected: ['photo', 'photo', 'cup']

# Test Case 6: Case sensitivity
souvenirs6 = ["Coin", "coin", "Coin"]
threshold6 = 2
print(declutter(souvenirs6, threshold6))
# Expected: ['coin'] — 'Coin' appears twice, 'coin' appears once

# Test Case 7: Empty list
souvenirs7 = []
threshold7 = 3
print(declutter(souvenirs7, threshold7))
# Expected: []

# Test Case 8: Threshold is zero
souvenirs8 = ["ring", "ring", "ring"]
threshold8 = 0
print(declutter(souvenirs8, threshold8))
# Expected: [] — nothing can be < 0

# Test Case 9: Threshold is high enough to include all
souvenirs9 = ["key", "key", "tag"]
threshold9 = 5
print(declutter(souvenirs9, threshold9))
# Expected: ['key', 'key', 'tag']

# Test Case 10: Non-contiguous qualifying items
souvenirs10 = ["badge", "coin", "badge", "coin", "badge", "poster"]
threshold10 = 3
print(declutter(souvenirs10, threshold10))
# Expected: ['coin', 'coin', 'poster']


# Problem 4: Time Portals
# In your time travel adventures, you are given an array of digit strings portals and a digit string destination. Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.

# Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.

# def num_of_time_portals(portals, destination):
#     pass
# Example Usage:

# portals1 = ["777", "7", "77", "77"]
# destination1 = "7777"
# portals2 = ["123", "4", "12", "34"]
# destination2 = "1234"
# portals3 = ["1", "1", "1"]
# destination3 = "11"

# print(num_of_time_portals(portals1, destination1))
# print(num_of_time_portals(portals2, destination2))
# print(num_of_time_portals(portals3, destination3))
# Example Output:

# 4
# 2
# 6
# Problem 1: Words Containing Character
# Write a function words_with_char() that accepts a list of strings words and a character x. Return a list of indices representing the words that contain the character x. The returned list may be in any order.

# def words_with_char(words, x):
# 	pass
# Example Usage:

# words = ["batman", "superman"]
# x = "a"
# words_with_char(words, x)

# words = ["black panther", "hulk", "black widow", "thor"]
# x = "a"
# words_with_char(words, x)

# words = ["star-lord", "gamora", "groot", "rocket"]
# x = "z"
# words_with_char(words, x)
# Example Output:

# [0, 1]
# [0, 2]
# []

def words_with_char(words, x):
    
    char = x
    answerlist = []
    for i in range(len(words)):
        nextword = words[i]
        if char in nextword:
            answerlist.append(i)

    return answerlist


print("---------------PROBLEM 1---------------")
words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))  # Output: [0, 1]

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))  # Output: [0, 2]

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))  # Output: []




# Problem 2: HulkSmash
# Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:

# answer[i] == "HulkSmash" if i is divisible by 3 and 5.
# answer[i] == "Hulk" if i is divisible by 3.
# answer[i] == "Smash" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
# def hulk_smash(n):
# 	pass
# Example Usage:

# n = 3
# hulk_smash(n)

# n = 5
# hulk_smash(n)

# n = 15
# hulk_smash(n)
# Example Output:

# ["1", "2", "Hulk"]
# ["1", "2", "Hulk", "4", "Smash"]
# ["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]

def hulk_smash(n):

    ansArr = [0] * n

    for i in range(n):
        index = i + 1

        if index % 3 == 0 and index % 5 == 0:
            ansArr[i] = "HulkSmash"
        elif index % 3 == 0:
            ansArr[i] = "Hulk"
        elif index % 5 == 0:
            ansArr[i] = "Smash"
        else:
            ansArr[i] = str(index)
    
    return ansArr

print("---------------PROBLEM 2---------------")

n = 3
print(f"Test case n = {n}: {hulk_smash(n)}")  # Expected: ["1", "2", "Hulk"]

n = 5
print(f"Test case n = {n}: {hulk_smash(n)}")  # Expected: ["1", "2", "Hulk", "4", "Smash"]

n = 15
print(f"Test case n = {n}: {hulk_smash(n)}")  # Expected: ["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]




# Problem 3: Encode
# The Riddler is planning to leave a coded message to lead Batman into a trap. Write a function shuffle() that takes in a string, the Riddler's message, and encodes it using an integer array indices. The message will be shuffled such that the character at the ith position in message moves to index indices[i] in the shuffled string. You may assume len(message) is equal to the len(indices).

# def shuffle(message, indices):
# 	pass
# Example Usage:

# message = "evil"
# indices = [3, 1, 2, 0]
# shuffle(message, indices)

# message = "findme"
# indices = [0, 1, 2, 3, 4, 5]
# shuffle(message, indices)
# Example Output:

# "lvie"
# "findme"

# character at the ith position in message moves to index indices[i] in the shuffled string.

def shuffle(message, indices):
    result = [''] * len(message)  # create a list of the same length
    for i in range(len(message)):
        result[indices[i]] = message[i]
    return ''.join(result)

print("---------------PROBLEM 3---------------")

message = "evil"
indices = [3, 1, 2, 0]
print(f"Test case message = '{message}', indices = {indices}: {shuffle(message, indices)}")  # Expected: "lvie"

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(f"Test case message = '{message}', indices = {indices}: {shuffle(message, indices)}")  # Expected: "findme"

message = "batman"
indices = [5, 4, 3, 2, 1, 0]
print(f"Test case message = '{message}', indices = {indices}: {shuffle(message, indices)}")  # Expected: "namtab"

message = "superman"
indices = [7, 6, 5, 4, 3, 2, 1, 0]
print(f"Test case message = '{message}', indices = {indices}: {shuffle(message, indices)}")  # Expected: "namrepus"


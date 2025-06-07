# Problem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.

# def linear_search(lst, target):
#   pass
# Example Usage:

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
# linear_search(items, target)

# items = ['bed', 'blue jacket', 'red shirt', 'hunny']
# target = 'red balloon'
# linear_search(items, target)
# Example Output:

# 3
# -1


def linear_search(lst, target):

  for i in range(len(lst)):
    element = lst[i]

    if element == target:
      return i

  return -1


print("------PROBLEM 1-------")
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))  # ➝ 3

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))  # ➝ -1

# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

# def final_value_after_operations(operations):
#   pass
# Example Usage:

# operations = ["trouncy", "flouncy", "flouncy"]
# final_value_after_operations(operations)

# operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)
# Example Output:

# 2
# 4


def final_value_after_operations(operations):

  tigger = 1

  for op in operations:
    if op == 'bouncy' or op == 'flouncy':
      tigger += 1
    else:
      tigger -= 1

  return tigger


# Test cases for final_value_after_operations()
print("------PROBLEM 2-------")
print(final_value_after_operations(["bouncy", "flouncy", "trouncy",
                                    "pouncy"]))  # Expected: 1
print(final_value_after_operations(["bouncy", "bouncy",
                                    "flouncy"]))  # Expected: 4
print(final_value_after_operations(["trouncy", "pouncy",
                                    "pouncy"]))  # Expected: -2
print(final_value_after_operations([]))  # Expected: 1
print(
    final_value_after_operations(
        ["flouncy", "flouncy", "flouncy", "flouncy",
         "flouncy"]))  # Expected: 6
print(final_value_after_operations(["bouncy", "bouncy",
                                    "bouncy"]))  # Expected: 4
print(
    final_value_after_operations(["trouncy", "trouncy", "trouncy",
                                  "trouncy"]))  # Expected: -3

# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

# def tiggerfy(word):
#   pass
# Example Usage:

# word = "Trigger"
# tiggerfy(word)

# word = "eggplant"
# tiggerfy(word)

# word = "Choir"
# tiggerfy(word)
# Example Output:

# "r"
# "eplan"
# "Chor"

# t, i, gg, and er


def tiggerfy(word):
  newWord = ""
  i = 0
  while i < len(word):
    if word[i].lower() == 't' or word[i].lower() == 'i':
      i += 1
      continue

    if i < len(word) - 1:
      pair = word[i:i + 2].lower()
      if pair == "gg" or pair == "er":
        i += 2
        continue

    newWord += word[i]
    i += 1

  return newWord


print("------PROBLEM 3-------")
print(tiggerfy("Trigger"))  # ➝ "r"
print(tiggerfy("eggplant"))  # ➝ "eplan"
print(tiggerfy("Choir"))  # ➝ "Chor"
print(tiggerfy("TiGgEr"))  # ➝ ""
print(tiggerfy("git"))  # ➝ "g"
print(tiggerfy("Rugged terrain"))  # ➝ "Rued ran"

# Problem 4: Non-decreasing Array
# Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# def non_decreasing(nums):
#   pass
# Example Usage:

# nums = [4, 2, 3]
# non_decreasing(nums)

# nums = [4, 2, 1]
# non_decreasing(nums)
# Example Output:

# True
# False


def non_decreasing(nums):

  fix = 1

  for i in range(len(nums) - 1):
    num = nums[i]

    if nums[i + 1] < num:
      if fix < 1:
        return False
      else:
        fix -= 1

  return True


# Test cases
print("------PROBLEM 4-------")
print(non_decreasing([4, 2, 3]))  # True — can fix by changing 4 to 2
print(non_decreasing([4, 2, 1]))  # False — needs more than one fix
print(non_decreasing([1, 2, 3, 4, 5]))  # True — already non-decreasing
print(non_decreasing([3, 4, 2, 5]))  # True — fix 4 to 2 or 2 to 4
print(non_decreasing([5, 7, 1, 8]))  # True — fix 7 to 1
print(non_decreasing([5, 4, 3, 2]))  # False — multiple changes needed
print(non_decreasing([1, 3, 2, 1]))  # False — two drops
print(non_decreasing([1]))  # True — single element
print(non_decreasing([]))  # True — empty array
print(non_decreasing([1, 2, 5, 3]))  # True — fix 5 to 3

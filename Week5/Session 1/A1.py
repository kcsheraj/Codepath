# Problem 1: Player Class II
# A class constructor is a special method or function that is used to create and initialize a new object from a class. Define the class constructor __init__() for a new class Player that represents Mario Kart players. The constructor accepts two required arguments: strings character and kart. The constructor should define three properties for a Player:

# character, a string initialized to the argument character
# kart, a string initialized to the argument kart
# items, a list initialized to an empty list
# class Player:
#     def __init__(self, character, kart):
#         pass
# Example Usage:

# player_one = Player("Yoshi", "Super Blooper")
# print(player_one.character)
# print(player_one.kart) 
# print(player_one.items)
# Example Output:

# Yoshi
# Super Blooper
# []


# class Player:
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []



# Problem 2: Add Special Item
# Players can pick up special items as they race.

# Update the Player class with a new method add_item() that takes in one parameter, item_name.

# The method should validate the item_name.

# If the item is valid, add item_name to the player’s items attribute.
# The method does not need to return any values.
# item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".

# class Player:
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
        
#     def add_item(self, item_name):
#         pass
# Example Usage:

# player_one = Player("Yoshi", "Dolphin Dasher")
# print(player_one.items)

# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)
# Example Output:

# []
# ['red shell']
# ['red shell', 'super star']
# ['red shell', 'super star']



class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def add_item(self, item_name):
        valid_items = {
            "banana", "green shell", "red shell", "bob-omb",
            "super star", "lightning", "bullet bill"
        }
        if item_name in valid_items:
            self.items.append(item_name)



# Problem 3: Race Results
# Given a list race_results of Player objects where the first player in the list came first in the race, the second player in the list came second, etc., write a function print_results() that prints the players in place.

# class Player:
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
#     # ... methods from previous problems

# def print_results(race_results):
#     pass
# Example Usage:

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M")
# luigi = Player("Luigi", "Super Blooper")
# race_one = [peach, mario, luigi]

# print_results(race_one)
# Example Output:

# 1. Peach
# 2. Mario
# 3. Luigi


class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    # ... methods from previous problems

def print_results(race_results):
    for i, person in enumerate(race_results, 1):
        print(f"{i}. {person.character}")



# Problem 4: Get Rank
# The Player class has been updated below with a new attribute ahead to represent the player currently directly ahead of them in the race.

# Write a function get_place() that accepts a Player object my_player and returns their current place number in the race.

# class Player:
#     def __init__(self, character, kart, opponent=None):
#         self.character = character
#         self.kart = kart
#         self.items = []
#         self.ahead = opponent

# def get_place(my_player):
#     pass
# Example Usage:

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M", peach)
# luigi = Player("Luigi", "Super Blooper", mario)

# player1_rank = get_place(luigi)
# player2_rank = get_place(peach)
# player3_rank = get_place(mario)

# print(player1_rank)
# print(player2_rank)
# print(player3_rank)
# Example Output:

# 3
# 1
# 2

class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent


    def get_place(self):
        place = 1
        temp = self
        while temp.ahead:
            place += 1
            temp = temp.ahead

        return place

print("-------Problem 4--------")
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

print(luigi.get_place()) # 3
print(peach.get_place())  # 1
print(mario.get_place())  # 2

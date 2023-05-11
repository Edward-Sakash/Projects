
import random

def generate_stats(char_class):
    """
    Generates random stats for a character based on their class.
    """
    health = random.randint(3, 15)
    strength = random.randint(3, 15)
    magic = random.randint(3, 15)
    initiative = random.randint(3, 15)
    
    if char_class == "Barbarian":
        health *= 3
        strength *= 3
    elif char_class == "Cleric":
        magic *= 3
        initiative *= 3
    elif char_class == "Druid":
        health *= 2
        magic *= 2
        initiative *= 2
    
    return {"Health": health, "Strength": strength, "Magic": magic, "Initiative": initiative}

def create_characters(num_chars):
    """
    Prompts the user for character names and generates a list of characters with random stats.
    """
    characters = []
    
    for i in range(num_chars):
        name = input(f"Enter a name for character {i+1}: ")
        char_class = random.choice(["Barbarian", "Cleric", "Druid"])
        stats = generate_stats(char_class)
        
        characters.append({"Name": name, "Class": char_class, **stats})
    
    return characters

def print_team(characters):
    """
    Prints the list of characters with their stats in a formatted way.
    """
    print("Team:")
    print("---------")
    for char in characters:
        print(f"{char['Name']} the {char['Class']}")
        for stat, value in char.items():
            if stat != "Name" and stat != "Class":
                print(f"  {stat}: {value}")
        print()
    print("---------")

# Prompt the user for the number of characters to create
num_chars = int(input("How many characters do you want to create? "))

# Generate the list of characters and print the team
characters = create_characters(num_chars)
print_team(characters)
print("Happy advertising!")
"""
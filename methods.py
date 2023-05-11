my_text = "this is a TEST"

changed = my_text.upper()

print(my_text.upper())
print(my_text.capitalize())
print(my_text.lower())
print(my_text.isalpha()) # alpha = part of the alphabet
print(my_text.isalnum())
print(my_text.split())
print(my_text.split("T"))

long_text = """
It was a dark and stormy night
Ya ya, ding dong
The end.
"""

print(long_text.split("\n"))


print("A nice kitten".replace("kitten", "dragon"))

desc = "A mage conjured an image of a dragon"
print(desc.replace("mage", "wizard"))

text = "Joel \"Req\" Peltonen" 

text = "Rauli\n\tStr: 3\n\tHP: 7"
print(text)






print("------------------------")

len("caramel ice")
print(len("caramel ice"))
print(len(["water", "snow", "ice"]))
#print(len(1234567)) can't do len for numbers

drinks = ["Coffee", "Tea", "Water"]
print(drinks[0])

drinks.append("Juice") # add "Juice" in list "drinks"
print(drinks)







# Yvonne Aime
# COP 2500
# July 19, 2023

# Strings

name = "Kyle Steven DenCker"
print(name)

# Make the name all lowercase
lower_name = name.lower()
print(name, "-", lower_name)

# Makes the name all uppercase
upper_name = name.upper()
print(name, "-", upper_name)

# Capitalize
capital = name.capitalize()
print(name, "-", capital)
title_name = name.title()
print(name, "-", title_name)
guess=input("Guess my name")
if (name.lower() == guess.lower()):
    print("You got it, dude")
else:
    print("Cut it out")
if (guess.lower() == "key"):
    print("You got the hidden word")

# Lets get the length of a string
length = len(name)
print(length)

# Making substrings
print(name[3])
# the beginning to 3. (or whatever number is there.
print(name[:3])
# Start at 3 to the end.
print(name[3:])
# start at the 7th to the right
print(name[-7:])
print(name[5:11])
badpeople = name.replace("V", "ph")
print(badpeople)
x = "Super Van Evil guy"
hidden_bad_people = x.upper().replace("V", "ph")
print(x, hidden_bad_people)

# Here is the time we will combine lists and strings
list_of_names = name.split()
print(list_of_names)
list_split_by_e = name.split("e")
print(list_split_by_e)
list_of_names = name.lower().split()
if guess.lower() in list_of_names:
    print("You found a name")
else:
    print("You didn't")
hotdog = " Chicago DOGZ are THE best Hotdogzzz "
print("**"+hotdog+"**")
print("**"+hotdog.strip()+"**")
hotdog_words = hotdog.split()
print(hotdog_words)
new_hotdog = ""
for index in range(len(hotdog_words)):
    new_hotdog += hotdog_words[index] + " "
print(new_hotdog)
print("**"+new_hotdog+"**")
print("**"+new_hotdog[:-1]+"**")
print("**"+new_hotdog.strip()+"**")

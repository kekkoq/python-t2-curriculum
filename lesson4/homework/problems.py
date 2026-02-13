# Problem 1
# Ask the user for a sentence.
# Use a dictionary to count how many times each word appears.
# Print the dictionary.
# (Hint: split the sentence)
sentence = "I ate a sandwich for lunch."

words = sentence.split()   
word_count = {}            

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

print(word_count)


# Problem 2
# Create a dictionary called capitals with states and their capitals.
# Ask the user for a state and print the capital.
# If not found, print "No data".
capitals = {
    "Washington": "Olympia",
    "Alabama": "Montgomery",
    "Arizona": "Phoenix"
}
print(capitals["Washington"])

# Problem 3
# Ask the user for a word.
# Print the letter that appears the most times.
# If there is a tie, print any one of them.
word = "Telephone"
letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

most_common = max(letter_count, key=letter_count.get)
print(most_common)

# Problem 4
# Create a dictionary called inventory with items and their quantity.
# Ask the user what item they want to buy and how many.
# If there are enough, subtract from the inventory and print the new inventory.
# Otherwise print "Not enough".
inventory = {
    "apple": "10",
    "banana": "5",
    "orange": "2"
}
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 2
}
item = input("What item do you want to buy? ")
amount = int(input("How many do you want? "))

if item in inventory and inventory[item] >= amount:
    inventory[item] -= amount
    print(inventory)
else:
    print("Not enough")

# Problem 5
# Ask the user for two words.
# Use dictionaries to check if they are anagrams (same letters, different order).
# Print "Anagram" or "Not anagram".
word2 = "cup"
word3 = "pin"
def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

if count_letters(word2) == count_letters(word3):
    print("They are anagrams!")
else:
    print("Not anagrams.")

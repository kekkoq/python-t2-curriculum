# Problem 1
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).
word = "fish"
vowels = "aeiou"
counter = 0
for character in word:
    if character in vowels:
        counter = counter + 1
print("Vowel count:", counter)

# Problem 2
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".
test = "washington"
backwards = test[::-1]
if test == backwards:
    print("The word is a palindrome")
else:
    print("The word isn't a palindrome")


# Problem 3
# Ask the user for a word.
# Build a new string that contains ONLY the letters at odd indexes (1, 3, 5, ...).
word2 = "keyboard"
new_word = ""
for i in range(len(word2)):
    if i % 2 == 0:
        new_word = new_word + word2[i]
print(new_word)


# Problem 4
# Ask the user for two words.
# Print the two words combined with a dash in the middle. Example: "cat-dog".
word3 = "mushroom"
word4 = "glass"
print(word3, "-", word4)

# Problem 5
# Ask the user for a phrase.
# Build a new string that removes all spaces.
phrase = "GET OUT OF MY HOUSE"
new_word = ""

for i in range(len(phrase)):
    if phrase[i] != " ":
        new_word = new_word + phrase[i]
print(new_word)
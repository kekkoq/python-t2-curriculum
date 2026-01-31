# Problem 1
# Ask the user for a sentence.
# Print how many words it has.
# (Hint: split the sentence by spaces)
sentence = "I eat pizza."
spaces = sentence.count(" ")
extra_space_count = spaces + 1

print(extra_space_count)


# Problem 2
# Ask the user for a word.
# Build a new string that turns every vowel into "*".
# Example: "hello" -> "h*ll*"
word = "Special"
vowels = "aeiou"
new_word = ""
for character in word:
    if character.lower() in vowels:
        new_word += "*"
    else:
        new_word += character
print(new_word)


# Problem 3
# Ask the user for a word.
# Print the first index where the letter "a" appears.
# If there is no "a", print -1.
word2 = "Teeth"
try:
    print(word2.index("a"))
except ValueError:
    print("-1")


# Problem 4
# Ask the user for two words.
# Print the longer word. If they are the same length, print "Tie".
word3 = "Foul"
word4 = "Trait"
if len(word3) > len(word4):
    print(word3)
elif len(word4) > len(word3):
    print(word4)
else:
    print("Tie")

# Problem 5
# Ask the user for a phrase.
# Build a new string that keeps only letters (remove spaces and punctuation).
# For this problem, remove commas and periods too.
phrase = "Raining cats and dogs!"
new_phrase = ""

for char in phrase:
    if char.isalpha():
        new_phrase += char

print(new_phrase)

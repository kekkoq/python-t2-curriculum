# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
word = "chicken"
print(word[::-1])

# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive).
secondword = "apple"
letter = "v"
print(secondword.count(letter))


# Problem 3
# Ask the user for an email address like "name@example.com".
# Print only the part after the @ (example: "example.com").
email = "joe@coolwebsite.com"
print(email[4:19])

# Problem 4
# Ask the user for a word.
# Print the word without the first and last character.
thirdword = "taco"
print(thirdword[1:-1])

# Problem 5
# Ask the user for a sentence.
# Print "Long" if the sentence has more than 20 characters (including spaces),
# otherwise print "Short".
sentence = "I ate toast and some orange juice for breakfast."
if len(sentence)>20:
    print("Long")
else:
    print("Short")





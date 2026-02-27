# Problem 1
# Create a tuple called scores with 4 numbers.
# Print the average score.
scores = (1, 3, 2, 6)
total = sum(scores) / len(scores)
print(total)


# Problem 2
# Create a list of tuples representing students:
# ("Ava", 95), ("Ben", 88), ("Kai", 73)
# Print the name of the student with the highest score.
ava = ("Ava", 95)
ben = ("Ben", 88)
kai = ("Kai", 73)

best = min(ava, ben, kai)
print(best[0])

# Problem 3
# Ask the user for a sentence.
# Split it into words.
# Create a list of tuples where each tuple is (word, length_of_word).
# Print the list.
sentence = ("My name is kaiden.")
split = ["My", "name", "is", "kaiden"]
print("My has", len(split[0]), "letters.")
print("name has", len(split[1]), "letters.")
print("is has", len(split[2]), "letters.")
print("kaiden has", len(split[3]), "letters.")

# Problem 4
# Create a function called first_and_last(word).
# It should return a tuple containing the first and last letter of the word.
# Test it.
def first_and_last(word):
    first = word[0]
    last = word[-1]
    return (first, last)

result = first_and_last("Sushi")
print(result)

# Problem 5
# Tuples can be dictionary keys.
# Create a dictionary where the keys are points like (x, y) and the values are colors.
# Add at least 3 points and print the dictionary.
points = {
    (0, 0): "red",
    (1, 2): "blue",
    (3, 5): "green"
}

print(points)
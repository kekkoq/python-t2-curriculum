# Problem 1
# Create a dictionary called student with these keys:
# "name" -> your name
# "grade" -> your grade level
# Print the dictionary and then print only the name.
students = {
    "Kaiden": 6,
}
for name in students:
    print(name, "is in grade", students[name])


# Problem 2
# Create a dictionary called prices with:
# "apple" -> 2
# "banana" -> 1
# "orange" -> 3
# Ask the user for a fruit name and print its price.
# If the fruit is not in the dictionary, print "Not found".
prices = {
    "Apple": 2,
    "Banana": 1,
    "Orange": 3,
}
fruit_name = input("Please give me a fruit name: ")
if fruit_name in prices:
    print("$", prices[fruit_name])
else:
    print("Fruit not found.")

# Problem 3
# Ask the user for a word.
# Use a dictionary to count how many times each letter appears.
# Print the dictionary.



# Problem 4
# Create a dictionary called phonebook with names and phone numbers.
# Ask the user for a name and print the phone number if it exists.
# Otherwise print "Unknown contact".



# Problem 5
# Create a dictionary called scores with 3 students and their test scores.
# Print the name of the student with the highest score.

# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
n = 12
for i in range(0, n + 1, 3):
    print(i)


# Problem 2
# Ask the user for a number n.
# Print the square of every number from 1 to n (1*1, 2*2, ...).
n2 = 4

for i in range(n2):
    print(i ** 2)


# Problem 3
# Ask the user for a number n.
# Print the numbers from n down to 0 (counting down).
n3 = 5
for i in range(n3, -1, -1):
    print(i)

# Problem 4
# Ask the user for a word.
# Build a new string that repeats the word 5 times with spaces in between.
# Example: "hi hi hi hi hi"
word = "Gummy"
print((word + " ") * 5)



# Problem 5
# Ask the user for a number n.
# Print how many numbers from 1 to n are even.
n4 = 12
for i in range(0, n4, 2):
    print(i)
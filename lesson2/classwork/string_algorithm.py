word = "mississippi"
vowels = "aeiou"
counter = 0
for character in word:
    if character in vowels:
        counter = counter + 1
print("Vowel count:", counter)

test = "racecar"
backwards = test[::-1]
if test == backwards:
    print("The word is a palindrome")
else:
    print("The word isn't a palindrome")

word2 = "15pineapple343"
digits = "1234567890"
counter2 = 0
for character in word2:
    if character in digits:
        counter2 = counter2 + 1
print(counter2)

word3 = "orange"
counter3 = 0
for character in word3:
    if character == "o":
        counter3 = counter3 + 1
print(counter3)
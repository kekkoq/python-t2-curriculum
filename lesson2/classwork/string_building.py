name = "Kaiden"
result = ""
for character in name:
    result = result + character + "_"
print(result)

letters = ["a", "p", "p", "l", "e"]
built = "".join(letters)
print(built)


word = "computer"
new_word = ""
for i in range(len(word)):
    if i % 2 == 0:
        new_word = new_word + word[i]
print(new_word)

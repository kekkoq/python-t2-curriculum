word = "ballon"

freq = {}
for character in word:
    if character in freq:
        freq[character] = freq[character] + 1
    else:
        freq[character] = 1

print(freq)
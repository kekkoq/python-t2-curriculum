scores = {
    "Ava": 95,
    "Ben": 82,
    "Kai": 73,
}

for name in scores:
    print(name, "scored", scores[name])

print(list(scores.keys()))
print(list(scores.values()))
print(list(scores.items()))

for name, score in scores.items():
    if score >= 90:
        print(name, "got an A.")
    
for value in scores.values():
    print(value)

for key in scores.keys():
    print(key)

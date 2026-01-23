text = "  Hello World  "
print("Raw text:", text)

print(len(text))

print(text.lower())
print(text.upper())
print(text.title())

print(text.strip())
print(text.rstrip())
print(text.lstrip())

print(text.strip().lower())

message = "banana bread"
print(message.count("na"))
print(message.find("bread"))

print(message.replace("banana", "pumpkin"))

print(message.startswith("ba"))
if message.endswith("bread"):
    print("Message is a bread.")
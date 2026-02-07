person = {
    "name": "Alex",
    "age": 15,
    "city": "Seattle"
}
print(person)

print("Name:", person["name"])
print("Age:", person["age"])

person["favourite_food"] = "pizza"
print(person)

person["age"] = 16
print("New age: " + str(person["age"]))
person["age"] = person["age"] + 1
print("New age : ", person["age"])

print("age" in person)
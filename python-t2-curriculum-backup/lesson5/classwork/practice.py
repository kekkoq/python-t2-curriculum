# Problem 1
# Create a class called Cat.
# It should have an __init__ that takes name.
# It should have a method called meow() that prints "<name> says meow!".
# Create a Cat and call meow().
class Cat:
    def __init__(self, name):
        self.name = name
  
    def meow(self):
        print(self.name, "says meow!")

randy = Cat("randy")
randy.meow()

   


# Problem 2
# Create a class called Rectangle.
# __init__ should take width and height.
# Make a method area() that returns width * height.
# Create a Rectangle and print its area.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
rect = Rectangle(5, 10)
print(rect.area())

# Problem 3
# Create a class called Counter.
# It starts at value 0.
# Make a method add_one() that increases the value by 1.
# Call add_one() 5 times and print the final value.



# Problem 4
# Create a class called Player.
# __init__ takes name and health.
# Make a method take_damage(amount) that subtracts from health (no negatives).
# Create a Player and test take_damage().



# Problem 5
# Create a class called Book.
# __init__ takes title and pages.
# Make a method is_long() that prints "Long" if pages >= 300, else prints "Short".

class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 5

    def bark(self):
        print(self.name, "says woof!")

    def walk(self):
        if self.energy > 0:
            self.energy = self.energy - 1
            print(self.name, "went on a walk. Energy:", self.energy)
        else:
            print(self.name, "is too tired.")

buddy = Dog("buddy")
buddy.bark()
buddy.walk()
buddy.walk()
buddy.walk()
buddy.walk()
buddy.walk()
buddy.walk()
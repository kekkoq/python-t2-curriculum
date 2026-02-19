# Problem 1
# Create a class called BankAccount.
# __init__ takes owner and balance.
# Make a method deposit(amount) that adds to balance.
# Make a method withdraw(amount) that subtracts only if there is enough money.
# Test it with a few deposits and withdrawals.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

my_account = BankAccount("Kaiden", 50)
my_account.deposit(100)
my_account.withdraw(30)
my_account.withdraw(200)

# Problem 2
# Create a class called Car.
# __init__ takes model and miles.
# Make a method drive(distance) that adds to miles.
# Create a Car and drive it a few times, printing miles each time.
class Car:
    def __init__(self, model, miles):
        self.model = model
        self.miles = miles

    def drive(self, distance):
        self.miles += distance
        print(f"{self.model} has now driven {self.miles} miles.")

my_car = Car("Toyota", 0)

my_car.drive(10)
my_car.drive(25)
my_car.drive(5)


# Problem 3
# Create a class called ScoreKeeper.
# It stores a dictionary of player scores.
# Make a method add_points(name, points) that adds points for that player.
# Print the final dictionary after adding points for a few players.
class ScoreKeeper:
    def __init__(self):
        self.scores = {}

    def add_points(self, name, points):
        if name not in self.scores:
            self.scores[name] = 0
        self.scores[name] += points


game = ScoreKeeper()


game.add_points("Alice", 10)
game.add_points("Bob", 5)
game.add_points("Alice", 7)
print(game.scores)


# Problem 4
# Create a class called Timer.
# It starts at 0 seconds.
# Make a method tick() that adds 1.
# Make a method reset() that sets it back to 0.
# Test tick() and reset().
class Timer:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds += 1
        print(self.seconds)

    def reset(self):
        self.seconds = 0
        print(self.seconds)

# Test it
t = Timer()
t.tick()   # 1
t.tick()   # 2
t.tick()   # 3
t.reset()  # 0
t.tick()   # 1


# Problem 5
# Create a class called WordTracker.
# It stores a word (string).
# Make a method add_letter(letter) that adds the letter to the end.
# Make a method remove_last() that removes the last letter (if it exists).
# Test it.
class WordTracker:
    def __init__(self, word):
        self.word = word

    def add_letter(self, letter):
        self.word += letter
        print(self.word)

    def remove_last(self):
        if len(self.word) > 0:
            self.word = self.word[:-1]
        print(self.word)

w = WordTracker("hi")
w.add_letter("!")
w.add_letter("!")
w.remove_last()
w.remove_last()
w.remove_last()
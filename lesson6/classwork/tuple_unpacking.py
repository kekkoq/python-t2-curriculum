point = (8, 2)
x, y = point
print("x is", x)
print("y is", y)

a = 5
b = 9
a, b = b, a
print(a, b)

def min_and_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
        elif n < largest:
            smallest = n
    return smallest, largest

nums = [1, 2, 3, 4 ,5]
mn, mx = min_and_max(nums)
print("Min:", mn)
print("Max:", mx)
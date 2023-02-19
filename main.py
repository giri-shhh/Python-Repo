from math import *

# Simple
print("Hello World")
print(round(2, 3))
print(floor(34.4))
print(sqrt(9.4))
print(max(6.4, 3, 4))
print(min(3.4, 5.6))
print(min(8.4, 6.78, 6))

# Input
# name = input("Enter Name: \n")
# age = input("Enter Age: \n")
name = "Hello"
age = 12.345
print("Name: " + name)
print("age: " + str(float(age)))

# List
print("\n--------Lists---------\n")
friends = ["Test1", "Test2", "Test2", "Test1"]
luck = [1, 2, 3, 4, 5, 6]

friends.extend(luck)
print("Extends: " + str(friends))

friends.append("name")
print(friends)

print(friends.index("Test1"))

print(friends.count("Test1"))
luck.sort()
print("Sort" + str(luck))
print(luck.reverse())

print(friends[2])
print(friends[1:])
print(friends[1:3])
print(friends[-1])

print("Copy" + str(luck.copy()))

# Tuples

coordinates = [(4, 5, 3), (1, 34, 5453, 23, 23, 2, 3232)]

print(coordinates)
print(coordinates[0])


# Functions

def test(name, age, number):
    print("Test The Function: " + name + str(age) + str(number))


test("Hello All", 12, 100)


def sum(a, b):
    return a + b


sum = sum(1, 2)

print("Sum " + str(sum))

# If statements

is_male = True
is_tall = True

if is_male and is_tall:
    print("Male and Tall")
elif is_male and not (is_tall):
    print("Short Male")
else:
    print("Neither")

if 5 > 3:
    print("5 is BIGGGGGGGGGGGGGGG")


def max_num(num1, num2, num3):
    if num1 >= num2 and num2 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print("BIG NUmber : " + str(max_num(23, 45, 67)))

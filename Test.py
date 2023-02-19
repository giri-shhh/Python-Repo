# Dictionary
friend = {
    "Hello": "GHello",
    "Hello1": {
        "Test": ["testst", "hjahs"],
        "isIt": True,
        "Age": 20,
        "Salary": 1_22_234.00
    }
}

print(friend)

print(friend["Hello1"]["Test"])

i = 1

while i <= 10:
    print(i)
    i = i + 1
    i += 1

for i in [1, 2, 3, 4, 5]:
    print(i)

for letter in "Hello":
    print(letter)

for i in range(8, 10):
    print(i)

for i in range(0, len("Teet")):
    print(i)

for i in range(5):
    print(i)

print("Doneeeeeeeee\n")

print(2 ** 3)


try:
    val = 10/0
    print("Hello")
except ZeroDivisionError as err:
    print("Invalid" + str(err))

# For Loop
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

print()

for i in range(5):
    print("Hello World")

print()

for num in range(5, 10):
    print(num)

print()

for num in range(5, 100, 5):
    print(num)

print()

# step can be negative - just reverse order
for num in range(100, 20, -5):
    print(num)

# string splicing
phrase = "Tahiti, it's a magical place"
print(phrase[3])
print(phrase[3:6])
print(phrase[3:12:2])
print(phrase[::])  # copy the string
print(phrase[::-1])  # reverse the string

for char in phrase:
    print(char)

# len() returns the length of something
print("Number of characters in phrase:", len(phrase))
for index in range(0, len(phrase) - 1):
    print(phrase[index])

# While Loop
x = 1
while x < 5:
    print(x)
    x += 1

# infinite loop
# while x <= 5:
#     print(x)

# break vs continue
x = 1
while True:
    if x == 8:
        break

    x += 1
    print(x)

x = 1
while True:
    if x == 5:
        continue
    elif x == 20:
        break

    x += 1
    print(x)

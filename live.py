'''
print("Hello World")
print()
print("Hello", "Rebecca")

# string concatenation
print("Hello " + "Rebecca" + " I am a program")


This is
a
multi-line
compile


name = input("What is your name? ")
print(name)

print(5)
print(3.5)
print(True)
print(False)
'''

"""
This is also a 
multiline comment
"""

# age = int(input("What is your age? "))
# print(age + 5)
# str, bool, float

# arithmetic operators
# print(5 + 5) # addition
# print(5 - 5) # subtraction
# print(5 * 5) # mult
# print(12 / 5) # float division
# print(12 // 5) # floor division
# print(5 ** 2) # exponents
# print(10 % 3) # modulo

# DAYS_PER_WEEK = 7
# first_name = "Rebecca"

# PI = 3.14
# radius = float(input("Enter the radius of the circle: "))
# area = PI * radius * radius
# circumference = 2 * PI * radius
# print("Area:", area)
# print("Circumference:", circumference)

# logical operators
# is_raining = True
# have_netflix = False
# bored = False
# print(is_raining and have_netflix)  # False
# print(is_raining or bored)  # True
# print(not is_raining) # False

# relational operators
# print(5 < 10) # True
# print(10 > 20) # False
# print(10 >= 10) # True
# print(7 <= 12) # True
# print(5 == 5) # True
# print(5 != 5) # False

# is_raining = False
# have_netflix = True

# if is_raining:
#   print("Get an umbrella!")
# elif have_netflix:
#   print("Watch netflix")
# else:
#   print("No need for an umbrella")

# Grade
# score = float(input("Enter the student's score: "))
# if score >= 90:
#   print("A")
# elif score >= 80:
#   print("B")
# elif score >= 70:
#   print("C")
# elif score >= 60:
#   print("D")
# else:
#   print("F")

# Challenge - just reverse the order!
# if score < 60:
#   print("F")
# elif score < 70:
#   print("D")
# elif score < 80:
#   print("C")
# elif score < 90:
#   print("B")
# else:
#   print("A")

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# for i in range(5):
#   print("Hello World")

# for num in range(5):
#   print(num)

# range(start, stop, step)
# for num in range(3, 10):
#   print(num)

# for num in range(3, 10, 2):
#   print(num)

# for num in range(10, 2, -1):
#   print(num)

# string splicing
# phrase = "Good morning!"
# print(phrase[3]) # prints d
# # [start:stop:step]
# print(phrase[3:6]) # prints d m
# print(phrase[3:7:2]) # prints dm
# print(phrase[::]) # a copy of the string phrase
# print(phrase[::-1]) # a reversed string

# for char in phrase:
#   print(char)

# print("The length of phrase is", len(phrase))

# for index in range(0, len(phrase)):
#   print(phrase[index])

# while loops
# x = 1
# while x < 5:
#   print(x)
#   x += 1

# augmented assignment operators
# a = 5
# a += 1  # equivalent to a = a + 1
# -=, *=, /=, //=, %=, **=

# x = 5
# while True:
#   if x == 6:
#     x += 1
#     continue
#   elif x == 10:
#     break
#   else:
#     print(x)
#     x += 1

# lists
names = ["Finch", "Shaw", "Reese", "Carter"]
print(names)

print(names[3]) # carter
names[2] = "Root"
print(names)

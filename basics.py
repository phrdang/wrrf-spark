# Output
print("Hello World")  # programmer rite of passage
print("Hello " + "World")  # concatenation: mind the space
print('3.1415926 is pi')  # strings can basically have any character
print("Hello", "World")  # multiple arguments
print()  # print empty line

# Comments
# Add comments to increase your code's readability
# It's good programming style!
"""
Multi
line
comments!
"""

'''
Multi
line
comments!
'''

# Variables
my_name = "Rebecca Dang"
favorite_tv_show = "Agents of SHIELD"

print(my_name + " like " + favorite_tv_show)

# constants
DAYS_PER_WEEK = 7

# arithmetic operators
x = 5
x = x - 2
x = x * 3
x = x / 4  # "regular" division
x = x ** 5
x = x // 6  # floor division (NOT integer division, but similar)
x = x % 10  # modulus

# augmented assignment operators
x = 5
x -= 2
x *= 3
x /= 4
x **= 5
x //= 6
x %= 10

# Input
color = input("What's your favorite color? ")
print(color)

age = input("Enter your age: ")
print(age)
print(age + 5)  # oh no! concat!
print(int(age) + 5)  # recommend just converting right away to avoid errors
# explain diff data types: str, int, float, bool
# other conversion functions: str(), float(), bool()

# Boolean Logic
# relational operators
print(5 == 5)  # True
print(5 != 5)  # False
print(10 > 5)  # True
print(5 < 6.5)  # False
print(5 >= 5)  # True
print(23 <= 1)  # False

# logical operators
is_raining = True
have_netflix = False

print(is_raining and have_netflix)  # False
print(is_raining or have_netflix)  # True
print(not is_raining)  # False


# If Statements
# if
if is_raining:
    print("Stay inside")

# if else
if is_raining:
    print("Stay inside")
else:
    print("Go for a walk")

# if elif else
if is_raining and have_netflix:
    print("Binge watch a TV show")
elif is_raining:
    print("Stay inside")
else:
    print("Go for a walk")

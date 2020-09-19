def square(x):
    print(x * x)


def greet(name, greeting_type):
    if greeting_type == "SHIELD":
        print("I hear Tahiti's a magical place, " + name)
    elif greeting_type == "Star Wars":
        print("May the Force be with you, " + name)
    elif greeting_type == "Star Trek":
        print("Live long and prosper, " + name)
    elif greeting_type == "Person of Interest":
        print("We have another number, " + name)
    elif greeting_type == "Six of Crows":
        print("No mourners, no funerals, " + name)
    else:
        print("Hey there, " + name)


def echo(message, count):
    for i in range(count):
        print(message)


def pop_from_list(items):
    items.pop()
    return items


def main():
    square(5)
    greet("Rebecca", "Person of Interest")
    echo("Hello world", 5)

    # pass by reference vs pass by value
    # my_list = [1, 2, 3]
    # pop_from_list(my_list)
    # print(my_list)


# Calling functions
main()


# return and docstrings

# def square(x):
#     '''
#     Returns the square of the given number

#     Args:
#         x (float): a number to square

#     Returns:
#         float: x^2
#     '''
#     return x * x


# def main():
#     number = float(input("Enter a number to square: "))
#     result = square(number)
#     print("The square of " + str(number) + " + 5 = " + str(result + 5))

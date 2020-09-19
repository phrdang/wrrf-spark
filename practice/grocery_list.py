# Grocery List
# Continuously ask the user to enter items to add
# to a grocery list. When the user enters 'quit',
# stop asking for items and then print each item
# in a numbered format.
# For example, if the user enters 'eggs', 'bread',
# and 'apples', then the output would be:
# 1. eggs
# 2. bread
# 3. apples

groceries = []

while True:
    item = input("Enter a grocery item: ")
    if item == 'quit':
        break
    else:
        groceries.append(item)

for i in range(len(groceries)):
    print(str(i + 1) + ". " + groceries[i])

people = ["Finch", "Shaw", "Reese", "Carter", "Fusco"]

for person in people:
    print(person)

# List methods
# adds element to end of list
print("---Append---")
people.append("Root")
print(people)
print()

# inserts element at an index, shifts elements forward if needed
print("---Insert---")
people.insert(3, "Collier")
print(people)
print()

# Returns a copy of the list
print("---Copy---")
copy_of_people = people.copy()
print(copy_of_people)
print()

# Removes the element at an index
print("---Pop---")
removed_element = people.pop()  # default is the last item
print("Removed:", removed_element)
print(people)
removed_element = people.pop(2)
print("Removed:", removed_element)
print(people)
print()

# removes the first occurence of that element
print("---Remove---")
people.remove("Finch")
print(people)
print()

# returns first index of that element
print("---Index---")
print("Shaw is at index", people.index("Shaw"))
print()

# reverses the list IN PLACE
print("---Reverse---")
people.reverse()
print(people)
print()

# sorts the list IN PLACE
print("---Sort---")
people.sort()
print(people)
print()

# removes all elements in a list
print("---Clear---")
people.clear()
print(people)

print("Copy of people we made a while ago is still the same!")
print(copy_of_people)
print()

# List splicing - same as string splicing
print(copy_of_people[1:4])

# len() also works for lists
print("Number of elements in list:", len(copy_of_people))

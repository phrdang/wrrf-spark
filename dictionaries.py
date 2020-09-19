address_book = {
    "Coulson": "1234 Main St",
    "Daisy": "5678 Market Pl",
    "Fitz": "1357 Wall St",
    "Simmons": "2468 Park Pl",
}

print(address_book)
print()

# Retrieve
print("---Retrieve---")
print(address_book["Coulson"])
print()

# Add
print("---Add---")
address_book["May"] = "1632 Cavalry Ct"
print(address_book)
print()

# Update
print("---Update---")
address_book["Daisy"] = "4364 Astro Dr"
print(address_book)
print()


# Dictionary methods
# get
print("---Get---")
print(address_book.get("Simmons"))
# special because it can return a value if the key isn’t found
print(address_book.get("Mack", "No address found!"))
print()

# pop - remove entry at given key and return the value
print("---Pop---")
print(address_book.pop("Coulson"))
print(address_book)
print()

# popitem - removes entry that was last added to dict
print("---Popitem---")
address_book.popitem()
print(address_book)
print()

# copy - returns a copy of the dict
print("---Copy---")
copy = address_book.copy()
print(copy)
print()

# clear
print("---Clear---")
address_book.clear()
print(address_book)
print("Copy is still there:", copy)
print()


# Dictionary iteration
print("---Regular iteration (keys)---")
for name in copy:
    print(name)
print()

# keys
print("---Iterate through keys---")
for key in copy.keys():
    print(key)
print()

# values
print("---Iterate through values---")
for value in copy.values():
    print(value)
print()

# items
print("---Iterate through items (keys and values)---")
for key, value in copy.items():
    print(key + " lives at " + value)
print()

# len() also works for dictionaries
print("Length of copy of address book (# of entries):", len(copy))

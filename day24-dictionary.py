# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# gets the value inside the key mentioned
print(capitals.get("USA"))

# prints else block
if capitals.get("Japan"):
    print("This capital exists")
else:
    print("This capital does not exist")

# adds a key value pair to the dict
capitals.update({"Germany": "Berlin"})

# you can use update to modify a value using the key
capitals.update({"USA": "New York"})

# gets rid of china
capitals.pop("China")

# removes the latest keyvalue pair inserted (so here Germany)
capitals.popitem()

# capitals.clear()

print(capitals)

# stores all the keys in an array
keys = capitals.keys()

# for key in keys:
#     print(key)

# stores all the values in an array
values = capitals.values()

# for value in values:
#     print(value)

# returns an array of tuples
# ([('USA', 'New York'), ('India', 'New Delhi'), ('Russia', 'Moscow')])
items = capitals.items()

for key, value in capitals.items():
    print(f"{key} : {value:.2f}")

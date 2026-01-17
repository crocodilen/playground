# There are 4 collection data types in Python:
#   Lists
#   Sets
#   Tuples
#   Dictionaries

# Lists
list1 = ['cat', 'dog', 'bear']
list2 = list(('bear', 'bat', 'squirrel'))

list_union1 = list1 + list2
list_union2 = [*list1, *list2]

# Sets
set1 = {'One', 'Two', 'Three'}
set2 = set(("Three", "Four", "Five"))

set_union1 = set1 | set2
set_union2 = set1.union(set2)

# Tuples
tuple1 = ('blue', 'green', 'red')
tuple2 = tuple(('red', 'purple', 'black'))

tuple_union1 = tuple1 + tuple2
tuple_union2 = (*tuple1, *tuple2)

# Dicts
dict1 = {
    "name": "Bob",
    "age": 44,
    "children": ["Jane", "Doe"]
    }
dict2 = {
    "name": "Jane",
    "age": 45,
    "children": ["Bob", "Doe"]
    }
dict_union1 = dict1 | dict2
dict_union2 = {**dict1, **dict2}

print("\nLists")
print("list1:", list1)
print("list2:", list2)
print("list_union1:", list_union1)
print("list_union2:", list_union2)
print("\nSets")
print("set1:", set1)
print("set2:", set2)
print("set_union1:", set_union1)
print("set_union2:", set_union2)
print("\nTuples")
print("tuple1:", tuple1)
print("tuple2:", tuple2)
print("tuple_union1:", tuple_union1)
print("tuple_union2:", tuple_union2)
print("\nDictionaries")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict_union1:", dict_union1)
print("dict_union2:", dict_union2)

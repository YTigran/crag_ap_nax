my_dict = {
    'a': 10, 
    'b': 20, 
    'c': 10, 
    'd': 30, 
    'e': 20,
    'f': 20,
    'g': 20,
}

value_counts = {}

for value in my_dict.values():
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

print(value_counts)
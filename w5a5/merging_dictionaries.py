keys1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
values1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]

keys2 = ['u', 'b', 'o', 'x', 'e', 'a']
values2 = [200, 30, 10, 88, 55, 920]

def filter_odd(keys, values):
    return {k: v for k, v in zip(keys, values) if v % 2 != 0}

result1 = filter_odd(keys1, values1)
result2 = filter_odd(keys2, values2)
merged = {**result1, **result2}

print(result1)   # {'b': 3, 'c': 1, 'f': 55}
print(result2)   # {'e': 55}
print(merged)    # {'b': 3, 'c': 1, 'f': 55, 'e': 55}

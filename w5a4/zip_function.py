keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(f"Before adding 'd' to keys: {dictionary}")


# after adding "d" to keys
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(f"\nAfter adding 'd' to keys: {dictionary}")

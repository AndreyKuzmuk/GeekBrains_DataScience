print()
my_list = [5, 2.5, "str", False, {4, 6}, (8, 2)]
for i, item in enumerate(my_list, 1):
    print(f"item {item} - {type(item)}")

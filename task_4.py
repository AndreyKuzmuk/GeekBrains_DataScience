user_str = input("Type a few words here: ")

for i, word in enumerate(user_str, 1):
    print(f"{i} {word[:10]}")

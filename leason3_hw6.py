def int_func(a):
    return a[0].upper() + a[1:].lower()


int_func(input("Type 1 word here: "))

s = input("Type a few words with space here in lower register: ").split()
for i, a in enumerate(s):
    if not a.isascii() or not a.isalpha() or not a.islower():
        print("You need to type all words with space here in lower register!")
    else:
        s[i] = int_func(a)
print(" ".join(s))

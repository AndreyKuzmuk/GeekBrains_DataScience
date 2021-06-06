def my_func(x, y):
    if x <= 0 or y >= 0:
        print("X - need to be positive, and Y - need to be negative!")
    else:
        return pow(x, y)


try:
    print(my_func(int(input("Type X: ")), int(input("Type Y: "))))
except ValueError:
    print("You need to type numbers only!")

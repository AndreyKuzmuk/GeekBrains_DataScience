def my_func(a_1, a_2, a_3):
    return sum((a_1, a_2, a_3)) - min(a_1, a_2, a_3)


try:
    print(my_func(int(input("Please input first number: ")), int(input("Please input second number: ")),
              int(input("Please input third number: "))))
except ValueError:
    print("You need to type numbers only!")

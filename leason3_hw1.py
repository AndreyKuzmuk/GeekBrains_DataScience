def my_func(a_1, a_2):
    try:
        return int(a_1) / int(a_2)
    except ZeroDivisionError:
        print("You could not divide on zero!")
    except ValueError:
        print("Please, try type numbers")


a = my_func(input("Please input first number: "), input("Please input second number: "))
print(a)

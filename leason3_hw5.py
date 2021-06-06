def additional():
    a = 0
    while True:
        in_list = input("Enter numbers separated by a space or wright any letter to stop program: ").split()
        for i in in_list:
            try:
                a += int(i)
            except ValueError:
                print("You've stop program, by typing a number!")
                print("The final number is:")
                print()
        else:
            print(a)
            continue
        break
    return s


additional()

integer = int(input("Hello! Please, enter a positive integer: "))
biggestInt = integer % 10
while integer:
    lstNum = integer % 10
    if lstNum > biggestInt:
        biggestInt = a
        if biggestInt == 9:
            break
    integer = integer // 10

print("The Biggest integer is: ", biggestInt)

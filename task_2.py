the_list = input("Type 2 or more numbers with space - ").split()

for i in range(1, len(the_list), 2):
    the_list[i - 1], the_list[i] = the_list[i], the_list[i - 1]

print(the_list)

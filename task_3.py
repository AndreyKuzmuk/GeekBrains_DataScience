while True:
    month = int(input("Type number of month: "))
    number_of_season = month // 3
    if 0 < int(month) <= 12:
        seasons_list = ["Winter", "Spring", "Summer", "Autumn", "Winter"]
        seasons_dict = {0: "Winter", 1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
        print(f"In list this is {seasons_list[number_of_season]}")
        print(f"in dict this is {seasons_dict[number_of_season]}")
        break
    else:
        print("Wrong number of the month! Try from 1 to 12")

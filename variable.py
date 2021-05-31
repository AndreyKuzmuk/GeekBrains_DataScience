workingHrs = int(input("How many hours do you work per day? "))
normalHrs = 9
if workingHrs > normalHrs:
    print(f"This is too much! You need to work {normalHrs} hours per day!")
elif workingHrs == normalHrs:
    print("Good job! That's normal for you!")
else:
    print(f"This is not enough! You need to work {normalHrs} hours per day!")

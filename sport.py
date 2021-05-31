firstResult = int(input("Type, how many kilometers you run today: "))
result = int(input("Type, how many kilometers you want to run? "))
days = 1
while result > firstResult:
    firstResult = firstResult * 1.1
    days = days + 1
print(f"You need {days} days to run {result} kilometers, if you will run 10% more everyday")

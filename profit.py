print("Hello! Welcome to the profit calculator!")
monthProfit = int(input("Please indicate your monthly profit: "))
print(" ")  # Я понимаю, что это не правильно,
# но пока не знаю как сделать правильно,
# по-этому делаю костыль :)
monthCost = int(input("Please indicate your monthly costs: "))
print(" ")
workersCount = int(input("Please indicate numbers of your workers: "))
print(" ")
pureProfit = round(monthProfit - monthCost, 2)
purePrftPerWrkrs = round(pureProfit / workersCount, 2)
if pureProfit > 0:
    print("Your business is profitable! Yor monthly income is", pureProfit)
else:
    print("Your business is unprofitable! Yor monthly outcome is", pureProfit)
print(" ")
if pureProfit > 0:
    print("On average, one employee brings you", purePrftPerWrkrs, "of profit")
else:
    print("On average, one employee cost you", purePrftPerWrkrs)

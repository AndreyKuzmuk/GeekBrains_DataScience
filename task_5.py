rating = [9, 5, 5, 4, 2, 2, 1]
n = 0
print(rating)
print()
user_rating = int(input("Enter new element of the rating: "))
print()
for i in rating:
    if user_rating <= i:
        n += 1
rating.insert(n, user_rating)
print(rating)

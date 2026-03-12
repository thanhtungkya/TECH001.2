seasons = ("spring", "summer", "autumn", "winter")
# 12, 1, 2: winter
# 3, 4, 5: spring
# 6, 7, 8: summer
# 9, 10, 11: autumn

n = int(input("Enter a month: "))
print(seasons[n//3 - 1])
a = list([])

for i in range(5):
    tmp = input(f"Enter your {i + 1} city: ")
    a.append(tmp)

for i in range(5):
    print(f"Name of city {i + 1}: {a[i]}")



minn = inf
maxx = -inf

while True:
    value = input("Enter a number (press Enter to quit): ")
    if value > maxx:
        maxx = value
    if value < minn:
        minn = value

if numbers:
    print("Smallest number:", minn)
    print("Largest number:", maxx)
else:
    print("No numbers were entered.")

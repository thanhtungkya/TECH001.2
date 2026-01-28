
while True:
    inch = float(input("Input number of inch: "))
    if inch < 0:
        break
    centi = inch * 2.54
    print(f"centimet is: {centi:0.2f}")

print("End.")
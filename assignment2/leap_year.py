import math

def unit_price(diameter_cm: float, price: float) -> float:
    radius_m = (diameter_cm / 100) / 2
    area = math.pi * radius_m ** 2
    return price / area


def main():
    d1 = float(input())
    p1 = float(input())

    d2 = float(input())
    p2 = float(input())

    price1 = unit_price(d1, p1)
    price2 = unit_price(d2, p2)

    if price1 < price2:
        print("The first pizza provides better value for money.")
    elif price2 < price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


if __name__ == "__main__":
    main()

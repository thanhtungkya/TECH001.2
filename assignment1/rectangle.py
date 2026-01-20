length, width = map(float, input("Enter length and width of you rectangle: ").split())

perimeter = 2 * (length + width)
area = length * width

print(f"perimeter of the rectangle is: {perimeter : 0.2f}")
print(f"area of the rectangle is: {area : 0.2f}")

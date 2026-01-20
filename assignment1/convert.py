talents, pounds, lots = map(float, input("Enter talents, pounds, lots: ").split())

total_grams = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3

kilos = float(total_grams / 1000)
grams = float(total_grams - int(kilos) * 1000)

print(f"kilos = {int(kilos)}, grams = {grams : 0.2f}")

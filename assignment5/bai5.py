import random

N = int(input("Enter the number of random points to generate: "))

n = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1

pi_approx = 4 * (n / N)
print(f"Approximation of pi: {pi_approx}")
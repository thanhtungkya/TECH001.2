import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Tạo 10 xe
cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))


# Đua xe
race_finished = False
hours = 0

while not race_finished:
    hours += 1

    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True


print("Race finished in", hours, "hours\n")

print(f"{'Reg':<10}{'MaxSpeed':<10}{'Speed':<10}{'Distance':<15}")
print("-" * 45)

for car in cars:
    print(f"{car.registration_number:<10}{car.max_speed:<10}{car.current_speed:<10}{car.travelled_distance:<15.2f}")
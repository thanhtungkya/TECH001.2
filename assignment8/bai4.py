import random

class Car:
    def __init__(self, reg, max_speed):
        self.registration_number = reg
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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n--- {self.name} ---")
        print(f"{'Reg':<10}{'Speed':<10}{'Distance':<15}")
        print("-" * 35)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.current_speed:<10}{car.travelled_distance:<15.2f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(150, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:
        race.print_status()

race.print_status()
print("\nRace finished in", hours, "hours")
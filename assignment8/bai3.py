class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, index, target_floor):
        self.elevators[index].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n🔥 FIRE ALARM! All elevators go to bottom floor")
        for i, elevator in enumerate(self.elevators):
            elevator.go_to_floor(self.bottom)
            print(f"Elevator {i} at floor {elevator.current_floor}")


b = Building(1, 10, 3)

b.run_elevator(0, 8)
b.run_elevator(1, 5)

b.fire_alarm()
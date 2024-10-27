import random

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self):
        self.distance_traveled += self.current_speed

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()

    def print_status(self):
        print(f"{'Car Name':<15}{'Max Speed':<15}{'Current Speed':<15}{'Distance Traveled':<15}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.name:<15}{car.max_speed:<15}{car.current_speed:<15}{car.distance_traveled:<15}")

    def race_finished(self):
        # Return True if any car has reached or passed the distance
        return any(car.distance_traveled >= self.distance for car in self.cars)

# Main program
cars = [
    Car("Car 1", 200),
    Car("Car 2", 180),
    Car("Car 3", 190),
    Car("Car 4", 210),
    Car("Car 5", 220),
    Car("Car 6", 200),
    Car("Car 7", 195),
    Car("Car 8", 205),
    Car("Car 9", 215),
    Car("Car 10", 225)
]

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nStatus after {hours} hours:")
        race.print_status()

print(f"\nFinal Status after {hours} hours:")
race.print_status()


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        print("Elevator is at floor", self.current_floor)

    def floor_up(self):
        self.current_floor += 1
        print("Elevator is now at floor", self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print("Elevator is now at floor", self.current_floor)

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Invalid floor. Please choose a floor between", self.bottom_floor, "and", self.top_floor)
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]
        print(f"Building with {num_elevators} elevators created.")

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid elevator number. Please choose a valid elevator.")

main = """
# Create a building with floors from 1 to 5 and 2 elevators
building = Building(1, 5, 2)

# Run the first elevator to the 3rd floor
building.run_elevator(0, 3)

# Run the second elevator to the 5th floor
building.run_elevator(1, 5)

# Bring the first elevator back to the 1st floor
building.run_elevator(0, 1)
"""

exec(main)

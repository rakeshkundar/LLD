import Display
import Direction
import Status
import InternalButton


class ElevatorCar:
    display: Display
    current_floor: int
    direction: Direction
    status : Status
    internal_button: InternalButton

    def move(destination_floor: int, direction: Direction):
        pass

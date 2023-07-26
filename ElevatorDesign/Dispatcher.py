import ElevatorController
import Direction

class Dispatcher:
    pass

class InternalButtonDispatcher:
    elevator_controllers_list: list(ElevatorController)

    def submit_request():
        pass

class ExternalButtonDispatcher:
    elevator_controllers_list: list(ElevatorController)
    
    def submit_request(floor: int, direction: Direction):
        pass
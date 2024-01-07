from vehicle_factory import VehicleFactory


if __name__ == '__main__':
    factory = VehicleFactory.get_vehicle_object(None)

    print(f"Tank capacity : {factory.get_tank_capacity()}")
    print(f"Seat capacity : {factory.get_seat_capacity()}")



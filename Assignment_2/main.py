"""Demonstrate the CampusWheels rental classes."""

from rental import ElectricCar, Motorbike, Renter, Vehicle


def main():
    car = Vehicle("Toyota", "Yaris", "1AB234")
    electric_car = ElectricCar("Tesla", "Model 3", "EV2026", 60)
    motorbike = Motorbike("Honda", "Click", "MB125", 125)
    renter = Renter("Erik", 1001)

    print("New renter:")
    print(f"{renter.name} (licence {renter.license_no})")

    print("\nRenting and returning a vehicle:")
    print(car)
    car.rent()
    print(car)
    car.return_vehicle()
    print(car)

    print("\nInvalid renter examples:")
    try:
        Renter("", 1002)
    except ValueError as error:
        print(f"Caught invalid name: {error}")

    try:
        Renter("Somchai", 0)
    except ValueError as error:
        print(f"Caught invalid licence: {error}")

    print("\nPolymorphism with mixed vehicle types:")
    vehicles = [car, electric_car, motorbike]
    for vehicle in vehicles:
        print(vehicle)


if __name__ == "__main__":
    main()

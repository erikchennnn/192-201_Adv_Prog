"""Object-oriented models for the CampusWheels rental desk."""


class Vehicle:
    """A vehicle that can be rented and returned."""

    def __init__(self, make, model, plate):
        self.make = make
        self.model = model
        self.plate = plate
        self.is_rented = False

    def rent(self):
        """Mark the vehicle as rented."""
        self.is_rented = True

    def return_vehicle(self):
        """Mark the vehicle as available."""
        self.is_rented = False

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return f"{self.make} {self.model} ({self.plate}) [{status}]."


class Renter:
    """A renter with validated personal details."""

    def __init__(self, name, license_no):
        self.name = name
        self.license_no = license_no
        self.rented = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must not be empty.")
        self._name = value

    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("License number must be a positive number.")
        self._license_no = value


class ElectricCar(Vehicle):
    """A vehicle powered by a battery."""

    def __init__(self, make, model, plate, battery_kwh):
        super().__init__(make, model, plate)
        self.battery_kwh = battery_kwh

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return (
            f"Electric car: {self.make} {self.model} ({self.plate}), "
            f"{self.battery_kwh} kWh [{status}]."
        )


class Motorbike(Vehicle):
    """A vehicle described by its engine capacity."""

    def __init__(self, make, model, plate, engine_cc):
        super().__init__(make, model, plate)
        self.engine_cc = engine_cc

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return (
            f"Motorbike: {self.make} {self.model} ({self.plate}), "
            f"{self.engine_cc} cc [{status}]."
        )

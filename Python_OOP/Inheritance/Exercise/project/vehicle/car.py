from project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle


class Car(Vehicle, CapacityMixin):
    def __init__(self, available_seats: int, fuel_tank: int, fuel_consumption: float, fuel: float):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value + self.__fuel <= self.fuel_tank:
            self.__fuel += value

    def drive(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        res = CapacityMixin.get_capacity(self.fuel_tank, self.fuel + liters)

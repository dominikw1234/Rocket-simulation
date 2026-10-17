import numpy as np

class Rocket:
    def __init__(self, mass_r, fuel, thrust, fuel_consumption):
        self.mass_r = mass_r
        self.fuel = fuel
        self.thrust = thrust
        self.fuel_consumption = fuel_consumption

    def calculate_mass(self):
        return self.mass_r + self.fuel

    def fuel_amount(self, time):
        self.time = time
        self.fuel_used = self.fuel_consumption * time
        self.fuel_usage = max((self.fuel - self.fuel_used), 0)
        self.velocity = self.thrust / self.mass_r
        return self.velocity


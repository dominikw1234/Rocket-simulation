class Rocket:
    def __init__(self, mass_r, fuel, thrust, fuel_consumption):
        self.mass_r = mass_r
        self.fuel = fuel
        self.thrust = thrust
        self.fuel_consumption = fuel_consumption

    def calculate_mass(self):
        return self.mass_r + self.fuel


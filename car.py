<<<<<<< HEAD
class Car:
    def __init__(self, name, fuel, velocity=60):
        self.name = name
        self.fuel = fuel
    
        if velocity <= 0:
            print(f" Velocity for {name} was 0, defaulting to 60 km/h.")
            velocity = 60
        self.velocity = velocity

    def drive(self, distance, velocity=None):
        if velocity is not None:
            if velocity <= 0:
                print(" Velocity must be > 0. Using default 60 km/h")
                velocity = 60
            self.velocity = velocity
        print(f"{self.name} is driving")
        self.fuel -= distance * 0.2  
        print(" Car stopped You have arrived at your destination.")

    def refuel(self, amount):
        self.fuel += amount
        print(f"{self.name} refueled with {amount} liters. Total fuel: {self.fuel}")
=======
class Car:
    def __init__(self, name, fuel, velocity=60):
        self.name = name
        self.fuel = fuel
    
        if velocity <= 0:
            print(f" Velocity for {name} was 0, defaulting to 60 km/h.")
            velocity = 60
        self.velocity = velocity

    def drive(self, distance, velocity=None):
        if velocity is not None:
            if velocity <= 0:
                print(" Velocity must be > 0. Using default 60 km/h")
                velocity = 60
            self.velocity = velocity
        print(f"{self.name} is driving")
        self.fuel -= distance * 0.2  
        print(" Car stopped You have arrived at your destination.")

    def refuel(self, amount):
        self.fuel += amount
        print(f"{self.name} refueled with {amount} liters. Total fuel: {self.fuel}")
>>>>>>> 40a56da3bccdad916880001c1e57cf442a6d5ba2

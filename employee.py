<<<<<<< HEAD
class Employee:
    def __init__(self, name, age, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        self.name = name
        self.age = age
        self.mood = mood
        self.healthRate = healthRate
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def drive(self, distance, velocity):
        self.car.drive(distance, velocity)

    def drive_to_work(self):
        self.car.drive(self.distanceToWork, self.car.velocity)

    def refuel(self, amount):
        self.car.refuel(amount)

    def __str__(self):
        return f"Employee({self.name}, ID={self.emp_id}, Email={self.email}, Salary={self.salary})"
=======
class Employee:
    def __init__(self, name, age, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        self.name = name
        self.age = age
        self.mood = mood
        self.healthRate = healthRate
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def drive(self, distance, velocity):
        self.car.drive(distance, velocity)

    def drive_to_work(self):
        self.car.drive(self.distanceToWork, self.car.velocity)

    def refuel(self, amount):
        self.car.refuel(amount)

    def __str__(self):
        return f"Employee({self.name}, ID={self.emp_id}, Email={self.email}, Salary={self.salary})"
>>>>>>> 40a56da3bccdad916880001c1e57cf442a6d5ba2

<<<<<<< HEAD
class Office:
    def __init__(self, name, start_hour=9):
        self.name = name
        self.start_hour = start_hour
        self.employees = []

  
    def hire(self, emp):
        self.employees.append(emp)
        print(f"{emp.name} has been hired at {self.name}.")

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            print(f"Employee {emp.name} (ID={emp_id}) has been fired.")
        else:
            print("Employee not found.")

    
    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def get_all_employees(self):
        return [f"{e.name} (ID={e.emp_id})" for e in self.employees]

   
    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if not emp:
            print("Employee not found.")
            return

        print(f"\n [Scenario] {emp.name} driving to {self.name} at {moveHour}h")
        emp.drive_to_work()

        try:
            is_late = Office.calculate_lateness(
                self.start_hour, moveHour, emp.distanceToWork, emp.car.velocity
            )
            if is_late:
                print(f"{emp.name} is late")
            else:
                print(f"{emp.name} arrived on time")
        except ValueError as e:
            print(f"[Error] {e}")

    @staticmethod
    def calculate_lateness(start_hour, move_hour, distance, velocity):
        if velocity <= 0:
            raise ValueError("Car velocity must be greater than 0 to calculate travel time.")
        travel_time = distance / velocity
        arrival_time = move_hour + travel_time
        return arrival_time > start_hour

    def deduct(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= amount
            print(f"{emp.name}'s salary deducted by {amount}. New salary: {emp.salary}")
        else:
            print("Employee not found.")


    def reward(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += amount
            print(f"{emp.name} rewarded by {amount}. New salary: {emp.salary}")
        else:
            print("Employee not found.")
=======
class Office:
    def __init__(self, name, start_hour=9):
        self.name = name
        self.start_hour = start_hour
        self.employees = []

  
    def hire(self, emp):
        self.employees.append(emp)
        print(f"{emp.name} has been hired at {self.name}.")

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            print(f"Employee {emp.name} (ID={emp_id}) has been fired.")
        else:
            print("Employee not found.")

    
    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def get_all_employees(self):
        return [f"{e.name} (ID={e.emp_id})" for e in self.employees]

   
    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if not emp:
            print("Employee not found.")
            return

        print(f"\n [Scenario] {emp.name} driving to {self.name} at {moveHour}h")
        emp.drive_to_work()

        try:
            is_late = Office.calculate_lateness(
                self.start_hour, moveHour, emp.distanceToWork, emp.car.velocity
            )
            if is_late:
                print(f"{emp.name} is late")
            else:
                print(f"{emp.name} arrived on time")
        except ValueError as e:
            print(f"[Error] {e}")

    @staticmethod
    def calculate_lateness(start_hour, move_hour, distance, velocity):
        if velocity <= 0:
            raise ValueError("Car velocity must be greater than 0 to calculate travel time.")
        travel_time = distance / velocity
        arrival_time = move_hour + travel_time
        return arrival_time > start_hour

    def deduct(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= amount
            print(f"{emp.name}'s salary deducted by {amount}. New salary: {emp.salary}")
        else:
            print("Employee not found.")


    def reward(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += amount
            print(f"{emp.name} rewarded by {amount}. New salary: {emp.salary}")
        else:
            print("Employee not found.")
>>>>>>> 40a56da3bccdad916880001c1e57cf442a6d5ba2

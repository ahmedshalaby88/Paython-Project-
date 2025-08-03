<<<<<<< HEAD
from car import Car
from employee import Employee
from office import Office


office = Office("ITI Smart Village")
car_samy = Car("Fiat 128", 100, 100)
samy = Employee("Samy", 500, "neutral", 80, 1, car_samy, "samy@iti.com", 5000, 20)
office.hire(samy)


print("\n  Samy driving to ITI at 7:30 AM (7.5h) ")
samy.drive(20, 100)
office.check_lateness(1, moveHour=7.5)


while True:
    print("\n===== Office Management Menu =====")
    print("1. Show all employees")
    print("2. Hire new employee")
    print("3. Fire employee")
    print("4. Check lateness")
    print("5. Deduct salary")
    print("6. Reward employee")
    print("7. Drive to work")
    print("8. Refuel employee car")
    print("9. Exit")

  
    try:
        choice = int(input("Choose an option (1-9): "))
    except ValueError:
        print("Error: Please enter a valid number")
        continue

    if not (1 <= choice <= 9):
        print("Invalid choice Enter a number between 1 and 9.")
        continue

   
    if choice == 1:
        print("Employees:", office.get_all_employees())

    elif choice == 2:
        name = input("Enter name: ")
        emp_id = int(input("Enter ID: "))
        email = input("Enter email: ")
        salary = float(input("Enter salary: "))
        distance = float(input("Enter distance to work: "))
        car_name = input("Enter car name: ")
        car = Car(car_name, 100, 100)
        new_emp = Employee(name, 500, "neutral", 80, emp_id, car, email, salary, distance)
        office.hire(new_emp)

    elif choice == 3:
        emp_id = int(input("Enter employee ID to fire: "))
        office.fire(emp_id)

    elif choice == 4:
        emp_id = int(input("Enter employee ID: "))
        moveHour = float(input("Enter move hour: "))
        office.check_lateness(emp_id, moveHour)

    elif choice == 5:
        emp_id = int(input("Enter employee ID: "))
        amount = float(input("Enter deduction amount: "))
        office.deduct(emp_id, amount)

    elif choice == 6:
        emp_id = int(input("Enter employee ID: "))
        amount = float(input("Enter reward amount: "))
        office.reward(emp_id, amount)

    elif choice == 7:
        emp_id = int(input("Enter employee ID: "))
        emp = office.get_employee(emp_id)
        if emp:
            dist = float(input("Enter distance: "))
            vel = float(input("Enter velocity: "))
            if vel <= 0:
                print(" Velocity must be > 0, using default 60 km/h")
                vel = 60
            emp.drive(dist, vel)
        else:
            print("Employee not found.")

    elif choice == 8:
        emp_id = int(input("Enter employee ID: "))
        emp = office.get_employee(emp_id)
        if emp:
            amount = float(input("Enter fuel amount: "))
            emp.refuel(amount)
        else:
            print("Employee not found.")

    elif choice == 9:
        print("Exiting program")
        break
=======
from car import Car
from employee import Employee
from office import Office


office = Office("ITI Smart Village")
car_samy = Car("Fiat 128", 100, 100)
samy = Employee("Samy", 500, "neutral", 80, 1, car_samy, "samy@iti.com", 5000, 20)
office.hire(samy)


print("\n  Samy driving to ITI at 7:30 AM (7.5h) ")
samy.drive(20, 100)
office.check_lateness(1, moveHour=7.5)


while True:
    print("\n===== Office Management Menu =====")
    print("1. Show all employees")
    print("2. Hire new employee")
    print("3. Fire employee")
    print("4. Check lateness")
    print("5. Deduct salary")
    print("6. Reward employee")
    print("7. Drive to work")
    print("8. Refuel employee car")
    print("9. Exit")

  
    try:
        choice = int(input("Choose an option (1-9): "))
    except ValueError:
        print("Error: Please enter a valid number")
        continue

    if not (1 <= choice <= 9):
        print("Invalid choice Enter a number between 1 and 9.")
        continue

   
    if choice == 1:
        print("Employees:", office.get_all_employees())

    elif choice == 2:
        name = input("Enter name: ")
        emp_id = int(input("Enter ID: "))
        email = input("Enter email: ")
        salary = float(input("Enter salary: "))
        distance = float(input("Enter distance to work: "))
        car_name = input("Enter car name: ")
        car = Car(car_name, 100, 100)
        new_emp = Employee(name, 500, "neutral", 80, emp_id, car, email, salary, distance)
        office.hire(new_emp)

    elif choice == 3:
        emp_id = int(input("Enter employee ID to fire: "))
        office.fire(emp_id)

    elif choice == 4:
        emp_id = int(input("Enter employee ID: "))
        moveHour = float(input("Enter move hour: "))
        office.check_lateness(emp_id, moveHour)

    elif choice == 5:
        emp_id = int(input("Enter employee ID: "))
        amount = float(input("Enter deduction amount: "))
        office.deduct(emp_id, amount)

    elif choice == 6:
        emp_id = int(input("Enter employee ID: "))
        amount = float(input("Enter reward amount: "))
        office.reward(emp_id, amount)

    elif choice == 7:
        emp_id = int(input("Enter employee ID: "))
        emp = office.get_employee(emp_id)
        if emp:
            dist = float(input("Enter distance: "))
            vel = float(input("Enter velocity: "))
            if vel <= 0:
                print(" Velocity must be > 0, using default 60 km/h")
                vel = 60
            emp.drive(dist, vel)
        else:
            print("Employee not found.")

    elif choice == 8:
        emp_id = int(input("Enter employee ID: "))
        emp = office.get_employee(emp_id)
        if emp:
            amount = float(input("Enter fuel amount: "))
            emp.refuel(amount)
        else:
            print("Employee not found.")

    elif choice == 9:
        print("Exiting program")
        break
>>>>>>> 40a56da3bccdad916880001c1e57cf442a6d5ba2

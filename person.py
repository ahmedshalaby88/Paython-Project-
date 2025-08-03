class Person:
    def __init__(self, name, age, mood="neutral", healthRate=100, email=None):
        self.name = name
        self.age = age
        self.mood = mood
        self.healthRate = healthRate
        self.email = email

    def sleep(self, hours):
        if hours < 6:
            self.mood = "tired"
        elif 6 <= hours <= 8:
            self.mood = "happy"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            self.healthRate = 30

    def __str__(self):
        return f"Person({self.name}, Age={self.age}, Mood={self.mood}, Health={self.healthRate}, Email={self.email})"

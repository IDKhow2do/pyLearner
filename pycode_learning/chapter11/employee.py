class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary
    
    def get_name(self):
        return self.name
    
    def raise_salary(self, amount=5000):
        self.salary += amount
        return self.salary

#Q1: Define a circle class to create with radius r using the constructor.
#Define an area() method of circle which calculates the area of the circle
#Define a perimeter() method of the class which allows you to calculate the primeter of the circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#Q2: Define a Employee class with attributes role, department & salary. This class also showDetails() method.
#Create an Engineer class that inherits properties from Employee

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept= dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer (Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("Rahul", "78")
engg1.showDetails()

e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()
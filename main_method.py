"""
print('-----MAIN METHODS----')
print('First method:{}'.format(__name__))

def main():
    print('This is the main method')


if __name__ == "__main__":
    main()

"""

print('---Addition of two numbers----')

"""
class Add:

    def __init__(self):
        self.a = 5
        self.b = 10
        self.result = self.a + self.b
        print('The result ={}'.format(self.result))


class Mul:
    def __init__(self):
        self.a = 2
        self.b = 2
        self.result = self.a * self.b
        print('The result ={}'.format(self.result))


class Sub:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = self.a - self.b
        print('The result ={}'.format(self.result))


if __name__ == "__main__":
    print()
    a = Add()
    b = Mul()
    c = Sub(12, 12.5)

"""


class CivilDepartment:

    def __init__(self, Department, roll_no, attendance):
        self.Department = Department
        self.roll_no = roll_no
        self.attendance = attendance

    def display(self):
        print('The department is {}'.format(self.Department))
        print('The roll_no is {}'.format(self.roll_no))
        print('The attendance  is {}'.format(self.attendance))


class MechanicalDepartment:

    def __init__(self, Subject, Pratical):
        self.Subject = Subject
        self.Pratical = Pratical

    def display_data(self):
        print('The Subject lecture is {}'.format(self.Subject))
        print('The Pratical class is {}'.format(self.Pratical))


if __name__ == "__main__":
    a = CivilDepartment('Engineering', 1222, 75)
    b = MechanicalDepartment('CAD', 'Audit')
    for i in [a.display(), b.display_data()]:
        i

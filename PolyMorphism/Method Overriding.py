"""4. Method Overriding: By using method overriding a class may “copy” another class, avoiding duplicated code,
and at the same time enhance or customize a part of it. Method overriding is thus a part of the inheritance mechanism.

In Python, method overriding occurs by simply defining the child class in a method with the same name as a method in the parent class."""

"""
class Programming_Java:

    def practice(self):
        print('Practice can make man perfect')

    def consistency(self):
        print('Hard Work can defeat talent')


class Programming_Python(Programming_Java):

    def consistency(self):
        print('Hard Work can defeat talent')


a = Programming_Python()
print('-----Method Overriding-----')
a.consistency()
a.practice()

"""


class Operation:
    print('----------Basic Example of Method Overriding------------')

    def Add(self, a, b):
        self.a = a
        self.b = b
        result = self.a + self.b

    def display(self):
        print('The addition=', self.result)


class Operation_WithThree(Operation):

    def Add(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.result = self.a + self.b + self.c

    def display(self):
        print('The addition of three numbers=', self.result)


a1 = Operation_WithThree()
a1.Add(12, 12, 12)
a1.display()

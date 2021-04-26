"""Operator Overloading: Operator overloading in Python is the ability of a single operator to perform more than one
operation based on the class (type) of operands. So, basically defining methods for operators is known as operator
overloading. For e.g: To use the + operator with custom objects  you need to define a method called __add__.

 We know + operator is used for adding numbers and at the same time to concatenate strings. It is possible because
 the + operator is overloaded by both int class and str class. The operators are actually methods defined in
 respective classes.

So if you want to use the + operator to add two objects of some user-defined class then you will have to define that behavior yourself and inform Python about that."""


class Student:
    print('----Operator Overloading----')
    print()

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


s1 = Student(58, 60)
s2 = Student(59, 60)
s3 = s1 + s2
print(s3.m1)
print()
print(s3.m2)


class Student2:
    print()
    print('---Operator Overloading in Second Class')
    print()

    def __init__(self, m1, m2):
        # self.__m1=m1 # Private access modifier
        self._m1 = m1  # Protected access modifier
        self._m2 = m2

    def __add__(self, other):
        # m1=self.__m1 - other.__m1
        m1 = self._m1 - other._m1
        m2 = self._m2 - other._m2
        s3 = Student2(m1, m2)
        return s3


a1 = Student2(12, 12)
a2 = Student2(29, 28)
a3 = a1 + a2
# a3.__m1 cannot be access as it is private
print(a3._m1)
print()
print(a3._m2)

print(dir(a1))

"""Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variable.
A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
"""

"""Real Life Example Consider a real-life example of encapsulation, in a company, there are different sections like 
the accounts section, finance section, sales section etc. The finance section handles all the financial transactions 
and keeps records of all the data related to finance. Similarly, the sales section handles all the sales-related 
activities and keeps records of all the sales. Now there may arise a situation when for some reason an official from 
the finance section needs all the data about sales in a particular month. In this case, he is not allowed to directly 
access the data of the sales section. He will first have to contact some other officer in the sales section and then 
request him to give the particular data. This is what encapsulation is. Here the data of the sales section and the 
employees that can manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides 
the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other 
section. """
"""

class Base:

    def __init__(self):
        self._a = 2
        self.__c = 3


class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print('Calling protected members of base class')

        print(self._a)
        # print(self.__c)


obj1 = Derived()
obj2 = Base()

# Calling protected member
# Outside class will  result in
# AttributeError
obj2._a


# obj1.__c  # Private Member
"""


class Student:

    def __init__(self):
        self._first_name = 'Asif'
        self.__last_name = 'Tandel'


class College_location(Student):

    def __init__(self):
        self._college_location = 'Washington_DC'
        Student.__init__(self)
        print('Protected Members of College_location')
        print(self._first_name)
        # print(self.__last_name)
        print()
        print(self._college_location)


obj1 = College_location()
obj2 = Student()
print('')
obj2._first_name
# print(obj2.__last_name)
obj1._college_location

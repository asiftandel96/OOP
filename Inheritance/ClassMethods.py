"""The classmethod() is an inbuilt function in Python, which returns a class method for a given function.

Syntax:
classmethod(function)

Parameter :This function accepts the function name as a parameter.

Return Type:This function returns the converted class method.


Description:-
classmethod() methods are bound to a class rather than an object.
Class methods can be called by both class and object. These methods can be called with a class or with an object.
"""
print('-----UNDERSTANDING THE CONCEPTS OF CLASSMETHODS--------')


class StudentA:
    name = 'GeeksForGeeks'

    def printname(obj):
        print('The name is', obj.name)


print()
StudentA.printname = classmethod(StudentA.printname)

# now this method can be called as classmethod
# print_name() method is called a class method
StudentA.printname()


class Subject_11:
    Subject_name = 'Physics'

    def print_subject(cls):
        print('The subject is', cls.Subject_name)


print()
Subject_11.print_subject = classmethod(Subject_11.print_subject)
Subject_11.print_subject()


#ClassMethod Usage
"""classmethod() function is used in factory design patterns where we want to call many functions with the class name 
rather than object. """


"""Basic Example of Exception Handling"""
"""

class Ex_Operation:

    def __init__(self, a, b):
        try:
            self.a = a
            self.b = b
            self.result = self.a / self.b
            if self.result > 5:
                print('The result is good')
            elif self.result == 5:
                print('Howrah!!!!')
            else:
                print('the result is ok')
        except ZeroDivisionError:
            print('The Denominator should be greater than zero')
        except TypeError:
            print('The Type should be specified correctly')
        except Exception as ex:
            print(ex)
        finally:
            print('------The Execution is done--------')


if __name__ == "__main__":
    a = Ex_Operation(25, 5)
"""

"""Custom Exception Handling"""


class Error(Exception):
    pass


class dobException(Error):
    pass


def Ex():
    year = int(input('Enter the year'))
    age = 2021 - year
    try:
        if age <= 30 & age > 20:
            print('The age is valid and you can apply for the exams')
        else:
            raise dobException
    except dobException:
        print('The age is not in the range and you cannot apply for exams')


Ex()

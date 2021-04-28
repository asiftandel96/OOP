"""-----------------------------------ITERATORS CONCEPTS--------------------------------"""

# This library is the wrapper for numpy,pandas,matplotlib and seaborn
import self as self
"""
from pyforest import *


# Create Number Upto 10

# Looping through the list
class Iterator_Concepts:

    def __init__(self):
        Natural_No = np.arange(1, 10, 1)
        # Getting an iterator through iter()
        # print('-----------------FIRST APPROACH OF CREATING AN ITERATOR By USING iter()-------------------')
        iteri_concepts = iter(Natural_No)
        # Iterating through it using next()

        print(next(iteri_concepts))
        print('-------------------SECOND APPROACH OF CREATING AN ITERATOR  BY  USING .__next__() ------------')
        print(iteri_concepts.__next__())
        print("Creating A Function to Iterate through")
        print()

        for i in iteri_concepts:
            print(i, end=' ')

    def my_iterator(self):
        print('My Iterator Function')
        try:
            # counter = 0
            # print('The counter =', counter)
            my_list_2 = np.arange(10, 140, 10)
            my_iter_1 = iter(my_list_2)
            for i in my_iter_1:
                if i == 120:
                    continue
                else:
                    print(i)
        except NameError:
            print('Name is not defined')
        except Exception:
            print("Other Exception")
        finally:
            print('The execution is done')


if __name__ == "__main__":
    a = Iterator_Concepts()
    a.my_iterator()
"""

# Some Basic Example to understand Iterators in depth
"""
class Addition:
    def __init__(self, a: int, b: int) -> int:
        try:
            self.a = a
            self.b = b
        except NameError:
            print('The Name is not defined properly')
        except TypeError:
            print('The Type should be specified correctly')
        except Exception:
            pass

    def __iter__(self):
        '''The __iter__() function returns an
        iterator for the given object (array, set, tuple etc. or custom objects).
        It creates an object that can be accessed one element at a time using __next__()
        function, which generally comes in handy when dealing with loops.
        '''
        try:

            self.result = self.a + self.b
            return f"The result is ", self.result
        except TypeError:
            print('The Type should be specified Correctly')
        except Exception:
            pass

    def __next__(self):
        print('No Value Present Please Write Once ')


if __name__ == "__main__":
    Addition_no = Addition(3, 3)
    print(Addition_no.__iter__())
    print(Addition_no.__iter__())
    Addition_no.__next__()

"""

# Here we are taking a example of power of 2 in each iteration.Power exponent start from zero up to set numbers
"""
class PowTwo:
    '''Class to Implement an Iterator of power of two  '''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":

    numbers = PowTwo(10)
    i = iter(numbers)
    for item in numbers:
        print(item)
        
"""


# Now Using Some Example to showcase iterators
class TopTen:

    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 10:
            val = self.n
            self.n += 1
            return val
        else:
            raise StopIteration


if __name__ == "__main__":

    TopTen_no = TopTen()
    a = iter(TopTen_no)
    for i in a:
        print(i, end=' ')

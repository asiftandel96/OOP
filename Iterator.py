"""----------------------------------Iterators------------------------------------ """
"""
my_list = [1, 2, 3, 4]  # Creating A List
my_iter = iter(my_list)  # Getting an iterator using iter()
print(next(my_iter))  # Iterating through it using next()
print(my_iter.__next__())  # # next(obj) is same as obj._next_()
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

"""


def my_iterator():
    try:
        # counter = 0
        # print('The counter =', counter)
        my_list_2 = [1, 2, 3, 4, 5]
        my_iter_1 = iter(my_list_2)
        for i in my_iter_1:
            if i == 3:
                continue
            else:
                print(i)
    except NameError:
        print('Name is not defined')
    except Exception:
        print("Other Exception")
    finally:
        print('The execution is done')


my_iterator()

# Iterating through the for loop- This is a more efficient way to iterate through the loop
# for item in my_iter:
#    print(item)


# Just some simple exercise for Iterators
"""
class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = self.a + self.b

    def __iter__(self):
        return self.result


Addition_no = Addition(3, 4)
print(Addition_no.__iter__())
"""
# Here we are taking a example of power of 2 in each iteration.Power exponent start from zero up to set numbers
"""
class PowTwo:
    '''Class to Implement an Iterator of power of two'''

    def __init__(self, max=0):
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


numbers = PowTwo(10)
i = iter(numbers)
print(next(i))
for item in numbers:
    print(item)
"""

# Write a Program to find the cube of the number using Iterator
"""
class Cube:

    def __init__(self, max=0):

        self.max = max

    def __iter__(self):

        self.n = 0
        return self

    def __next__(self):

        if self.n <= self.max:
            result = 3 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


N = Cube(5)
i1 = iter(N)
print(next(i1))
print(next(i1))
print(next(i1))
"""
# Creating Your own Iterators
"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

"""
# Creating A Tuple
"""
Tuples_no = (1, 2, 3, 4)
# Using an Iter methods to see the value
i = iter(Tuples_no)
# Displaying the first value
print(i.__next__())
"""

# Now Using Some Example to showcase iterators
"""
class TopTen:
    
    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 10:
            val = self.n
            self.n += 1
        else:
            raise StopIteration
        return val


TopTen_no = TopTen()
# i=iter(TopTen_no)
# print(next(i))#print(next(i))print(next(i))
for i in TopTen_no:
    print(i)

"""

# Write A Program to see even numbers in the function using Iterator
"""
class Even_Numbers:
    def __init__(self, a):
        self.num = 1
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.a:
            val = (self.num % 2 == 0 and self.num % 3 == 0)
            self.num += 1
            return val
        else:
            raise StopIteration


Even_No = Even_Numbers(30)
# i=iter(Even_No)
# print(next(i))
for i in Even_No:
    print(i)
"""

# Write A Python Program for no divisible by 4 and 5 using Iterator
"""
class Top6:
    def __init__(self, b):
        self.no = 1
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.no <= self.b:
            val = (self.no % 4 == 0 and self.no % 5 == 0)
            self.no += 1
            return val
        else:
            raise StopIteration


Top = Top6(50)
for i in Top:
    print(i)





class No:

    def __init__(self, numbers):
        self.numbers = numbers
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.numbers:
            val = (self.n % 2 == 0)
            self.n += 1
            return val
        else:
            raise StopIteration


N = No(30)
for i in N:
    print(i)

"""

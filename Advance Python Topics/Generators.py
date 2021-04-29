# Creating Generators
def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'


a = my_gen()
print(type(a))
print(a.__next__())
print(a.__next__())
print(a.__next__())
# Implementing Generators
"""
import time


def countdown(num):
    print('Countdown started...')
    while num > 0:
        yield num
        num = num - 1


value = countdown(20)
for i in value:
    print(i)
    time.sleep(1)




# To generate first n numbers
def first(num):
    n = 1
    while n <= num:
        yield n
        n = n + 1


for x in first(20):
    print(x)
"""

# How to generate Fibonacci numbers
"""
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for x in fib():
    if x > 100:
        break
    print(x)
"""
# Show the differennce of performance with respect to generators
"""
import time
import random

names = ['sunny', 'bunny', 'chinny', 'vinny']
subjects = ['Python', 'Java', 'blockchain']


def people_list(num):
    result = []
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        result.append(person)
        return result


def people_generator(num):
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        yield person


t1 = time.process_time_ns()
people = people_list(10000)
t2 = time.process_time_ns()
print('Time taken for List:', t2 - t1)

t1 = time.process_time_ns()
people = people_generator(10000)
t2 = time.process_time_ns()
print('Time Taken for Generators:', t2 - t1)

"""

# Write A Program to find even no using Generators
"""
def evens():
    i = 1
    while True:
        if i % 2 == 0:
            yield i
        i += 1


for x in evens():
    if x > 200:
        break
    print(x)
"""
# Write A Program to calculate Fibonacci numbers from 1 to 200
"""
def Fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


for x in Fib():
    if x > 200:
        break
    print(x)

"""

# Write A Python Program to find odd number using yield keyword
"""
def Odd():
    n = 1
    while True:
        if n % 2 != 0:
            yield n
            n += 2


i = Odd()
print(next(i))
print(next(i))
"""
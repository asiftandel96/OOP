# Building Generators With Generator ExpressionsBuilding Generators With Generator Expressions

# Like list comprehensions, generator expressions allow you to quickly create a generator object in just a few lines
# of code. They’re also useful in the same cases where list comprehensions are used, with an added benefit: you can
# create them without building and holding the entire object in memory before iteration. In other words, you’ll have
# no memory penalty when you use generator expressions. Take this example of squaring some numbers:

num_squared_lc = [num ** 2 for num in range(1, 5) if num % 2 == 0]
print(num_squared_lc)
num_squared_gc = (num ** 2 for num in range(1, 5))
print(num_squared_gc)  # generator object
print(next(num_squared_gc))  # Now iterate through it

# The first object used brackets to build a list, while the second created a generator expression by using
# parentheses. The output confirms that you’ve created a generator object and that it is distinct from a list.

# Profiling Generator Performance You learned earlier that generators are a great way to optimize memory. While an
# infinite sequence generator is an extreme example of this optimization, let’s amp up the number squaring examples
# you just saw and inspect the size of the resulting objects. You can do this with a call to sys.getsizeof():

import sys

print()
print('Check Memory Space b/w List Vs Generators')
num_squ_list = [i * 2 for i in range(10000)]
print(sys.getsizeof(num_squ_list))
num_sq_generator = (i * 2 for i in range(10000))
print(sys.getsizeof(num_sq_generator))

# We can clearly see that generator have 100 time less size than list and dictionary

import cProfile

print('LIST PERFORMANCE')
cProfile.run('sum([i * 2 for i in range(10000)])')
print('GENERATOR PERFORMANCE')
cProfile.run('sum((i * 2 for i in range(10000)))')

"""Here, you can see that summing across all values in the list comprehension took about a third of the time as 
summing across the generator. If speed is an issue and memory isn’t, then a list comprehension is likely a better 
tool for the job. 

Note: These measurements aren’t only valid for objects made with generator expressions. They’re also the same for 
objects made from the analogous generator function since the resulting generators are equivalent. 

Remember, list comprehensions return full lists, while generator expressions return generators. Generators work the 
same whether they’re built from a function or an expression. Using an expression just allows you to define simple 
generators in a single line, with an assumed yield at the end of each inner iteration. 


The Python yield statement is certainly the linchpin on which all of the functionality of generators rests, 
so let’s dive into how yield works in Python. 

"""

# Understanding the Python Yield Statement
"""On the whole, yield is a fairly simple statement. Its primary job is to control the flow of a generator function 
in a way that’s similar to return statements. As briefly mentioned above, though, the Python yield statement has a 
few tricks up its sleeve. 

When you call a generator function or use a generator expression, you return a special iterator called a generator. 
You can assign this generator to a variable in order to use it. When you call special methods on the generator, 
such as next(), the code within the function is executed up to yield. 

When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the 
caller. (In contrast, return stops function execution completely.) When a function is suspended, the state of that 
function is saved. This includes any variable bindings local to the generator, the instruction pointer, the internal 
stack, and any exception handling. 

This allows you to resume function execution whenever you call one of the generator’s methods. In this way, 
all function evaluation picks back up right after yield. You can see this in action by using multiple Python yield 
statements: 

"""

print('The yield leyword')


def multi_yield():
    yieldstr1 = "This is  the first string"
    yield yieldstr1
    yieldstr2 = 'This is the second string'
    yield yieldstr2


a = multi_yield()
print(sys.getsizeof(a))
print(a.__next__())
print(a.__next__())


class NorGenDif:

    def __init__(self):
        pass

    @staticmethod
    def Add_Return():
        """Normal Function"""
        a = 500 ** 2
        b = 600 ** 5
        result = a + b
        print('The Normal Function Size is', sys.getsizeof(result))
        return 'The normal function result =', result

    @staticmethod
    def Add_Generator():
        """Generator Function"""
        c = 500 ** 2
        d = 600 ** 5
        result_1 = c + d

        yield 'The generator function =', result_1


if __name__ == "__main__":
    a = NorGenDif()
    print(a.Add_Return())
    # print('The Normal Function Size is', sys.getsizeof(a))
    print(a.Add_Generator().__next__())
    print('The Generator Function Size is ', sys.getsizeof(a))

"""Take a closer look at that last call to next(). You can see that execution has blown up with a traceback. This is 
because generators, like all iterators, can be exhausted. Unless your generator is infinite, you can iterate through 
it one time only. Once all values have been evaluated, iteration will stop and the for loop will exit. If you used 
next(), then instead you’ll get an explicit StopIteration exception """
print()
print('----------STOPITERATION EXPLAINATION------------')
letter = ['a', 'b', 'c', 'd']
it = iter(letter)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)

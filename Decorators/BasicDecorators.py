"""Function Copy"""
"""
# Creating A Function
def welcome_DataScience():
    return "Welcome to Data Science Program"


# Calling the Function
# welcome_DataScience()
# Assigning the function to varible a
a = welcome_DataScience()
#print(a)
# deleting the function
del welcome_DataScience
# Now we check that if the variable a has the contents of the function is called function copy
print(a)

"""

"""This is A Python Closure Method """


def outer():
    print('Welcome to Data Science Program')

    def inner():
        print('This is A Supervised Learning Approach')
    inner()


outer()

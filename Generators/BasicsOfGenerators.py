"""
class BasicThings:
    def __init__(self):
        pass

    def csv_reader(self, file_name):
        try:
            file_name = open(file_name)
            result = file_name.read().split("\n")
            return result
        except NameError as ex:
            print(ex)
        except FileNotFoundError as ex:
            print(ex)
        except MemoryError as ex:
            print(ex)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    a = BasicThings()
    csv_gen = a.csv_reader("somecsv")
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print("Row count =",row_count)
    print('The Execution is done')

"""

# Creating A Generator and Using Class
"""
class GeneratorO:
    def __init__(self):
        pass

    def csv_reader(self, file_name):
        for row in open(file_name, "rb"):
            yield row


if __name__ == "__main__":
    a = GeneratorO()
    csv_gen = a.csv_reader('D:\Python Code\sudeste.csv')
    row_count = 0
    for row in csv_gen:
        row_count += 1

print('The row count =', row_count)

"""

"""Example 2: Generating an Infinite Sequence Let’s switch gears and look at infinite sequence generation. In Python, 
to get a finite sequence, you call range() and evaluate it in a list context: """
"""
a = range(0, 5)
print(list(a))
"""

"""
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_sequence():
#    print(i, end=" ")

gen = infinite_sequence()
print(next(gen))
print(next(gen))

"""


class Palindrome:

    def __init__(self):
        pass

    def is_palindrome(self, num):
        # Skip single_digits_inputs
        if num // 10 == 0:
            return False
        temp = num
        reverse_num = 0

        while temp != 0:
            reverse_num = (reverse_num * 10) + (temp % 10)
            temp = temp // 10

        if num == reverse_num:
            return num
        else:
            return False

    def infinite_sequence(self):

        num = 0
        while True:
            num += 1
            yield num


if __name__ == "__main__":

    a = Palindrome()
    for i in a.infinite_sequence():

        pal = a.is_palindrome(i)
        if pal:
            print(pal)

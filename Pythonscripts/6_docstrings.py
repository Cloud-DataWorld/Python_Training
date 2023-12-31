"""
1 . Docstrings provide a convenient way of associating documentation with functions,classes,methods or modules.
2 . They appear right after the definition of a function, method, class or mdoule

"""

def square(num):
    ''' Square Function : - This fucntion will return the square of a number '''
    return num**2

print(square(10))

# we can access the docstring using __doc__ method

print(square.__doc__)

# example 2
def evenodd(num):
    ''' evenodd function : - this function will test whether a number is even or odd '''
    if num % 2 == 0:
        print('Even Number')
    else:
        print('Odd Number')

print(evenodd(3))
print(evenodd(8))
print(evenodd.__doc__)
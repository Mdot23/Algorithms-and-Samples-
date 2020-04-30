"""if n != 0 the function will return the result.
Until n == 0 condition is satifsfied it will multiply n-1
Once n == 0, the first branch will return 1 without making any more recursive calls"""

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        # Stores recurse * n in variable to call function from within function and perform recursion.
        result = n * recurse 
        return result 


# Function will print statement in second block if NOT an integer data type. 
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
    elif n == 0:
        return 1 
    else:
        return n * factorial(n-1)


# Recursive function with additional visability for debugging 
def factorial(n):
    space = ' ' * (4*n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n  * recurse
        print(space, 'returning', result) 
        return result 








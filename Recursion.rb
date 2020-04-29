# Sample 1 

# Iteractive factorial 
def iterative_factorial n
    # Factorial of 5 = 1 * 2 *3 * 4 * 5 
    (1..n).inject(:*)
end 

# Recrusive factorial
def recursive_factorial n
    return 1 if n <= 1 

    # recursive call 
    n * recursive_factorial(n-1)
end 

  
recursive_factorial(5)

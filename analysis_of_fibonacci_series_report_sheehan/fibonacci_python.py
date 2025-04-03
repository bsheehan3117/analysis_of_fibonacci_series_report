"""
Brendan Sheehan
This file contains three implementations of the Fibonacci sequence in python. The Fibonacci sequence is a series of numbers in 
which each number is the sum of the two preceding ones, usually starting with 0 and 1. This file contains an iterative 
implementation, a recursive implementation, and a dynamic programming implementation. 

Each implementation takes two arguments: 
the nth value of the Fibonacci sequence.
A print level that determines whether to print the entire sequence(2), the nth value(1), or nothing and return the value(0).

The iterative function calculates the Fibonacci sequence by iterating over each index up to n and summing the two 
previous numbers in the sequence.

The recursive function solves the same problem through recursion, calling itself with n-1 and n-2 until reaching the 
base case (n=0 or n=1).

The dynamic programming function uses recursion and memoization to store values in an array.
"""
import sys  


def fibonacci_iterative_python(n, print_level):
    "Iterative function to calculate the fibonacci series"
    
    # initialize first 2 numbers
    a, b = 0, 1  
    
    # print first fib number if print level 2
    if print_level > 1:
        print(a, end=' ')
        
    # for loop to calculate nth number
    for _ in range(n):
        a, b = b, a + b  
        # print each fib number if print level 2
        if print_level > 1:
            print(a, end=' ')
            
    # print nth number
    if print_level == 1:
        print(a)
    return a

def fibonacci_recursive_python(n, print_level):
    "Recursive function to calculate the fibonacci series"
    
    # base case 
    if n <= 1:
        if print_level > 0:
            print(n)
        return n
    
    # calculate the nth Fibonacci number using recursion
    result = fibonacci_recursive_python(n - 1, print_level) + fibonacci_recursive_python(n - 2, 0)
    if print_level == 1 and n == print_level:
        print(result)
    return result


def fibonacci_dynamic_programming_python(n, print_level):
    "Function to calculate the fibonacci series with dynamic programming."
    
    # initialize memoization table
    darray = [-1 for _ in range(n + 1)]

    
    def dynamic_helper(n):
        "Helper function for dynamic solution"
        
        # Set base case
        if darray[n] != -1:
            return darray[n]

        if n <= 1:
            darray[n] = n
            # print each line if print level 2
            if print_level == 2:
                print(n, end=' ')
            return n

        # calculate n
        darray[n] = dynamic_helper(n - 1) + dynamic_helper(n - 2)

        # Print if print_level is 2
        if print_level == 2:
            print(darray[n], end=' ')
        return darray[n]

    # call recursively
    return dynamic_helper(n)


if __name__ == "__main__":
    
    # n to int
    n = int(sys.argv[1])  
    
    # select algo
    algo = sys.argv[2]  
    
    # print level to int
    print_level = int(sys.argv[3])  
    result = None

    # call function based on algorithm
    if algo == "iterative":
        result = fibonacci_iterative_python(n, print_level)
    elif algo == "recursive":
        result = fibonacci_recursive_python(n, print_level)
    elif algo == "dp":
        result = fibonacci_dynamic_programming_python(n, print_level)
    else:
        print("Invalid algorithm choice.")
        sys.exit(1)  

    print(result) 
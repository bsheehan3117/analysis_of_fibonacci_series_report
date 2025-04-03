/*Brendan Sheehan
*
* This file contains three implementations of the Fibonacci sequence in C. The Fibonacci sequence is a series of numbers in 
* which each number is the sum of the two preceding ones, usually starting with 0 and 1. This file contains an iterative 
* implementation, a recursive implementation, and a dynamic programming implementation. 
* 
* This file also contains tests for the above functions which can be run in the main function 
* by writing "test" as an argument after running the file.
*
* Each implementation takes two arguments: 
* the nth value of the Fibonacci sequence.
* A print level that determines whether to print the entire sequence(2), the nth value(1), or nothing and return the value(0).
*
* The iterative function calculates the Fibonacci sequence by iterating over each index up to n and summing the two 
* previous numbers in the sequence.
*
* The recursive function solves the same problem through recursion, calling itself with n-1 and n-2 until reaching the 
* base case (n=0 or n=1).
*
* The dynamic programming function uses recursion and memoization to store values in an array.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
Iterative function to calculate the fibonacci series.
*/ 

long long int fibonacci_iterative_c(int n, int print_level) {

    // initialize the first two numbers
    long long int a = 0, b = 1;  
    
    // print first num if print level 2
    if (print_level > 1)
        printf("%lld ", a);
    
    // loop through fib nums to calculate next n
    for (int i = 0; i < n; i++) {
        long long int temp = a;
        a = b; 
        b = temp + b; 
        
        // print each number if print level 2
        if (print_level > 1)
            printf("%lld ", a);
    }
    
    // print only n if print level 1
    if (print_level == 1)
        printf("%lld\n", a);
    
    return a;
}

/**
Recursive function to calculate the fibonacci series.
*/ 
long long int fibonacci_recursive_c(int n, int print_level) {
    
    // base case
    if (n <= 1) {
        if (print_level > 0)
            printf("%d\n", n);
        return n;
    }
    
    // recursive step
    long long int result = fibonacci_recursive_c(n - 1, print_level) + fibonacci_recursive_c(n - 2, 0);
    
    if (print_level == 1 && n == print_level)
        printf("%lld\n", result);
    
    return result;
}

/**
Helper function for dynamic programming approach
*/
long long int fibonacci_dynamic_programming_c_helper(int n, long long int* dparray, int print_level) {
    
    // If the value is already calculated, return it from array
    if (dparray[n] != -1) {
        return dparray[n];
    }
    
    // Base case
    if (n <= 1) {
        dparray[n] = n;
        if (print_level == 2) {
            printf("%lld ", dparray[n]);
        }
        return n;
    }
    
    // Calculate the nth Fibonacci number and store it in the array
    dparray[n] = fibonacci_dynamic_programming_c_helper(n - 1, dparray, print_level) + 
            fibonacci_dynamic_programming_c_helper(n - 2, dparray, print_level);
    
    // print each number if print level 2
    if (print_level == 2) {
        printf("%lld ", dparray[n]);
    }
    
    return dparray[n];
}

/**
Dynamic programming function to calculate the fibonacci series
*/
long long int fibonacci_dynamic_programming_c(int n, int print_level) {

    // allocate memory for dp array
    long long int* dparray = (long long int*) malloc((n+1) * sizeof(long long int));

    // initialize dp array to -1
    for(int i = 0; i <= n; i++) {
        dparray[i] = -1;
    }

    // call the helper function to calculate n
    long long int result = fibonacci_dynamic_programming_c_helper(n, dparray, print_level);

    // free mem
    free(dparray);

    return result;
}
/*
*A test function to be called in the main function when program runs.
*/
void tests() {

    printf("Testing the iterative function with input 10...\n");
    long long int result = fibonacci_iterative_c(10, 1);
    printf("Output: %lld\n", result);
    printf("Expected output: 55\n");

    printf("Testing the recursive function with input 10...\n");
    result = fibonacci_recursive_c(10, 1);
    printf("Output: %lld\n", result);
    printf("Expected output: 55\n");

    printf("Testing the dynamic programming function with input 10...\n");
    result = fibonacci_dynamic_programming_c(10, 1);
    printf("Output: %lld\n", result);
    printf("Expected output: 55\n");

    printf("Testing the iterative function with input 5 and print_level 2...\n");
    fibonacci_iterative_c(5, 2);
    printf("Expected output: 0 1 1 2 3 5\n");

    printf("Testing the dynamic programming function with input 5 and print_level 2...\n");
    fibonacci_dynamic_programming_c(5, 2);
    printf("Expected output: 0 1 1 2 3 5\n");

}

int main(int argc, char* argv[]) {

    // Check for test as arg when running.
    if (argc > 1 && strcmp(argv[1], "test") == 0) {
        tests();
        return 0;
    }    

    // convert first argument to an int
    int n = atoi(argv[1]);  

    // algorithm to use
    char* algo = argv[2];   

    // convert 3rd arg to int
    int print_level = atoi(argv[3]);  
    long long int result;

    // array to store numbers
    long long int dparray[n + 1];  

    // initialize array with i of -1
    for (int i = 0; i <= n; i++) {
        dparray[i] = -1;
    }

    // call function based on algorithm
    if (strcmp(algo, "iterative") == 0) {
        result = fibonacci_iterative_c(n, print_level);
    }
    else if (strcmp(algo, "recursive") == 0) {
        result = fibonacci_recursive_c(n, print_level);
    }
    else if (strcmp(algo, "dp_recursive") == 0) {
        result = fibonacci_dynamic_programming_c(n, print_level);
    }
    else {
        printf("Invalid algorithm choice.\n");
        return 1;
    }

    printf("%lld\n", result);

    return 0;
}
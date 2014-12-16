# # The many ways to do Fibonacci in Python, as seen below.

# NOTE: UNCOMMENT EACH SOLUTION TO RUN IT - TRYING TO RUN
# ALL OF THEM AT ONCE WILL RETURN ERRORS

# # 1. This is a simple recursive form which translates 
# # easily from the universal formula for fibonacci.
# # As with option #1, this also calculates the total.

# def Fibonacci(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return Fibonacci(n-1)+Fibonacci(n-2)

# print Fibonacci(3)

# # 2. This is a recursive version which will give you 
# # the amount of fibonacci numbers requested (so for 
# #	example, if you request 10, it will give you the first
# # ten numbers of the fibonacci sequence.) 

# def Fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return(Fibonacci(n-1) + Fibonacci(n-2))

# n_terms = int(raw_input("How many fibonacci numbers would you like? "))

# print("Fibonacci sequence:")
# for i in range(n_terms):
# 	print(Fibonacci(i))

# 3. Iterative solution which calculates fibonacci numbers up to the
# nth number.

# def Fibonacci(n):
#     current = 1
#     old = 1
#     i = 1 # range of numbers from i-n, starting with 1
#     while (i < n):
#         current, old, i = current + old, current, i + 1
#     return current

# print("Fibonacci sequence:")
# for i in range(10): # The input
#     print(Fibonacci(i))

# # 4. This is the simplest and fastest way to calculate
# # the TOTAL in python, though not the most readable.

# from math import sqrt 

# def Fibonacci(n):
#     return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# print Fibonacci(5)    
# print Fibonacci(10)
# print Fibonacci(20)

# 5. Is fibonacci calculator - returns True or False for if a 
# given number is within the fibonacci sequence

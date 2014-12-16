# OPTION 1 (the version I came up with)

def product(numlist):
    total = 1
    for num in numlist:
        total *= num
    return total

# OPTION 2 (from Stack Overflow)  utilizes lambdas!

def product(numlist):
	produced = reduce(lambda x, y: x*y, numlist)
	return produced

# OPTION 3 - requires import

import operator

def product(numlist):
	multiplied = reduce(operator.mul, numlist, 1)
	return multiplied

# DRIVER CODE

print product([5, 3, 4]) # should return 60

"""
Fizzbuzz in Python: 
1) Print numbers 1 through 100
2) For multiples of three print "Fizz" 
3) For multiples of five print "Buzz" 
4) For multiples of three and five print "Fizzbuzz"
"""

# 1) Fizzbuzz with an if statement

# fzbz_ary = range(1, 101)

# for x in fzbz_ary: 
# 	if x % 5 == 0 and x % 3 == 0:
# 		print("FizzBuzz")
# 	elif x % 5 == 0:
# 		print("Buzz")
# 	elif x % 3 == 0:
# 		print("Fizz")
# 	else:
# 		print(x)

# 2: FizzBuzz with a switch statement --
# Python does not have a case/switch statement,
# so nothing is here

# 3: FizzBuzz with classes and modules

class FizzBuzz:
	def __init__(num):
		for x in num:
			num % 5 == 0 and num % 3 == 0
			print "FizzBuzz"
			num % 5 == 0
			print "Buzz"
			num % 3 == 0
			print "Fizz"
			num
			print "#{num}"

# class FizzBuzzer:
# 	def process(array):

# 			x = FizzBuzz.new(x)


one_hundred = range(1, 101)
fizzbuzz = FizzBuzz(one_hundred)
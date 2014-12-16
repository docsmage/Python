# Write code that takes an integer (N) and returns the amount of
# different pairs (the length of the pair K) 
# that an array of that number can produce.

# Example: N = 5, K = 2 would produce 3 because there are 3
# potential pairs in N (5,3) (4,2) and (3,1). 
# Note that the pairs cannot be comprised of numbers that touch
# each other!

# PSEUDOCODE
# 1) Take integer N and divide it into an array of numbers counting
# up from 1 to N.
# 2) Iterate over the array
# 2a. For each value in the array, calculate the amount of digits
# not touching it

def PairCalculator(N,K):
# 	H=range(1,N+1)
# # 	ans = sum(1 for a in N if a-k in H) # something from stackoverflow
# # 	print ans # something from stackoverflow

# 	H=set() # more from stackoverflow
# 	ans=0
# 	for a in H: 
# 	  H.add(a)
# 	for a in A: 
# 	  if a-k in H: 
# 	    ans+=1
# 	print ans

	temp = input()
	temp = temp.split(" ")
	N = int(temp[0])
	K = int(temp[1])
	num_array = input()
	num_array = num_array.split(" ")
	diff = 0
	pairs= 0
	i = 0
	while(i < N):
	    num_array[i] = int(num_array[i])
	    i += 1
	while(num_array != []):    
	    j = 0
	    while(j < (len(num_array)-1)):
	        diff = abs(num_array[j+1] - num_array[0])
	        if(diff == K):
	            pairs += 1
	        j += 1
	    del num_array[0]
	    if(len(num_array) == 1):
	        break
	print(pairs)

# DRIVER code

PairCalculator(5,2) # ==> 3
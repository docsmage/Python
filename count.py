def count(sequence, item):
	amt = 0
	for i in sequence:
		if i == item:
			amt += 1
	return amt		

print count([1,1,2,1], 1)
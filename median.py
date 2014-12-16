def median(inp):
    inp.sort()
    if len(inp)%2==0:
       return (inp[len(inp)/2]+inp[len(inp)/2-1])/2.0
    else:
        return inp[len(inp)/2]

print median([3,1,2]) # should return 2
print median([4, 9, 14, 5, 2]) # should return 5
print median([1]) # should return 1
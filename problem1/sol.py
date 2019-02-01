# Use set to exclude repeated values
s = set(range(0,1000,3))
s.update(set(range(0,1000,5)))
print(sum(s))

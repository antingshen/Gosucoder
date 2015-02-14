from random import *
n = 5000
print n
for i in range(n):
	print "%s %s %s" % (
		choice(["<", ">", "="]), 
		randint(1, 100000), 
		choice(["yes", "no"]))

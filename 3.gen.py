from random import random
N = 2
M = 5
print "%d %d" % (N, M)
for _ in range(N):
	print "%.4f %.4f" % (random() * 1000, random() * 1000)
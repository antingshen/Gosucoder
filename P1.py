from __future__ import division
import sys

def solve():
	start, lower, upper = map(float, sys.stdin.readline().split(' '))
	wins = 0
	losses = 0
	curr = start
	while curr <= upper:
		wins += 1
		curr *= 1.5
	curr = start
	while curr >= lower:
		losses += 1
		curr /= 1.5
	if wins < losses:
		print "Player fortune"
		return
	if wins > losses:
		print "Player ruin"
		return
	print "A fair game"
	return


num_cases = input()
for _ in range(num_cases):
	solve()

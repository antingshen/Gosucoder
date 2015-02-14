from __future__ import division
import sys

def solve():
	start, lower, upper = map(float, sys.stdin.readline().split(' '))
	cache = {}

	stack = [round(start, 4)]

	while stack:
		last = stack[-1]
		if last in cache:
			stack.pop()
			continue
		next_win = round(last * 1.5, 4)
		next_loss = round(last * 2 / 3, 4)

		flag = False
		if next_win <= upper and next_win not in cache:
			stack.append(next_win)
			flag = True
		if next_loss >= lower and next_loss not in cache:
			stack.append(next_loss)
			flag = True

		if flag:
			continue

		prob = cache.get(next_win, 1) + cache.get(next_loss, 0)
		prob /= 2
		cache[last] = prob
		
	result = cache[round(start, 4)]

	if result > 0.5001:
		print "Player fortune"
		return
	if result < 0.4999:
		print "Player ruin"
		return
	print "A fair game"
	return

num_cases = input()
for _ in range(num_cases):
	solve()

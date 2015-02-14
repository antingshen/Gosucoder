import sys
import re

regex = re.compile(r'^([<>=]) ?(\d+) ?(yes|no).*$')

num_hints = int(sys.stdin.readline())
hints = []
sorted_hints = set()
for _ in xrange(num_hints):
	match = regex.match(sys.stdin.readline())
	if match is None:
		continue
	sign, num, truthy = match.groups()
	num = int(num)
	truthy = truthy == "yes"
	hints.append((num, sign, truthy))
	sorted_hints.add(num)

sorted_hints = sorted(list(sorted_hints))
sorted_hints.append(sys.maxint)
sorted_hints.append(sys.maxint)

minimum = sys.maxint
n = 1
for new_n in sorted_hints:
	max_run = 0
	cur_run = 0
	for number, sign, truthy in hints:
		if sign == "<":
			lie = (n < number) != truthy
		elif sign == ">":
			lie = (n > number) != truthy
		else:
			lie = (n == number) != truthy
		if lie:
			cur_run += 1
		else:
			max_run = max(max_run, cur_run)
			cur_run = 0
	max_run = max(max_run, cur_run)
	n = new_n
	minimum = min(minimum, max_run)

print minimum

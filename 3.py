from random import random
N, M = map(int, raw_input().split())

directions = ((1, 1), (1, 0), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 1), (-1, 0), (-1, -1))

DIVISION = 10
ITERS = 50
current = [[[]]*DIVISION]*DIVISION

def dist(x, y):
	return (x[1]-y[1])*(x[1]-y[1]) + (x[0]-y[0])*(x[0]-y[0])

for _ in xrange(N):
	point = tuple(map(float, raw_input().split()))
	x, y = int(point[0]*DIVISION/1000), int(point[1]*DIVISION/1000)
	current[min(x, DIVISION-1)][min(y, DIVISION-1)].append(point)

for _ in range(M):
	max_dist = 0
	for _ in range(ITERS):
		point = (random()*1000, random()*1000)
		x, y = int(point[0]*DIVISION/1000), int(point[1]*DIVISION/1000)
		closest_dist = float('inf')
		# closest_neighbor = None # TODO
		for x_offset, y_offset in directions:
			new_x = x_offset + x
			new_y = y_offset + y
			if new_x < 0 or new_x >= DIVISION or new_y < 0 or new_y >= DIVISION:
				continue
			for pt in current[new_x][new_y]:
				d = dist(point, pt)
				if d < closest_dist:
					closest_dist = d
					# closest_neighbor = ??
		if closest_dist > max_dist:
			max_dist = closest_dist
			best_pt = point

	x, y = int(best_pt[0]*DIVISION/1000), int(best_pt[1]*DIVISION/1000)
	current[x][y].append(best_pt)
	print "%f %f" % best_pt

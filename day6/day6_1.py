grid = [x.strip() for x in open("day6.in").readlines()]

dim = (len(grid), len(grid[0]))
(row,col) = [(i, j) for i in range(dim[0]) for j in range(dim[1]) if grid[i][j] == "^"][0]
obs = [(i, j) for i in range(dim[0]) for j in range(dim[1]) if grid[i][j] == "#"]


def destinationFromObstacle(orient, obstacles, current, dim_max):
	less = orient in ["UP", "LEFT"]

	extreme = max if less else min
	filt = (lambda x: x< current) if less else (lambda x: x>current)
	offset = +1 if less else -1
	exit_max = 0 if less else dim_max

	obstacles = [o for o in obstacles if filt(o)]
	return (extreme(obstacles) + offset, False) if obstacles else (exit_max, True)

def nextLoc(row, col, orient):
	horizontal = orient in ["LEFT", "RIGHT"]

	obstacles = [c[1] for c in obs if c[0] == row] if horizontal else [r[0] for r in obs if r[1] == col]

	destination, exited = destinationFromObstacle(orient, obstacles, 
		col if horizontal else row,
		dim[1]-1 if horizontal else dim[1]-1)			

	return (row, destination, exited) if horizontal else (destination, col, exited)

visited = set()
for orientation in ["UP","RIGHT","DOWN","LEFT"]*100000:
	r,c,exited = nextLoc(row,col,orientation)
	visited.update((i,j) 
		for i in range(min(r,row),max(r,row)+1) 
		for j in range(min(c,col),max(c,col)+1))
	if exited: break
	row,col = r,c

print(len(visited))


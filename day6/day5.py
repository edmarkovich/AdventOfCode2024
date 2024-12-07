grid = [x.strip() for x in open("day6.in").readlines()]

dim = (len(grid), len(grid[0]))
(row,col) = [(i, j) for i in range(dim[0]) for j in range(dim[1]) if grid[i][j] == "^"][0]
obs = [(i, j) for i in range(dim[0]) for j in range(dim[1]) if grid[i][j] == "#"]


def destinationFromObstacle(orient, obstacles, current, dim_max):
	if orient in ["UP", "LEFT"]:
		extreme = max
		filt = lambda x: x< current
		offset = +1
		exit_max = 0
	else:
		extreme = min
		filt = lambda x: x>current
		offset = -1
		exit_max = dim_max-1

	obstacles = [o for o in obstacles if filt(o)]
	if obstacles:
		return extreme(obstacles) + offset

	return exit_max


def nextLoc(row, col, orient):
	exited = False
	if orient in ["LEFT", "RIGHT"]:
		obstacles = [c[1] for c in obs if c[0] == row]
		filt= col
		exit_max = dim[1]
	else: 
		obstacles = [r[0] for r in obs if r[1] == col]
		filt = row
		exit_max = dim[0]

	destination = destinationFromObstacle(orient, obstacles, filt, exit_max)	
	if destination in [0, exit_max-1]:
		exited = True
				
	if orient in ["LEFT", "RIGHT"]:
		return (row, destination, abs(destination-col), exited)
	else:
		return (destination, col, abs(destination-row), exited)
		


moves = 1
visited = set()
for orientation in ["UP","RIGHT","DOWN","LEFT"]*100000:
	(r,c,m,exited) = nextLoc(row,col,orientation)
	moves +=m
	#print(r,c,m,moves,exited)
	
	for i in range(min(r,row),max(r,row)+1):
		for j in range(min(c,col),max(c,col)+1):
			visited.add((i,j))

	row = r
	col = c	


	if exited: break
print(moves)
print(len(visited))


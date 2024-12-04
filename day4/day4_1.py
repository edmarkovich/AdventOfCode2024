import itertools
formuli = list(itertools.product([-1,0,1], repeat=2))
formuli.remove((0,0))
grid = open("day4.in").readlines()

def checkOneFormula(i,j, formula):
	for l in "XMAS":
		if i < 0 or j < 0: return 0
		if i >= len(grid) or j >= len(grid[i]): return 0
		if grid[i][j] != l: return 0
		i += formula[0]
		j += formula[1]
	return 1

def checkMatches(i,j):
	out = 0
	for f in formuli:
		res = checkOneFormula(i,j,f)
		#print(i,j,res, f)
		out += res
	return out

matches = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		matches += checkMatches(i,j)

print(matches)


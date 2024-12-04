import itertools
grid = open("day4.in").readlines()

formula1 = [(1,1),(-1,-1)]
formula2 = [(1,-1),(-1,1)]

def checkOneFormula(i,j, formula):
	for l in "MAS":
		if i < 0 or j < 0: return None 
		if i >= len(grid) or j >= len(grid[i]): return None
		if grid[i][j] != l: return None
		if grid[i][j] == 'A': out = (i,j)
		i += formula[0]
		j += formula[1]
	return out

def checkMatches(i,j, formuli):
	q = ([checkOneFormula(i,j,f) for f in formuli])
	return [q for q in q if q is not None]

m1=[]
m2=[]
for i in range(len(grid)):
	for j in range(len(grid[i])):
		m1 += checkMatches(i,j, formula1)
		m2 += checkMatches(i,j, formula2)

print( len ( set(m1) & set(m2)))


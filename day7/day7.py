from itertools import product

def parseLine(line):
	first,rest = line.split(":")
	return int(first), [int(x) for x in rest.split()]

def permute(target, ints):
	for operations in [p for p in product("+*|", repeat=len(ints)-1)]:
		total = ints[0]
		for o in range(len(operations)):
			if operations[o]=="+": total += ints[1+o]
			elif operations[o]=="*": total *= ints[1+o]
			elif operations[o]=="|": total = int(str(total)+str(ints[1+o]))
		if total == target: return True
	return False

out = 0
count=0
for line in [parseLine(x) for x in open("day7.in").readlines()]:
	count +=1
	print(count)
	if permute(line[0], line[1]): out += line[0]
print(out)

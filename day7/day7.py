from itertools import product
import operator

ops = [operator.add, operator.mul, lambda x,y: int(str(x)+(str(y)))]

def parseLine(line):
	first,rest = line.split(":")
	return int(first), [int(x) for x in rest.split()]

def permute(target, ints):
	for operations in [p for p in product(ops, repeat=len(ints)-1)]:
		total = ints[0]
		for o in range(len(operations)):
			total=operations[o](total, ints[1+o])
		if total == target: return True
	return False

def do():
	lines = [parseLine(x) for x in open("day7.in").readlines()]
	out = sum([line[0] for line in lines if permute(line[0], line[1])])
	print(out)

do()

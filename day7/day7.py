import operator
from itertools import product
from functools import reduce

ops = [operator.add, operator.mul, lambda x,y: int(str(x)+(str(y)))]

def parseLine(line):
	first,rest = line.split(":")
	return int(first), [int(x) for x in rest.split()]

def permute(target, ints):
	for operations in [p for p in product(ops, repeat=len(ints)-1)]:
		total = reduce(lambda x,y: (None, y[0](x[1],y[1])), zip((None,)+operations, ints))
		if total[1] == target: return True
	return False

lines = [parseLine(x) for x in open("day7.in").readlines()]
print(sum([line[0] for line in lines if permute(line[0], line[1])]))


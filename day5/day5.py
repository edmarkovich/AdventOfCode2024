import math

lines = open("day5.in").readlines()

rules = [x.strip().split("|") for x in lines if "|" in x]
pages = [x.strip().split(",") for x in lines if "," in x]

def checkRulePattern(rule, pattern):
	if rule[0] not in pattern or rule[1] not in pattern: return True
	return pattern.index(rule[0]) < pattern.index(rule[1])

out = 0
for p in pages:
	if False in [checkRulePattern(r,p) for r in rules]: continue

	idx = math.floor(len(p)/2)
	out += int(p[idx])

print(out)
			


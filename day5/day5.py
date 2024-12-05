import math

lines = open("day5.in").readlines()

rules = [x.strip().split("|") for x in lines if "|" in x]
pages = [x.strip().split(",") for x in lines if "," in x]

def checkRulePattern(rule, pattern, fix=False):
	if rule[0] not in pattern or rule[1] not in pattern: return True
	if pattern.index(rule[0]) < pattern.index(rule[1]): return True

	if fix:
		el = pattern.pop(pattern.index(rule[0]))
		pattern.insert(pattern.index(rule[1]),el)

	return False

out = 0
for p in pages:
	if not False in [checkRulePattern(r,p) for r in rules]: continue
	while False in [checkRulePattern(r,p, True) for r in rules]: 
		pass

	idx = math.floor(len(p)/2)
	out += int(p[idx])

print(out)
			


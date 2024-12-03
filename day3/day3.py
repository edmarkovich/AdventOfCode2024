import re


def do_mult(instruction):
    pattern =r"(\d+)"
    matches = [int(x) for x in re.findall(pattern, instruction)]
    return matches[0] * matches[1]

with open("day3.in","r") as f:
    line = f.read().replace('\n','')

ignore = r"don't\(\)(.+?)(do\(\)|$)"
line = re.sub(ignore,"", line)

pattern = r"(mul\(\d+,\d+\))"
matches = [do_mult(x) for x in re.findall(pattern,line)]

print( sum(matches))

import re

def do_mult(instruction):
    matches = [int(x) for x in re.findall(r"(\d+)", instruction)]
    return matches[0] * matches[1]

line = open("day3.in").read().replace("\n","")
line = re.sub(r"don't\(\)(.+?)(do\(\)|$)","", line)

matches = [do_mult(x) for x in re.findall(r"(mul\(\d+,\d+\))",line)]
print(sum(matches))

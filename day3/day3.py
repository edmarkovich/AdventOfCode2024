import re


def do_mult(instruction):
    pattern =r"(\d+)"
    matches = re.findall(pattern, instruction)
    matches = list(map(lambda x: int(x), matches))
    return matches[0] * matches[1]

with open("day3.in","r") as f:
    total=0
    lines = f.readlines()
    pattern = r"(mul\([0-9]+,[0-9]+\))"
    for line in lines:
        matches = re.findall(pattern,line)
        matches = map(lambda x: do_mult(x), matches)
        total += sum(matches)

    print(total)
    

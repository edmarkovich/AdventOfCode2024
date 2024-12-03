import re


def do_mult(instruction):
    pattern =r"(\d+)"
    matches = re.findall(pattern, instruction)
    matches = list(map(lambda x: int(x), matches))
    return matches[0] * matches[1]

with open("day3.in","r") as f:
    total=0
    lines = f.read().replace('\n','')
    pattern = r"(mul\([0-9]+,[0-9]+\))"
    ignore = r"don't\(\)(.+?)do\(\)"
    ignore_eol = r"don't\(\)(.+?)$"
    line = lines
    line = re.sub(ignore,"", line)
    line = re.sub(ignore_eol,"", line)
    matches = re.findall(pattern,line)
    matches = map(lambda x: do_mult(x), matches)
    total += sum(matches)

    print(total)
    

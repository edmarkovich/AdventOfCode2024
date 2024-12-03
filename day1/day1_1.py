

def getLists():
    with open("day1.in","r") as f:
        lines = f.readlines()

    pairs = map(lambda x: [int(y) for y in x.split()], lines)
    return zip(*pairs)


[col1, col2] = getLists()
out = sum([abs(x-y) for x,y in zip(sorted(col1),sorted(col2))])
print(out)


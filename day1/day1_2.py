

def getLists():
    with open("day1.in","r") as f:
        lines = f.readlines()

    pairs = map(lambda x: [int(y) for y in x.split()], lines)
    return zip(*pairs)


[col1, col2] = getLists()
sim = map(lambda x: x * col2.count(x), col1)
print(sum(sim))



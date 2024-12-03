def safeReport(report):
    lvl_diffs = [abs(report[i] - report[i-1]) for i in range (1, len(report))]
    if min(lvl_diffs) < 1 or max(lvl_diffs)>3: return False
    return report == sorted(report) or report == sorted(report, reverse=True)


with open("day2.in","r") as f:
    lines = f.readlines()
    lines = map(lambda x: [int(y) for y in x.split()], lines)
    lines = map(safeReport, lines)
    lines = sum(lines)

print(lines)




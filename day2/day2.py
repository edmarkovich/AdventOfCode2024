def safeReport_helper(report):
    lvl_diffs = [abs(report[i] - report[i-1]) for i in range (1, len(report))]
    if min(lvl_diffs) < 1 or max(lvl_diffs)>3: return False
    return report == sorted(report) or report == sorted(report, reverse=True)

def safeReport(report):
    if safeReport_helper(report): return True

    for i in range(len(report)):
        subReport = report[:i] + report[i+1:]
        if safeReport_helper(subReport): return True

    return False

with open("day2.in","r") as f:
    lines = f.readlines()
    lines = map(lambda x: [int(y) for y in x.split()], lines)
    lines = map(safeReport, lines)
    lines = sum(lines)

print(lines)




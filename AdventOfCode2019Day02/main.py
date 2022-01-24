
import day02
import sys
from timeit import default_timer as timer

lines = sys.stdin.readlines()
print("Read", len(lines), "lines")
day02 = day02.Day02(lines)

start1 = timer()
part1 = day02.solve_part_1(True)
end1 = timer()
print("Part 1 results is", part1, "in", end1 - start1, "seconds")

start2 = timer()
part2 = day02.solve_part_2()
end2 = timer()
print("Part 2 results is", part2, "in", end2 - start2, "seconds")
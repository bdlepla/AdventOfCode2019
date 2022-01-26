
import day05
import sys
from timeit import default_timer as timer

lines = sys.stdin.readlines()
print("Read", len(lines), "lines")
day05 = day05.Day05(lines)

start1 = timer()
part1 = day05.solve_part_1_output()
end1 = timer()
print("Part 1 results is", part1, "in", end1 - start1, "seconds")

start2 = timer()
part2 = day05.solve_part_2_output()
end2 = timer()
print("Part 2 results is", part2, "in", end2 - start2, "seconds")
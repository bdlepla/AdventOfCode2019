
import day06
import sys
from timeit import default_timer as timer

lines = sys.stdin.readlines()
print("Read", len(lines), "lines")
day06 = day06.Day06(lines)

start1 = timer()
part1 = day06.solve_part1()
end1 = timer()
print("Part 1 results is", part1, "in", end1 - start1, "seconds")

start2 = timer()
part2 = day06.solve_part2()
end2 = timer()
print("Part 2 results is", part2, "in", end2 - start2, "seconds")
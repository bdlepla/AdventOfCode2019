
import day04
import sys
from timeit import default_timer as timer

#lines = sys.stdin.readlines()
lines = ["108457-562041"]
print("Read", len(lines), "lines")
day04 = day04.Day04(lines)

start1 = timer()
part1 = day04.solve_part_1()
end1 = timer()
print("Part 1 results is", part1, "in", end1 - start1, "seconds")

start2 = timer()
part2 = day04.solve_part_2()
end2 = timer()
print("Part 2 results is", part2, "in", end2 - start2, "seconds")
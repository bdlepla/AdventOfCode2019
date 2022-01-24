from ntpath import join


class Day01:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines

    def solve_part_1(self) -> int:
        return self.solve()

    def solve_part_2(self) -> int:
        return self.solve(True)

    def solve(self, account_for_fuel=False) -> int:
        #print(self.lines)
        trimmed_strings = [s.strip() for s in self.lines]
        #print(trimmed_strings)
        numbers = [int(s) for s in trimmed_strings]
        fuel_costs = [self.fuel_cost(i) for i in numbers]
        if (account_for_fuel):
            fuel_costs = [self.recursive_fuel_cost(i) for i in fuel_costs]

        #print(fuel_costs)
        return sum(fuel_costs)
        
    def fuel_cost(self, number):
        return number // 3 - 2

    def recursive_fuel_cost(self, number):
        if (number < 1): return 0
        this_fuel_cost = self.fuel_cost(number)
        return number + self.recursive_fuel_cost(this_fuel_cost)


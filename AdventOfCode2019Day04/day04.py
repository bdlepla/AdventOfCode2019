class Day04:
    def __init__(self, lines):
        self.lines = lines

    def solve_part_1(self):
        return self.solve()

    def solve(self, strict=False):
        min = int(self.lines[0][0:6])
        max = int(self.lines[0][7:])
        number_of_matches = 0
        for number in range(min, max-1):
            matched = self.meets_requirements(number, strict)
            if matched:
                number_of_matches += 1

        return number_of_matches

    def solve_part_2(self):
        return self.solve(True)

    def meets_requirements(self, password, strict=False):
        str_password = str(password)
        if not self.meets_increasing_requirement(str_password): 
            return False

        digit_counts = self.count_digits(str_password)
        for key, value in digit_counts.items():
            if strict:
                if value == 2: return True
            elif value > 1: return True

        return False

    def count_digits(self, str_password):
        ret = {}
        for c in str_password:
            count = 1
            if c in ret: count = ret[c]+1
            ret[c] = count

        return ret

      

    def meets_increasing_requirement(self, str_password):
        last_c = str_password[0]
        for c in str_password[1:]:
            if (c < last_c): return False
            last_c = c
        return True



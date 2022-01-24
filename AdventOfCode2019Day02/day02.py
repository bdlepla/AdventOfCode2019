import opcode


class Day02:
    def __init__(self, lines):
        self.positions = list(map(lambda s: int(s), lines[0].split(",")))

    def solve_part_1(self, modify=False):
        return self.solve(modify)[0]

    def solve_part_2(self):
        for noun in range(100):
            for verb in range(100):
                positions = self.positions[::]
                positions[1] = noun
                positions[2] = verb
                solved = self.solve_with_positions(positions)[0]
                print("noun", noun, "verb", verb, "solved", solved)
                if (19690720 == solved):
                    return noun * 100 + verb

        return 0

    def solve(self, modify=False):
        positions = self.positions[::]
        if modify:
            positions[1] = 12
            positions[2] = 2
        return self.solve_with_positions(positions)

    def solve_with_positions(self, positions):
        position = 0
        while (True):
            opcode = positions[position]
            if (99 == opcode): break
            try:
                pos1 = positions[position+1]
                operand1 = positions[pos1]
                pos2 = positions[position+2]
                operand2 = positions[pos2]
                destination = positions[position+3]
                position += 4
            except:
                break

            if opcode == 1:  
                positions[destination] = operand1 + operand2
            elif opcode == 2:
                positions[destination] = operand1 * operand2
            else:
                break 

        return positions
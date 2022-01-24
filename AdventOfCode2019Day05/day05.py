
class Day05:
    def __init__(self, lines):
        self.positions = list(map(lambda s: int(s), lines[0].split(",")))
        self.input = 1
        self.output = []

    def solve_part_1(self, modify=False):
        return self.solve(modify)[0]

    def solve_part_2(self):
        for noun in range(100):
            for verb in range(100):
                positions = self.positions[::]
                positions[1] = noun
                positions[2] = verb
                solved = self.solve_with_positions(positions)[0]
                #print("noun", noun, "verb", verb, "solved", solved)
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

            if 99 == opcode: break

            if 1 <= opcode <= 2:
                operand1 = self.get_reference(positions, position+1)
                operand2 = self.get_reference(positions, position+2)
                destination = positions[position+3]
                result = operand1 * operand2 if opcode == 2 else operand1 + operand2
                positions[destination] = result
                position += 4  
                continue

            if 3 == opcode:
                destination = positions[position+1]
                positions[destination] = self.input
                position += 2
                continue

            if 4 == opcode:
                value = self.get_reference(positions, position+1)
                self.output.append(value)
                position += 2
                continue

            special_opcode = opcode % 100
            if 1 <= special_opcode <= 2:
                mode1 = (opcode // 100) % 10
                val1 = self.get_reference(positions, position+1, mode1)
                mode2 = (opcode // 1000) % 10
                val2 = self.get_reference(positions, position+1, mode2)
                destination = positions[position+3]
                result = val1 * val2 if 2 == special_opcode else val1 + val2
                positions[destination] = result
                position += 4
                continue

            if 1 == opcode % 100:
                mode1 = (opcode // 100) % 10
                val1 = self.get_reference(positions, position+1, mode1)
                mode2 = (opcode // 1000) % 10
                val2 = self.get_reference(positions, position+1, mode2)
                destination = positions[position+3]
                positions[destination] = val1 + val2
                position += 4
                continue
                
            else:
                break 

        return positions

    def get_reference(self, positions, at, mode=0):
        if (0 == mode):
            return positions[positions[at]]
        else:
            return positions[at]


class Day05:
    def __init__(self, lines):
        self.positions = list(map(lambda s: int(s), lines[0].split(",")))
        self.output = []

    def solve_part_1_output(self):
        self.input = 1
        self.solve_part_1()
        return self.output[-1]

    def solve_part_2_output(self):
        self.input = 5
        self.solve_part_2()
        return self.output[-1]

    def solve_part_1(self):
        return self.solve()[0]

    def solve_part_2(self):
       return self.solve()[0]

    def solve(self):
        positions = self.positions[::]
        return self.solve_with_positions(positions)

    def solve_with_positions(self, positions):
        position = 0
        while (True):
            operation = positions[position]
            opcode = operation % 100
            mode1 = (operation // 100) % 10 
            mode2 = (operation // 1000) % 10
            
            if 1 <= opcode <= 2:
                operand1 = self.get_reference(positions, position+1, mode1)
                operand2 = self.get_reference(positions, position+2, mode2)
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

            if  5 == opcode:
                operand1 = self.get_reference(positions, position+1, mode1)
                if operand1:
                    position = self.get_reference(positions, position+2, mode2)
                else:
                    position += 3
                continue
                
            if 6 == opcode:
                operand1 = self.get_reference(positions, position+1, mode1)
                if not operand1:
                    position = self.get_reference(positions, position+2, mode2)
                else:
                    position += 3
                continue

            if 7 == opcode:
                operand1 = self.get_reference(positions, position+1, mode1)
                operand2 = self.get_reference(positions, position+2, mode2)
                destination = positions[position+3]
                positions[destination] = 1 if operand1 < operand2 else 0
                position += 4
                continue

            if 8 == opcode:
                operand1 = self.get_reference(positions, position+1, mode1)
                operand2 = self.get_reference(positions, position+2, mode2)
                destination = positions[position+3]
                positions[destination] = 1 if operand1 == operand2 else 0
                position += 4
                continue

            if 99 == opcode: break
                
            else:
               break
                 
        return positions

    def get_reference(self, positions, at, mode=0):
        return positions[at] if (1 == mode) else positions[positions[at]]

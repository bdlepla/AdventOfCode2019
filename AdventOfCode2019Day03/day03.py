
class Day03:
    def __init__(self, lines):
        self.lines = lines

    def solve_part_1(self):
        return self.solve()

    def solve_part_2(self):
        return self.solve2()

    def solve(self):
        points1 = self.points(self.lines[0])
        points2 = self.points(self.lines[1])
        point_set_1 = set(points1)
        point_set_2 = set(points2)
        intersection = point_set_1 & point_set_2
        inter_distance = map(lambda pt: self.manhattan_distance(pt), intersection)
        ret = min(inter_distance)
        return ret

    def solve2(self):
        points1 = self.points(self.lines[0])
        points2 = self.points(self.lines[1])
        point_set_1 = set(points1)
        point_set_2 = set(points2)
        intersection = point_set_1 & point_set_2

        steps = list()
        for point in intersection:
            distance1_to_point = points1.index(point)+1
            distance2_to_point = points2.index(point)+1
            distance = distance1_to_point + distance2_to_point
            steps.append(distance)
        
        ret = min(steps)
        return ret

    def points(self, line):
        ret = list()
        x = 0
        y = 0
        directions = line.split(",")
        for direct in directions:
            where = direct[0]
            amount = int(direct[1:])
            for a in range(amount):
                if where == 'U':
                    y += 1
                elif where == 'D':
                    y -= 1
                elif where == 'L':
                    x -= 1
                else:
                    x += 1
                element = (x,y)
                ret.append(element)
        return ret

    def manhattan_distance(self, point):
        return abs(point[0]) + abs(point[1])

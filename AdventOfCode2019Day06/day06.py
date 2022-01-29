class Day06:
    def __init__(self, lines):
        self.lines = lines
    
    def solve_part1(self):
        map = self.build_orbit_map(self.lines[::])
        return self.count_orbits(map)

    def solve_part2(self):
        map = self.build_orbit_map(self.lines[::])
        key = self.find_starting_key(map)
        you_path = self.find_path(map, "YOU", key, [])
        san_path = self.find_path(map, "SAN", key, [])
        common_parent = self.find_common_parent(you_path, san_path)
        parent_in_you = you_path.index(common_parent)
        you_dist = len(you_path) - parent_in_you - 2
        parent_in_san = san_path.index(common_parent)
        san_dist = len(san_path) - parent_in_san - 2
        return you_dist + san_dist

    def find_path(self, map, name, start, ret):
        ret.append(start)
        if name == start:
            return ret
        for child in map.get(start, []):
            childRet = self.find_path(map, name, child, ret[::])
            if childRet:
                return childRet
                
        return []

    def find_common_parent(self, you:list, san:list):
        reverse_you = you[::]
        reverse_you.reverse()
        for parent in reverse_you:
            if parent in san:
                return parent


    def build_orbit_map(self, lines):
        map = {}
        for l in lines:
            line = l.replace('\n', '')
            splits = line.split(")")
            first = splits[0]
            second = splits[1]
            second_list = map.get(first, [])
            second_list.append(second)
            map[first] = second_list
        return map

    def count_orbits(self, map:dict):
        key = self.find_starting_key(map)
        return self.count_key_orbits(key, 0, map)

    def count_key_orbits(self, key, acc, map:dict):
        ret = acc
        for val in map.get(key, []):
            ret += self.count_key_orbits(val, acc+1, map) 
        return ret

    def find_starting_key(self, map:dict):
        
        """Find the first key that is included in any value list"""
        
        set_of_values = set(self.flatten(map.values()))

        for k in map.keys():
            if k not in set_of_values:
                return k

        
    def flatten(self, list_of_lists):
        ret = []
        for list in list_of_lists:
            ret = ret + list
        return ret


        
        




            


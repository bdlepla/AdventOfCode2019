def test_solve_part_1():
    import day03
    raw_lines = """
        R8,U5,L5,D3
        U7,R6,D4,L4
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day03 = day03.Day03(lines)
    actual = day03.solve_part_1()
    expected = 6
    assert expected == actual

def test_solve_part_1a():
    import day03
    raw_lines = """
        R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
        U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day03 = day03.Day03(lines)
    actual = day03.solve_part_1()
    expected = 135
    assert expected == actual

def test_solve_part_2():
    import day03
    raw_lines = """
        R8,U5,L5,D3
        U7,R6,D4,L4
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day03 = day03.Day03(lines)
    actual = day03.solve_part_2()
    expected = 30
    assert expected == actual

def test_solve_part_2a():
    import day03
    raw_lines = """
        R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
        U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day03 = day03.Day03(lines)
    actual = day03.solve_part_2()
    expected = 410
    assert expected == actual
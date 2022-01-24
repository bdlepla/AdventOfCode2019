
def test_solve_part_1():
    import day05
    raw_lines = """
    1,0,0,0,99
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    actual = day05.solve_part_1()
    expected = 2
    assert expected == actual

def test_solve_part_1a():
    import day05
    raw_lines = """
    1,1,1,4,99,5,6,0,99
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    actual = day05.solve_part_1()
    expected = 30
    assert expected == actual

def test_solve_part_1b():
    import day05
    raw_lines = """
    1,9,10,3,2,3,11,0,99,30,40,50
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    actual = day05.solve_part_1()
    expected = 3500
    assert expected == actual

def test_solve_part_1c():
    import day05
    raw_lines = """
    2,3,0,3,99
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    results = day05.solve()
    actual = results[3]
    expected = 6
    assert expected == actual

def test_solve_part_1d():
    import day05
    raw_lines = """
    2,4,4,5,99,0
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    results = day05.solve()
    actual = results[5]
    expected = 9801
    assert expected == actual

def test_solve_part_1e():
    import day05
    raw_lines = """
    1,1,1,4,99,5,6,0,99
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    results = day05.solve()
    actual = results[4]
    expected = 2
    assert expected == actual

def test_solve_part_1f():
    import day05
    raw_lines = """
        1002,4,3,4,33
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    results = day05.solve()
    actual = results[4]
    expected = 99
    assert expected == actual

def test_solve_part_2():
    import day05
    raw_lines = """
      1,1,1,4,99,5,6,0,99
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day05 = day05.Day05(lines)
    actual = day05.solve_part_2()
    expected = 0
    assert expected == actual
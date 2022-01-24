def test_solve_part_1():
    import day04
    raw_lines = """
        108457-562041
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day04 = day04.Day04(lines)
    actual = day04.solve_part_1()
    expected = 2779
    assert expected == actual

def test_solve_part_1_meets_requirements_1():
    import day04
    day04 = day04.Day04(None)
    actual = day04.meets_requirements(111111)
    expected = True
    assert expected == actual

def test_solve_part_1_meets_requirements_2():
    import day04
    day04 = day04.Day04(None)
    actual = day04.meets_requirements(223450)
    expected = False
    assert expected == actual

def test_solve_part_1_meets_requirements_3():
    import day04
    day04 = day04.Day04(None)
    actual = day04.meets_requirements(123789)
    expected = False
    assert expected == actual


def test_solve_part_2():
    import day04
    raw_lines = """
        108457-562041
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day04 = day04.Day04(lines)
    actual = day04.solve_part_2()
    expected = 1972
    assert expected == actual

def test_solve_part_2_meets_requirements_1():
    import day04
    day04 = day04.Day04(None)
    actual = day04.meets_requirements(112233, True)
    expected = True
    assert expected == actual

def test_solve_part_2_meets_requirements_2():
    import day04
    day04 = day04.Day04(None)
    actual = day04.meets_requirements(123444, True)
    expected = False
    assert expected == actual

def test_solve_part_2_meets_requirements_2():
    import day04
    day04 = day04.Day04(None)
    actual = day04.meets_requirements(111122, True)
    expected = True
    assert expected == actual

def test_solve_part_1():
    import day01
    raw_lines = """
        12
        14
        1969
        100756
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = filter(None, trimmed_lines)
    day01 = day01.Day01(lines)
    actual = day01.solve_part_1()
    expected = 2 + 2 + 654 + 33583
    assert expected == actual

def test_solve_part_2():
    import day01
    raw_lines = """
        12
        14
        1969
        100756
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = filter(None, trimmed_lines)
    day01 = day01.Day01(lines)
    actual = day01.solve_part_2()
    expected = 2 + 2 + 966 + 50346
    assert expected == actual
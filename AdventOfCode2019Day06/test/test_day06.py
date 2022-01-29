def test_solve_part1():
    import day06
    raw_lines = """
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        COM)B
        D)I
        E)J
        J)K
        K)L
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day06 = day06.Day06(lines)
    actual = day06.solve_part1()
    expected = 42
    assert expected == actual

def test_solve_part2():
    import day06
    raw_lines = """
        COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L
        K)YOU
        I)SAN
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    day06 = day06.Day06(lines)
    actual = day06.solve_part2()
    expected = 4
    assert expected == actual
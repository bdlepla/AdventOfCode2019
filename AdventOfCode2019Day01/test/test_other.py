def test_filter1():
    raw_lines = """
        1
        2
        3
        4
        5
    """.split("\n")
    trimmed_lines = map(lambda s: s.strip(), raw_lines)
    lines = list(filter(None, trimmed_lines))
    assert len(lines) == 5
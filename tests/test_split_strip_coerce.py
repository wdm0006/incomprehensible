from incomprehensible import split_strip_coerce


def test_documented_example():
    assert split_strip_coerce('2, red, 3.2, green', ',') == [2, 'red', 3.2, 'green']


def test_coerces_int_float_and_string_with_types():
    result = split_strip_coerce('2, 3.2, red', ',')
    assert result == [2, 3.2, 'red']
    assert [type(x) for x in result] == [int, float, str]


def test_negative_numbers():
    assert split_strip_coerce('-2, -3.2', ',') == [-2, -3.2]


def test_whitespace_is_stripped():
    assert split_strip_coerce('  1  |  a  ', '|') == [1, 'a']


def test_empty_token_stays_a_string():
    result = split_strip_coerce('a,,b', ',')
    assert result == ['a', '', 'b']
    assert all(isinstance(x, str) for x in result)

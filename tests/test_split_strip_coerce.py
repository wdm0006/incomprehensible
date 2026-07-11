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


def test_internal_hyphen_falls_back_to_str():
    # Regression: '1-2' used to raise ValueError instead of coercing to str.
    assert split_strip_coerce('1-2', ',') == ['1-2']
    assert split_strip_coerce('1-2, ok', ',') == ['1-2', 'ok']


def test_partial_date_falls_back_to_str():
    assert split_strip_coerce('2024-01', ',') == ['2024-01']


def test_multiple_dots_falls_back_to_str():
    assert split_strip_coerce('1.2.3', ',') == ['1.2.3']

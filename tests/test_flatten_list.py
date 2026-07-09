from incomprehensible import flatten_list


def test_documented_example():
    # From the docstring "Before/After" block.
    assert flatten_list([1, 2, 3, [4, 'B', 6], {'7': 'A'}]) == [1, 2, 3, 4, 'B', 6, {'7': 'A'}]


def test_flattens_exactly_one_level():
    # Only the outer list layer is spliced; nested lists stay nested.
    assert flatten_list([1, [2, [3, 4]]]) == [1, 2, [3, 4]]


def test_dicts_are_left_intact():
    # Non-list elements (dicts here) pass through unchanged, not flattened.
    assert flatten_list([{'a': 1}, [{'b': 2}]]) == [{'a': 1}, {'b': 2}]


def test_empty_list():
    assert flatten_list([]) == []

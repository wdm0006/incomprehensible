from incomprehensible import dedupe_dictlist


def test_keeps_last_occurrence_and_actual_order():
    # Later duplicates overwrite earlier ones (keeps the LAST per key subset).
    # The returned order follows key-insertion order: the "A_B" key is seen first
    # (row ts:123, later overwritten by ts:125), then "B_B" (row ts:124). So the
    # actual output is [ts:125, ts:124] -- NOT the order shown in the docstring.
    rows = [
        {"ts": 123, "A": "A", "B": "B"},
        {"ts": 124, "A": "B", "B": "B"},
        {"ts": 125, "A": "A", "B": "B"},
    ]
    assert dedupe_dictlist(rows, keys=["A", "B"]) == [
        {"ts": 125, "A": "A", "B": "B"},
        {"ts": 124, "A": "B", "B": "B"},
    ]


def test_no_duplicates_returns_all_rows_in_order():
    rows = [{"A": "x"}, {"A": "y"}]
    assert dedupe_dictlist(rows, keys=["A"]) == [{"A": "x"}, {"A": "y"}]


def test_missing_key_treated_as_empty_string():
    # Rows lacking a dedupe key collapse together on the '' value.
    rows = [{"A": "x", "n": 1}, {"n": 2}, {"n": 3}]
    assert dedupe_dictlist(rows, keys=["A"]) == [{"A": "x", "n": 1}, {"n": 3}]


def test_composite_key_boundaries_are_preserved():
    # ('a_b', 'c') and ('a', 'b_c') are distinct composite identities. A '_'-joined
    # key would collapse both to "a_b_c" and drop a row; a tuple key keeps them apart.
    rows = [
        {"A": "a_b", "B": "c", "id": 1},
        {"A": "a", "B": "b_c", "id": 2},
    ]
    assert dedupe_dictlist(rows, keys=["A", "B"]) == [
        {"A": "a_b", "B": "c", "id": 1},
        {"A": "a", "B": "b_c", "id": 2},
    ]


def test_empty_input():
    assert dedupe_dictlist([], keys=["A"]) == []


def test_int_and_str_with_same_text_are_distinct():
    rows = [{"id": 1, "v": "int-row"}, {"id": "1", "v": "str-row"}]
    assert dedupe_dictlist(rows, keys=["id"]) == rows


def test_bool_and_str_with_same_text_are_distinct():
    rows = [{"id": True, "v": "bool"}, {"id": "True", "v": "str"}]
    assert dedupe_dictlist(rows, keys=["id"]) == rows


def test_unhashable_key_values_do_not_raise_and_still_dedupe():
    rows = [
        {"id": [1, 2], "v": "first"},
        {"id": {"a": 1}, "v": "dict"},
        {"id": [1, 2], "v": "last"},
    ]
    assert dedupe_dictlist(rows, keys=["id"]) == [
        {"id": [1, 2], "v": "last"},
        {"id": {"a": 1}, "v": "dict"},
    ]


def test_missing_key_shares_identity_with_empty_string():
    rows = [{"A": "", "n": 1}, {"n": 2}]
    assert dedupe_dictlist(rows, keys=["A"]) == [{"n": 2}]

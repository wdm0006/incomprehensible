from incomprehensible import dict_pivot


def test_documented_example():
    result = dict_pivot({"ts": 123, "A": "A", "B": "B", "sub": [{"C": 10}, {"C": 8}]}, key="sub")
    assert result == [
        {"ts": 123, "A": "A", "B": "B", "sub.C": 10},
        {"ts": 123, "A": "A", "B": "B", "sub.C": 8},
    ]


def test_one_row_per_pivoted_element():
    result = dict_pivot({"id": 1, "sub": [{"C": 1}, {"C": 2}, {"C": 3}]}, key="sub")
    assert len(result) == 3
    assert [r["sub.C"] for r in result] == [1, 2, 3]


def test_sibling_keys_copied_onto_every_row():
    result = dict_pivot({"id": 1, "tag": "x", "sub": [{"C": 1}, {"C": 2}]}, key="sub")
    assert all(r["id"] == 1 and r["tag"] == "x" for r in result)
    # The pivoted key itself is dropped in favor of the flattened "key.subkey" cols.
    assert all("sub" not in r for r in result)


def test_empty_pivot_list_yields_no_rows():
    assert dict_pivot({"id": 1, "sub": []}, key="sub") == []

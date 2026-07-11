from incomprehensible import get_files


def test_finds_matching_files_recursively(tmp_path):
    (tmp_path / "a.py").write_text("")
    (tmp_path / "b.txt").write_text("")
    nested = tmp_path / "pkg"
    nested.mkdir()
    (nested / "c.py").write_text("")

    found = set(get_files(str(tmp_path), "py"))
    assert found == {str(tmp_path / "a.py"), str(nested / "c.py")}


def test_non_matching_extensions_excluded(tmp_path):
    (tmp_path / "keep.py").write_text("")
    (tmp_path / "skip.md").write_text("")
    (tmp_path / "skip.txt").write_text("")

    assert set(get_files(str(tmp_path), "py")) == {str(tmp_path / "keep.py")}


def test_returns_a_lazy_generator(tmp_path):
    import types

    result = get_files(str(tmp_path), "py")
    assert isinstance(result, types.GeneratorType)


def test_no_matches_yields_nothing(tmp_path):
    (tmp_path / "only.txt").write_text("")
    assert list(get_files(str(tmp_path), "py")) == []

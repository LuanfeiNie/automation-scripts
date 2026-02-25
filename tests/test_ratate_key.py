from scripts.rotate_key import rotate_key

def test_rotate(tmp_path):
    old = tmp_path / "old.key"
    new = tmp_path / "new.key"

    old.write_text("abc")

    assert rotate_key(str(old), str(new)) is True
    assert new.read_text() == "cba"

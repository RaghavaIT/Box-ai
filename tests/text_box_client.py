from box_client import fetch_files

def test_fetch_files():
    items = fetch_files("0")
    assert items is not None

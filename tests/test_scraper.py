from scraper import extract_text_from_file

def test_extract_txt(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Hello RPA Bot")
    text = extract_text_from_file(str(file))
    assert "Hello RPA Bot" in text

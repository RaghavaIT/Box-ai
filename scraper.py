import os
import PyPDF2
import docx

def extract_text_from_file(file_path: str) -> str:
    """
    Extracts text from PDF, DOCX, or TXT file
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_pdf(file_path)
    elif ext in (".docx", ".doc"):
        return extract_docx(file_path)
    elif ext == ".txt":
        return extract_txt(file_path)
    return ""

def extract_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

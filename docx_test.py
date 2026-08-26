from docx import Document 
doc = Document ("/Users/dhritijindel/placements/RESUME`/DHRITIJINDAL_RESUME'SDE.docx")
for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)
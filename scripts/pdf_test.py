import pdfplumber

SECTION_HEADERS = ["EDUCATION", "TECHNICAL SKILLS", "EXPERIENCE", "PROJECTS", "LEADERSHIP"]

def parse_resume(pdf_path):
    all_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text()
            all_text += "\n"

    lines = all_text.split("\n")

    sections = {}
    current_section = None

    for line in lines:
        stripped = line.strip()
        if stripped in SECTION_HEADERS:
            current_section = stripped
            sections[current_section] = []
        elif current_section and stripped:
            sections[current_section].append(stripped)

    return sections

result = parse_resume("/Users/dhritijindel/placements/RESUME`/DHRITIJINDAL_RESUME'SDE.pdf")

for section_name, section_lines in result.items():
    print(f"--- {section_name} ---")
    for line in section_lines:
        print(line)
    print()

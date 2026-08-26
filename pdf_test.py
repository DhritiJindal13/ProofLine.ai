import pdfplumber

# known section headers we expect to find in the resume (must match exactly, case-sensitive for now)
SECTION_HEADERS = ["EDUCATION", "TECHNICAL SKILLS", "EXPERIENCE", "PROJECTS", "LEADERSHIP"]

def parse_resume(pdf_path):
    all_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text()
            all_text += "\n"

    lines = all_text.split("\n")          # split the big string into a list of individual lines

    sections = {}                          # dictionary to hold section_name -> list of lines
    current_section = None                 # tracks which section we're currently inside

    for line in lines:
        stripped = line.strip()            # remove leading/trailing whitespace from this line
        if stripped in SECTION_HEADERS:    # is this line a section header?
            current_section = stripped     # switch to this new section
            sections[current_section] = [] # start an empty list to collect lines under it
        elif current_section and stripped: # if we're inside a section AND the line isn't empty
            sections[current_section].append(stripped)  # add this line to the current section

    return sections

result = parse_resume("/Users/dhritijindel/placements/RESUME`/DHRITIJINDAL_RESUME'SDE.pdf")

for section_name, section_lines in result.items():   # loop through each section we found
    print(f"--- {section_name} ---")                 # print the section name as a header
    for line in section_lines:
        print(line)
    print()   # blank line for spacing between sections
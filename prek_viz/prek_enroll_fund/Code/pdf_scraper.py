from pathlib import Path
import PyPDF2
base_dir = Path(__file__).parent
path = base_dir / "pdf"

def extract_pages_with_keywords(pdf_path, keywords, output_path):
    """
    Extracts pages from a PDF that contain specific keywords.

    :param pdf_path: Path to the source PDF file.
    :param keywords: List of keywords to search for.
    :param output_path: Path to the output PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        keywords_found_count = 0
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            text = page.extract_text()
            if text and any(keyword in text for keyword in keywords):
                keywords_found_count +=1
                writer.add_page(page)
            if keywords_found_count == 2:
                break

        if len(writer.pages) > 0:
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
        else:
            print("No pages found with the given keywords.")


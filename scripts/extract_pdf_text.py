import os
import argparse
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extracts text from a single PDF file."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF files.")
    parser.add_argument("input", help="Path to a PDF file or a directory containing PDFs.")
    parser.add_argument("-o", "--output", help="Directory to save extracted text files. Defaults to current directory.")
    
    args = parser.parse_args()
    
    input_path = args.input
    output_dir = args.output if args.output else "."
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    if os.path.isfile(input_path):
        files = [input_path]
    elif os.path.isdir(input_path):
        files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.lower().endswith(".pdf")]
    else:
        print(f"Error: {input_path} is not a valid file or directory.")
        return

    for pdf_file in files:
        print(f"Extracting text from: {pdf_file}...")
        text = extract_text_from_pdf(pdf_file)
        if text:
            base_name = os.path.splitext(os.path.basename(pdf_file))[0]
            output_file = os.path.join(output_dir, f"{base_name}.txt")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()

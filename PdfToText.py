import PyPDF2


def pdf_to_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()

            return text
    except FileNotFoundError:
        return "The specified file was not found."

def main():

    path_to_pdf = input("Enter pdf file: ").strip()

    text = pdf_to_text(path_to_pdf)

    if text:
        text_file = path_to_pdf.replace('.pdf', '_text.txt')
        with open(text_file, 'w', encoding='utf-8') as file:
            file.write(text)
            print(f"Successfully extracted and saved to {text_file}")
    else:
        print("No text was found in pdf")


if __name__ == "__main__":
    main()
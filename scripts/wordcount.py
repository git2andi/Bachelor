import PyPDF2
import re

def count_words_in_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_words = 0
        for page in reader.pages:
            text = page.extract_text()
            words = re.findall(r'\b\w+\b', text)
            num_words += len(words)
        return num_words

# Replace with your actual PDF file path
pdf_path = r'C:\Users\Andi\Desktop\Bachelor\abschlussarbeit.pdf'
word_count = count_words_in_pdf(pdf_path)
print(f"Total word count: {word_count}")

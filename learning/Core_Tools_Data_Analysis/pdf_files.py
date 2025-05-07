# pdf

from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

reader = PdfReader("data/sample.pdf")
print(len(reader.pages))  # Number of pages in the PDF
print(reader.pages[0].extract_text())  # Extract text from the first page
print()
print(reader.pages[0].extract_text().split("\n\n\t"))  # Split text into lines

#rotate
read = reader.pages[0]
read.rotate(90)  # Rotate the page 90 degrees
writer = PdfWriter()
writer.add_page(read)  # Add the rotated page to the writer

with open("data/sample_rotated.pdf", "wb") as f:
    writer.write(f)  # Write the rotated page to a new PDF file
    f.close()  # Close the file after writing

#merge pdfs
pdfs = ["data/sample.pdf", "data/Sample-pdf.pdf"]
pdf_writer = PdfWriter()
#merge 2 pdfs
for pdf in pdfs:
    pdf_writer.append(pdf)

#write to a new pdf
with open ("data/merged.pdf", "wb") as f:
    pdf_writer.write(f)  # Write the merged pages to a new PDF file
    f.close()  # Close the file after writing
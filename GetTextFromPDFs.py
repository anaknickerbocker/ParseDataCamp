"""
GetTextFromPDFs.py was created to pull text from the downloaded pdfs.

Unfinished. The formatting of the scraped text is nearly unusable.
"""

# import PyPDF2
#
# file_path = 'D:\\Users\\ana1\\PycharmProjects\\ParseDataCamp\\Importing Data in Python (Part 1).pdf'
#
# pdf_file = open(file_path, 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# number_of_pages = read_pdf.getNumPages()
# for page_number in range(number_of_pages):
#     page = read_pdf.getPage(page_number)
#     page_content = page.extractText()
#     print(page_content.encode('utf-8'))
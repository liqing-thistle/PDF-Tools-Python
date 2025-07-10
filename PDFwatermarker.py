import sys
import PyPDF2

template = sys.argv[1]
watermark = sys.argv[2]

reader = PyPDF2.PdfReader(template)
marker = PyPDF2.PdfReader(watermark)
output = PyPDF2.PdfWriter()
num_pages = len(reader.pages)
print(f'This PDF file indluces {num_pages} pages in total.')

for i in range(num_pages):
    page = reader.pages[i]
    mark = marker.pages[0]
    page.merge_page(mark)
    output.add_page(page)

output.write('Watermarked.pdf')

print('Watermarked PDF created as \'Watermarked.pdf\'')
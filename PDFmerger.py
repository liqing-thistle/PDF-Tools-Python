import sys
import PyPDF2

# use sys module to grab all arguments, which refers to all input PDF files
input_file = sys.argv[1:]

# write a function to merge PDFs
def pdf_merge(pdf_list, output_filename = 'Merged.pdf'):
    merger = PyPDF2.PdfMerger()  # create a PdfMerger object
    for pdf in pdf_list:
        merger.append(pdf)
        reader = PyPDF2.PdfReader(pdf)
        num_pages = len(reader.pages)
        print(f'This PDF file  includes {num_pages} pages.')

    merger.write(output_filename)
    merger.close()

    mreader = PyPDF2.PdfReader(output_filename)
    num_pages_merged = len(mreader.pages)
    print(f'The merged file includes {num_pages_merged} pages.')

pdf_merge(input_file)




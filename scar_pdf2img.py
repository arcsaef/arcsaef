# import module
from pdf2image import convert_from_path
import os

# source programming credits
# https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/
# https://www.geeksforgeeks.org/introduction-to-python-pytesseract-package/
# https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html#simplest-invocation-to-ocr-an-image
# https://guides.library.illinois.edu/c.php?g=347520&p=4121426#:~:text=Tesseract%20has%20a%20limited%20number,PDF%20(searchable)
# https://stackoverflow.com/questions/53481088/poppler-in-path-for-pdf2image

# Convert SCAR bulletins into images so we can run an OCR program
# like tesseract over them. This exercise will allow us to search
# the text for words, regex, etc. In brief make the pdfs machine-reeadable.

pop_path = "C:/Users/****/AppData/Local/poppler-24.08.0/Library/bin" 
pdf_path = "C:/Users/****/Downloads/SCAR Bulletins-20250203T230902Z-001/dregs/"
img_path = "C:/Users/****/Downloads/SCAR Bulletins-20250203T230902Z-001/pdf2img/"
dir_list = os.listdir(pdf_path)

for pdf in dir_list:
    if pdf.endswith(".pdf"):
        # Store Pdf with convert_from_path function
        images = convert_from_path(f"{pdf_path}{pdf}", poppler_path=pop_path)

        for i in range(len(images)):
            # Save pages as images in the pdf
            images[i].save(f"{img_path}{os.path.splitext(pdf)[0]}_{str(i)}.jpg", 'JPEG')

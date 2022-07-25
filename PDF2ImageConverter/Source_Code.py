import os
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path

try:
    par_dir = "c:/Users/pc/Desktop/HexaWind InternShip/PDF2ImageConverter"

    for pdf_file in os.listdir(par_dir+"/Unprocessed Files"):
        print(pdf_file + " is being Processed.")
        inputpdf = PdfFileReader(open(par_dir+"/Unprocessed Files/"+pdf_file, "rb"))
        maxPages = inputpdf.numPages

        page_count=0
        total_pages = maxPages
        while maxPages>0:
            pages = convert_from_path(par_dir+"/Unprocessed Files/"+pdf_file,first_page=page_count+1,last_page=page_count+min(10,maxPages))

            img_file = pdf_file.replace('.pdf',"")

            count=page_count
            loc = par_dir+"/Processed Files/"+pdf_file
            if not os.path.isdir(loc):
                os.mkdir(loc)
            for page in pages:
                count += 1
                jpeg_file = 'Page ' + str(count) + '.jpeg'
                page.save(loc+"/"+jpeg_file,'JPEG')
            maxPages -= 10
            page_count += 10
            if maxPages>0:
                print(str(page_count) +"/"+ str(total_pages)+ " pages are processed." )
            else:
                print(str(total_pages) +"/"+ str(total_pages)+ " pages are processed." )
        print(pdf_file + " is processed Completely.\n")

except Exception as e:
    print(e)
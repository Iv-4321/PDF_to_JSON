import fitz

fitz.open('report.pdf')


for pageNumber, page in enumerate(file.pages()):

    text = page.getText()

    txt = open(f'report_Page_{pageNumber}.txt', 'a')
    txt.writelines(text)
    txt.close()

for imgNumber, img in enumerate(page.ImgeList(), start=1):

    xref = img[0]

    pix = fitz.Pixmap(file,xref)

    if pix.n > 4:

        pix = fitz.Pixmap(fitz.csRGB, pix)

    pix.writePNG(f'image_Page{pageNumber}_{imgNumber}.png')
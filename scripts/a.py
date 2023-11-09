
from ironpdf import *

pdf = PdfDocument.FromFile("template/certificate.pdf")

# Extract all pages to a folder as image files
# pdf.RasterizeToImageFiles("*.jpeg",DPI=96)

pdf.RasterizeToImageFiles("intermediate/*.jpeg",DPI=200)



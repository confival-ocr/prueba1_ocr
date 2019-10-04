#====================================================================================
#--> IMPORTAMOS LA LIBRERIA PARA OCR EN PYTHON 3 PYTESERACT 
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

img = convert_from_path('C:\\Users\\Jhon Jairo\\Desktop\\python\\OCR\\ced1.pdf')

#--> UBICACION PAQUETE TESSERACT EN LOCAL
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#--->SE GUARDA LOS DATOS DE IMAGEN PROCESADA POR PYTESSERACT 
print("==============================================================================")
d = pytesseract.image_to_string(Image.open("newL2.jpg"))
print(d) #imprime el string de datos obtenidos a traves de pytesseract



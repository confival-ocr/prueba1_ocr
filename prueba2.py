#====================================================================================
#--> IMPORTAMOS LA LIBRERIA PARA OCR EN PYTHON 3 PYTESERACT 
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#--> UBICACION PAQUETE TESSERACT EN LOCAL
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#--->SE GUARDA LOS DATOS DE IMAGEN PROCESADA POR PYTESSERACT 
d = pytesseract.image_to_string(Image.open("bajaResolucionJhon.jpg"))
print(d) #imprime el string de datos obtenidos a traves de pytesseract


#====================================================================================
#--> IMPORTAMOS LA LIBRERIA PARA OCR EN PYTHON 3 PYTESERACT 
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#--> UBICACION PAQUETE TESSERACT EN LOCAL
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(" ===================================")
print("|      PROBANDO OCR CONFIVAL        |")
print(" ===================================")

#====================================================================================
print("=============================================================")
print("SCRIPT EN PYTHON PARA RECONOCIMIENTO OPTICO DE CARACTERES OCR")
print("=============================================================")

#====================================================================================
#--->SE GUARDA LOS DATOS DE IMAGEN PROCESADA POR PYTESSERACT 
d = pytesseract.image_to_string(Image.open("jhon5.png"))
#print (d) imprime el string de datos obtenidos a traves de pytesseract
#print(type(d)) retorna el tipo de dato para d

#-->SE DIVIDE EL STRING DE DATOS EN ITEMS PARA ALMACENAR EN UNA LISTA
datos = d.split() 
#print(type(datos)) retorna el tipo de dato para la variable datos ()
print(datos)

cedula = (datos[9:10])
print("Identificacion  = ", cedula)

nombres = (datos[12:14])
print("Nombres = ", nombres)

apellidos = (datos[10:12])
print("Apellidos = ", apellidos)
#print(cedula.replace('.', ''))


datos_cedula=[79912457,"alejandro","juyo"]
var_cedula={"numero":datos_cedula[0], "nombre":datos_cedula[1], "apellido":datos_cedula[2]}
print(var_cedula)

#manipulación de cadenas en Python
#como cortar cadenas en python
#como pegar cadenas en python 
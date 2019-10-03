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
d = pytesseract.image_to_string(Image.open("resolucionAceptable1.png"))
#print(d) #imprime el string de datos obtenidos a traves de pytesseract

#-->SE DIVIDE EL STRING DE DATOS EN ITEMS PARA ALMACENAR EN UNA LISTA
datos = d.splitlines() 
#print(type(datos)) retorna el tipo de dato para la variable datos ()
print(datos)
datos_cedula = []
temp1 = datos[3]
tempcedula = temp1.split(" ")
#print(tempcedula)
cedula = tempcedula[1].replace(".", "")
#print(cedula) 
NumCedula = int(cedula)
print("==================================================")
print("Numero de Cedula: ", NumCedula)
print(type(NumCedula))
datos_cedula.append(NumCedula)
print("==================================================")

print("==================================================")
nombres = datos[6]
print("Nombres: ", nombres)
print(type(nombres))
datos_cedula.append(nombres)
print("==================================================")

print("==================================================")
apellidos = datos[4]
print("Apellidos: ", apellidos)
print(type(apellidos))
datos_cedula.append(apellidos)
print("==================================================")

print("==================================================")
print("arreglo de datos cedula")
print("Datos cedula => ", datos_cedula)

print("==================================================")
print("diccionario variable cedula")
var_cedula={"numero":datos_cedula[0], "nombre":datos_cedula[1], "apellido":datos_cedula[2]}
print("var_cedula => ", var_cedula)


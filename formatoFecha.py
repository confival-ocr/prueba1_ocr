date = '10-OCT-1989'

def ordenarFecha(date):
    if(len(date)==11):
        iz = date[:2]
        cen = date[2:7]
        der = date[7:]
        y = der + cen + iz
        return y
    else:
        print("formato no valido de fecha")
    
print(ordenarFecha(date))
tempFecha = ordenarFecha(date)

def formatoFecha(date):
    if(date[5:8]=='ENE'):
        fecha = date.replace(date[5:8], '01')
        return fecha

    elif(date[5:8]=='FEB'):
        fecha = date.replace(date[5:8], '02')
        return fecha
    
    elif(date[5:8]=='MAR'):
        fecha = date.replace(date[5:8], '03')
        return fecha
    
    elif(date[5:8]=='ABR'):
        fecha = date.replace(date[5:8], '04')
        return fecha   

    elif(date[5:8]=='MAY'):
        fecha = date.replace(date[5:8], '05')
        return fecha

    elif(date[5:8]=='JUN'):
        fecha = date.replace(date[5:8], '06')
        return fecha
    
    elif(date[5:8]=='JUL'):
        fecha = date.replace(date[5:8], '07')
        return fecha
    
    elif(date[5:8]=='AGO'):
        fecha = date.replace(date[5:8], '08')
        return fecha
    
    elif(date[5:8]=='SEP'):
        fecha = date.replace(date[5:8], '09')
        return fecha

    elif(date[5:8]=='OCT'):
        fecha = date.replace(date[5:8], '10')
        return fecha

    elif(date[5:8]=='NOV'):
        fecha = date.replace(date[5:8], '11')
        return fecha

    elif(date[5:8]=='DIC'):
        fecha = date.replace(date[5:8], '12')
        return fecha

    else :
        return "formato no valido"
   
    
print(formatoFecha(tempFecha))

print(type(formatoFecha('1992-AGO-12')))

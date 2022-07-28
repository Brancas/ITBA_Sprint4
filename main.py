
from colorama import Fore, Style
from datetime import datetime
import csv

def pedirNombre():
    name = input(Fore.GREEN + "Ingrese el nombre del archivo CSV: \n")
    contenido = openFile(name)
    return contenido

def openFile(name):
    path = name + ".csv"
    with open(path, "r") as file:
        contenido = list()
        reader = csv.DictReader(file)
        for i in reader:
            contenido.append(i)
    return contenido

def createFile(name):
    path = name + ".csv"
    with open(path, "w", newline='') as file:
        encabezado = ['NroCheque','CodigoBanco','CodigoSucursal','NumeroCuentaOrigen','NumeroCuentaDestino','Valor','FechaOrigen','FechaPago','DNI','Estado','Tipo']
        writer = csv.DictWriter(file, fieldnames = encabezado)
        writer.writeheader()
        for row in arrayFiltrada:
            writer.writerow(row)
        file.close()

def filtro(array, clave, valor):
    resultado = list()
    if not valor:
        return array
        
    for i in array:
        if i[clave] == valor:
            resultado.append(i)
    if not resultado:
        print('No se encontraron coincidencias')
    return resultado

def filtrarFecha(eleccion):
    fecha1 = datetime.strptime(input("Fecha 1 (Formato: DAY-MONTH-YEAR): "),('%d-%m-%Y'))
    fecha2 = datetime.strptime(input("Fecha 2 (Formato: DAY-MONTH-YEAR): "),('%d-%m-%Y'))
    fecha1 = int(datetime.timestamp(fecha1))
    fecha2 = int(datetime.timestamp(fecha2))
    fechasFiltradas = list()
    for i in contenido:
        fechasContenido = i[eleccion]
        fechasDateTime = datetime.strptime(fechasContenido, '%d-%m-%Y')
        fechasDateTime = int(datetime.timestamp(fechasDateTime))
        comparacion = fecha1 <= fechasDateTime and fecha2 >= fechasDateTime
        if comparacion:
            fechasFiltradas.append(i)
    return fechasFiltradas

def pantalla():
    for i in range(len(arrayFiltrada)):
                    print(' ==============================')
                    print('|| Nro de Cheque ==========>' + arrayFiltrada[i]['NroCheque']+' ||')
                    print('|| Codigo de Banco ======>'+ arrayFiltrada[i]["CodigoBanco"]+' ||')
                    print('|| Codigo de sucursal ===>'+ arrayFiltrada[i]["CodigoSucursal"]+' ||')
                    print('|| Cuenta Origen ========>'+ arrayFiltrada[i]["NumeroCuentaOrigen"]+' ||')
                    print('|| Cuenta Destino =======>'+ arrayFiltrada[i]["NumeroCuentaDestino"]+' ||')
                    print('|| Valor/Monto ======>'+ arrayFiltrada[i]["Valor"]+' ||')
                    print('|| Fecha Origen ==>'+ arrayFiltrada[i]["FechaOrigen"]+' ||')
                    print('|| Fecha Pago ====>'+ arrayFiltrada[i]["FechaPago"]+' ||')
                    print('|| DNI =============>'+ arrayFiltrada[i]["DNI"]+' ||')
                    print('|| Estado =========>'+ arrayFiltrada[i]["Estado"]+' ||')
                    print('|| Tipo ==========>'+ arrayFiltrada[i]["Tipo"]+' ||')
                    print(' ==============================')
                 

if __name__ == '__main__':
    while True:
        print(Fore.RED + 'APP de Procesamiento batch de cheques')
        print(Style.RESET_ALL)
        while True:
            try:
                contenido = pedirNombre()
                break
            except:
                continue

                
        while True:
            print(Fore.CYAN+ 'Indique una opcion para filtrar: \n1. ESTADO \n2. TIPO\n3. DNI \n4. RANGO DE FECHAS')
            opcion = input('==> ')
            match opcion:
                case '1':
                    while True:
                        print('Como desea filtrar el archivo: \n1. PENDIENTE \n2. APROBADO \n3. RECHAZADO')
                        opcion = input('==> ')
                        match opcion:
                            case '1':
                                opcion = 'PENDIENTE'
                            case '2':
                                opcion = 'APROBADO'
                            case '3':
                                opcion = 'RECHAZADO'
                            case _:
                                continue                     
                        arrayFiltrada=  filtro(contenido,'Estado',opcion )
                        break
                case '2':
                    while True:
                        print('Como desea filtrar el archivo: \n1. EMITIDO \n2. RECHAZADO')
                        opcion = input('==> ')
                        match opcion:
                            case '1':
                                opcion = 'EMITIDO'
                            case '2':
                                opcion = 'DEPOSITADO'
                            case _:
                                continue    
                        arrayFiltrada=  filtro(contenido,'Tipo',opcion )
                        break
                case '3':
                    dni = input(Fore.BLUE + 'Ingrese el DNI a buscar: ')
                    arrayFiltrada=  filtro(contenido,'DNI',dni )
                case '4':
                    opcion = 'RANGO DE FECHAS'
                    while True:
                        print("Elija opcion de filtro: \n1. Fecha de Origen \n2. Fecha de pago")
                        eleccion = input()
                        if eleccion == str(1):
                            eleccion = 'FechaOrigen'
                        elif eleccion == str(2):
                            eleccion = 'FechaPago'
                        else:
                            continue
                        print('Ingrese un rango de fechas a buscar:')
                        arrayFiltrada = filtrarFecha(eleccion)
                        break
                case '_':
                    continue
            break
        if arrayFiltrada:    
            while True:
                print('Elija una opcion para la salida de datos \n1. PANTALLA \n2. CSV')
                opcion = input('==> ')
                match opcion:
                    case'1':
                        pantalla()
                    case'2':
                        createFile(f"{arrayFiltrada[0]['DNI']} {datetime.timestamp(datetime.now())}")
                    case '_':
                        continue
                break

        print('Desea continuar \n1. SI \n2. NO \n')
        opcion = input('==> ')
        if int(opcion) != int(1):
            break
    print(Style.RESET_ALL)
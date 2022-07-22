from cgitb import reset
from os import times_result
from sqlite3 import Timestamp
from turtle import width
from colorama import init, Fore, Back, Style
from datetime import datetime
import csv

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
    with open(path, "w") as file:
        print(file)

def filtro(array, clave, valor):
    resultado = list()
    if not valor:
        return array
        
    for i in array:
        if i[clave] == valor:
            resultado.append(i)   
    return resultado

def filtrarFecha():
    fecha1 = datetime.strptime(input("Fecha 1 (Formato: DAY-MONTH-YEAR): "),('%d-%m-%Y'))
    fecha2 = datetime.strptime(input("Fecha 2 (Formato: DAY-MONTH-YEAR): "),('%d-%m-%Y'))
    fecha1 = int(datetime.timestamp(fecha1))
    fecha2 = int(datetime.timestamp(fecha2))
    fechasFiltradas=[]
    print(type(contenido))
    print("Comienzio del test")

    

    for i in contenido:
        if int(datetime.timestamp(i['FechaOrigen'])) >= fecha1 and int(datetime.timestamp(i['FechaOrigen']))<= fecha2:
            print(fecha1,i,fecha2)
            fechasFiltradas.append(i)
# SEGUIR PROBANDO ITERACIONES DE CODIGO HASTA QUE ENCUENTRE LA FORMA DE CONEVRTIR LAS FECHAS EN TIMESTAMP PARA FILTRARLAS

    
    print(fecha1)
    print(fecha2)
    # resultado = list()
    # if not datetime.valor():
    #     return array
    
    # for i[clave] == datetime.valor():
    #     if 
    #         resultado.append(i)
    # return resultado
    
if __name__ == '__main__':
    runtime = 0
    while runtime == 0:
        print(Fore.RED + 'APP de Procesamiento batch de cheques')
        print(Style.RESET_ALL)
        try:
            name = input(Fore.GREEN + "Ingrese el nombre del archivo CSV: \n")
            contenido = openFile(name)
        except:
            createFile(name)

        print(Fore.CYAN+ 'Indique una opcion para filtrar: \n1. ESTADO \n2. TIPO\n3. DNI \n4. RANGO DE FECHAS(no disponible)\nPor defecto SIN FILTRO')
        opcion = input('==> ')
        match opcion:
            case '1':
                print('Como desea filtrar el archivo: \n1. PENDIENTE \n2. APROBADO \n3. RECHAZADO')
                opcion = input('==> ')
                match opcion:
                    case '1':
                        opcion = 'PENDIENTE'
                    case '2':
                        opcion = 'APROBADO'
                    case '3':
                        opcion = 'RECHAZADO'
                    
                arrayFiltrada=  filtro(contenido,'Estado',opcion )
            case '2':
                match opcion:
                    case '1':
                        opcion = 'EMITIDO'
                    case '2':
                        opcion = 'DEPOSITADO'
                    
                arrayFiltrada=  filtro(contenido,'Tipo',opcion )
            case '3':
                dni = input(Fore.BLUE + 'Ingrese el DNI a buscar: ')
                arrayFiltrada=  filtro(contenido,'DNI',dni )
            case '4':
                opcion = 'RANGO DE FECHAS'
                print('Ingrese un rango de fechas a buscar:')
                filtrarFecha()
            case '_':
                opcion = False

        print('Elija una opcion para la salida de datos \n1. PANTALLA \n2. CSV')
        opcion = input('==> ')
        match opcion:
            case'1':
                print(arrayFiltrada)
            case'2':
                pass


        # print('Indique una opcion para coninuar \n1. Agregar nuevo movimiento \n2. Ver movimientos\n3. Terminar(Por defecto)')
        # opcion = input('==> ')

        

        print('Desea continuar \n1. SI \n2. NO \n')
        runtime = input('==> ')
        if runtime == '2':
            runtime = 3
        else:
            runtime = 0
    print(Style.RESET_ALL)






# archivo = input(Fore.GREEN + 'Ingrese el nombre del archivo CSV: \n')
# print('Como desea filtrar el archivo: \n1. PENDIENTE \n2. APROBADO \n3. RECHAZADO')
# opcion = input('==> ')
# print('Elija una opcion para la salida de datos \n1. PANTALLA \n2. CSV')
# opcion = input('==> ')
# print('Indique una opcion para coninuar \n1. Agregar nuevo movimiento \n2. Ver movimientos\n3. Terminar(Por defecto)')
# opcion = input('==> ')
# print('Indique una opcion para filtrar movimientos \n1. ESTADO \n2. DNI \n3. RANGO DE FECHAS')
# opcion = input('==> ')
# print('Desea continuar \n1. SI \n2. NO \n')
# runtime = input('==> ')
# if runtime == 1:
#     runtime=0
# print(Style.RESET_ALL)
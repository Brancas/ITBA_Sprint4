import datetime
from datetime import datetime as dt_dt
from datetime import date as dt_date
from sqlite3 import Timestamp
from time import strptime

# as dt_dt
# def openFile(name):
#     path = name + ".csv"
#     with open(path, "r") as file:
#         contenido = list()
#         reader = csv.DictReader(file)
#         for i in reader:
#             contenido.append(i)
#     return contenido


Timestamp = dt_dt.timestamp(dt_dt.now())

print(Timestamp)

print(Timestamp)


# hoy = strptime(str(datetime.now().date()), '%Y-%d-%m')
# print(hoy, type(hoy))

# # hoy = datetime.now().date()
# hoy =dt_date.today()
# # print(hoy, type(hoy))


# PRUEBAS DEL LIBREO PYTHON PARA FINANZAS
fecha_str= "2020-04-17"
fecha= dt_dt.strptime(fecha_str, '%Y-%m-%d')

print(fecha)








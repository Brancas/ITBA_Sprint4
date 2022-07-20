# ITBA_Sprint4
 Este es el repositorio correspondiente al sprint 4 del curso Full Stack Dev del ITBA

FINAL DE SPRINT 4.
||-><----><-- Consigna --><----><-||
Los distintos movimientos de cheques del banco
Se van registrando en un archivo de texto 
donde cada registro almacenado es una linea del archivo

Este archivo contiene los campos:
NroCheque -> Numero de cheque, este debe ser unico por cuenta  ✔️
CodigoBanco -> Codigo numerico del banco, #! entre 1 y 100. ✔️
CodigoSucursal -> Codigo numerico de la sucursal del banco #! entre 1 y 300. ✔️
NumeroCuentaOrigen -> Cuenta donde se cobra el cheque  ✔️
NumeroCuentaDestino -> Cuenta donde se cobra el cheque ✔️
Valor -> Float con el valor del cheque ✔️
FechaOrigen -> Fecha de emision: (en timestamp) ✔️
FechaPago -> Fecha de pago o cobro del cheque: (en timestamp) ✔️
DNI -> String con DNI del cliente donde se permite identificarlo  ✔️
Estado -> Puede tener tres valores: pendiente, aprobado o rechazado ✔️
Tipo -> Puede tener dos valores: Emitido o DEPOSITADO ✔️
||-><----><----><----><----><----><----><----><----><----><----><----><----><-||
? Requerimientos:
? 2. El orden de los argumentos son los siguientes:
    a. Nombre del archivo csv. ✔️
    b. DNI del cliente donde se filtraran.✔️
    c. Salida: PANTALLA o CSV.
    d. Tipo de cheque: EMITIDO o DEPOSITADO ✔️
    e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO (OPCIONAL) ✔️
    f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy(Opcional) ✔️
? 3. Si para un DNI dado un numero de cheque de una misma cuenta se repite,
?    se debe mostrar el error por pantalla, indicando que ese es el problema. ✔️
? 4. Si el parametro "Salida" es PANTALLA, se debera imprimir por pantalla
?    todos los valores que se tienen; 
?    Si el parametro "Salida" es CSV, se debera exportar a un csv con las siguientes
?    condiciones:
        a. El nombre de archivo tiene que tener el formato <DNI><TIMESTAMPS ACTUAL>.csv
        b. Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.
? 5. Si el estado del cheque no se pasa, se deberan imprimir los cheques sin filtrar
?    por estado.
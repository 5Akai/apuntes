import time
import sys

import pymssql

connection = pymssql.connect(
    server="hostdb-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)
cursor = connection.cursor(as_dict=True)

tiempo = time.time()

#Listado de clientes de USA y el número de pedidos de cada cliente




#DEBUG
print(f"--- Tiempo de Ejecución ----")
print(f"%s Segundos" % (time.time() - tiempo))

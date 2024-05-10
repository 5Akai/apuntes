import time
import sys
!{sys.executable} -m pip install --upgrade pip
!{sys.executable} -m pip install pymssql

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

cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")

for row in cursor.fetchall():
    cursor2 = connection.cursor()
    cursor2.execute(f"SELECT COUNT(*) FROM dbo.Orders WHERE CustomerID = '{row['CustomerID']}'")
    print(f"{row['CustomerID']}# {row['CompanyName']} -> {cursor2.fetchone()} pedidos")

print(f"--- Tiempo de Ejecución ----")
print(f"%s Segundos" % (time.time() - tiempo))


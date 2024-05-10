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

query = """
    SELECT c.CustomerID, c.CompanyName, COUNT(o.OrderID) AS NumPedidos
    FROM dbo.Customers c
    JOIN dbo.Orders o
    ON c.CustomerID = o.CustomerID
    WHERE c.Country = 'USA'
    GROUP BY c.CustomerID, c.CompanyName
"""
cursor.execute(query)
for row in cursor.fetchall():
    print(f"{row['CustomerID']}# {row['CompanyName']} -> {row['NumPedidos']} pedidos")


#DEBUG
print(f"--- Tiempo de Ejecución ----")
print(f"%s Segundos" % (time.time() - tiempo))

quit()
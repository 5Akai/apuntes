#Sacar la letra del DNI

#Formula: el resto de dividir el numero del DNI entre 23 (%)
import string

letras = letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']

print(letras)

try:

    dni = int(input("Introduce los números de tu DNI:"))

    res = dni % 23


    print(res)
    print(f"tu DNI es {dni}{letras[res]}.")

except exception as err:
    print(f"error: {err}")
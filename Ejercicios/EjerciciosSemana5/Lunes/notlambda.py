from functools import reduce

numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]

# Escribe una función que retorne una lista con los número mayores de 100
def MayorDeCien(lista):
    resultado = []
    
    for numero in lista:
        if numero > 100:
            resultado.append(numero)


    return resultado

print(MayorDeCien(numeros))


# Escribe una función que retorna true cuando un número es mayor de 100

def EsMayorDeCien(numero):
        if numero > 100:
            return True
        else:
            return False

# filter aplica la función a la lista indicada en el otro parámetro y lo vuelve otra lista.....filtrada jaj
print(f"Filter más una función estandar {list(filter(EsMayorDeCien, numeros))}")


# extraer números mayores de 100 mediante una función lambda con filter
#lambda numero: numero < 100 da true o false dependiendo de su condición sin más, recorriendo la lista
print(f"Filter más una función lambda que da true o false {list(filter(lambda numero: numero < 100, numeros))}")

print(f"Filter más una función lambda que da true o false {list(filter(lambda x: x < 50, numeros))}")

#Numeros pares

print(f"Numeros pares {list(filter(lambda x: x % 2 == 0, numeros))}")

print(f"Numeros impares {list(filter(lambda x: x % 2 != 0, numeros))}")


#Map hace lo mismo que filter, pero crea una nueva lista con los datos filtrados.
print(f"Datos: {numeros}")

resul = list(map(lambda x: (x * 10) / 2, numeros))
print(f"Resultado de sumar 10 y dividir entre 2: {resul}")


# Ejemplo reduce una suma
print(f"Resultado SUM: {sum(numeros)}")

# reduce los va sumando de dos en dos hasta que se queda sin parámetros
print(f"Resultado: {reduce(lambda x, y: x + y, numeros)}")

#


print(f"Datos: {numeros}")
print(f"Pares: {list(map(lambda x: x % 2 == 0, numeros))}")

print(f"Hay algún número par?: {any((map(lambda x: x % 2 == 0, numeros)))}")
print(f"Son todos pares? {all((map(lambda x: x % 2 == 0, numeros)))}")
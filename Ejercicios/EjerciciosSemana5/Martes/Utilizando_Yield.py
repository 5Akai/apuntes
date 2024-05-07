#####################################################################

# Utilizando yield                                                  #

#####################################################################


numeros = [8, 14, 65, 7, 14, 99, 745, 1, -35, 1408]


print(f"Datos: {numeros}")


def func1(lista):

    for i in lista:

        return i * 5

    

def func2(lista):

    resultado = []


    for i in lista:

        resultado.append(i * 5)


    return resultado   


print(f"Func 1: {func1(numeros)}")

print(f"Func 2: {func2(numeros)}")

print(f"Lambda: {list(map(lambda x: x * 5, numeros))}") # Map también retorna un generador

def func3(lista):

    for i in lista:

        yield i * 5 ##Genera un generador con un conjunto de datos, por eso imprime eso
print(f"Func 3: {func3(numeros)}")
print(f"Func 3 To-List: {list(func3(numeros))}")


# Utilización de los generadores 


from datetime import datetime

##Ejemplo de función que no recibe datos (no tiene parámetros) y no retorna datos##

def func1():
    """Func1, no tiene parámetros ni retorna datos\n\n pinga"""
    print("Hola mundo!!!")


##Ejemplo de función que sí recibe datos (si tiene parametros) y no retorna nada##

def func2(parametro1, parametro2):
    print(f"Me llamo {parametro1} y mi número de la suerte es {parametro2}")

##Ejemplo de función que sí recibe datos (si tiene parametros) y retorne##

def func3(parametro3):
    cantidad = len(parametro3)
    return cantidad

##Ejemplo de función que no recibe datos (no tiene parametros) y retorne##

def func4():
    return datetime.now().date().strftime("%A")

##Hasta que no se invoquen o llamen, no se van a ejecutar, ¿cuantas veces? pues las veces que los llamemos##

func1()
func2("Borja", 8)
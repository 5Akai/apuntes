
def sum(a,b):
   return a + b
def res(a,b):
   return a - b
def mul(a,b):
   return a * b
def div(a,b):
   return a / b


try:
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        calc = input("Introduce el cálculo a realizar: ")

        print(calc.upper())

        if calc.upper() == "SUMA":
            print(f"{a} + {b} = {sum(a,b)}")

        elif calc.upper() == "RESTA":
            print(f"{a} - {b} = {res(a,b)}")

        elif calc.upper() == "MULTIPLICACION":
            print(f"{a} X {b} = {mul(a,b)}")

        elif calc.upper() == "DIVISION":
            print(f"{a} entre {b} = {div(a,b)}")

        else:
            print(f"{a} + {b} = {sum(a,b)}")
except Exception as err:
    print(f"Error: operación no válida: {err}")
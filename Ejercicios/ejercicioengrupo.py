# Encuentas versión 1
# Preguntar Edad (validar)
# Preguntar puntuación de 0 a 10 (validar)
# Preguntar si es el último encuestado
# Con el último encuestado mostra el número de encuentas y la puntuación media

esUltimo = False
totalEnc = 0

puntTotal = 0
listaPunt = []
respuestaultimo = ""


while esUltimo == False:
     
    edad = input("Cual es tu edad?: ")
    
    while not edad.isdigit():
        edad = input("Por favor, introduce una edad válida: ")
        
        while edad.isdigit():
            break
    
    

    while int(edad) >= 101 or int(edad) <= -1:
        str(edad) == str(input("Por favor, introduce una edad válida: "))
  
            
    puntuacion = str(input("Cual es tu puntuación?: "))
   
    while not puntuacion.isdigit():
        
        puntuacion = input("Por favor, introduce una puntuación válida: ")
        while puntuacion.isdigit():
              while int(puntuacion) > 10 or int(puntuacion) < 0:
                puntuacion = str(input("Por favor, introduce una puntuanción válida: "))
              break
    
    
        
        
    

    respuestaultimo = input("Eres el último(S/N): ")
    puntTotal += int(puntuacion)
    totalEnc += 1
    


    if respuestaultimo.capitalize() == "S":
        esUltimo = True
        print(f"Número de encuestas: {totalEnc}")
        print(f"La puntuación media es: {puntTotal/totalEnc}\n")
        




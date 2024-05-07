from datetime import datetime

class Alumno:
    """Clase demostración del curso de Python"""

    # Variables de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    # Función constructora del objeto, se ejecuta al crear (instanciar) el objeto.
    #self es una variable que contiene el propio objeto.
    #Todos los objetos tienen una función init, es la función que ejecuta el propio objeto, todas estas funciones automáticamente agregadas son heredadas de object.
    def __init__(self, nombre, apellido1, apellido2 = "") -> None:
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2

        #Diversas funciones deel objeto Alumno
        
        def getEdad(self) -> int:
            resultado = datetime.now().date() - self.FechaNacimiento
            return resultado.days // 365


    def getNombreCompleto(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"

        def setFechaNacimiento(self, fecha) -> bool:
            try:
                if (len(fecha) == 10):
                    self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
                
                elif (len(fecha) == 8):
                    self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
                
                else:
                    return False
                return True
            except:
                return False

class Estudiante(Alumno):
    #Añadimos nuevas variables
    Curso = None

    #Sobreescribir la función constructora
    def __init__(self, nombre, apellido1, curso) -> None:
        #self.Nombre = nombre
        #self.Apellido1 = apellido1

        #Las líneas superiores no son necesarias ya que es la lógica escrita en la clase bsae y podemoas ejecutarla utilizando la fucnión super
        super().__init__(nombre, apellido1)

        #Nueva funcionalidad de la funcion constructora
        self.Curso = curso
    def getNombreCompleto(self) -> str:
            ###return f"{self.Nombre} {self.Apellido1} {self.Apellido2} - Curso: {self.Curso}"
        return f"{super().getNombreCompleto()} - Curso: {self.Curso}"
    
    #Añadimos nuevas funciones
    def Test(self) -> str:
        return "Función Test"



#Xreamos (Instanciamos) y utilizamos el objeto ALUMNO
a = Alumno("Ana", "Gomez")
print(a.getNombreCompleto())
print("")


# Creamos y utilizamos el objeto Estudiante
e = Estudiante("Borja", "Cabeza", "1A")
print(e.getNombreCompleto())
print(e.Test())
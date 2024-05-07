class Demo:
    __Clave = "Pinga!"


    def publico(self):
        print("Todos pueden sabeeeerrr")

    def _privado(self):
        print("Nadie debería saber")

    def __secreto(self):
        print(f"Nadie PUEDE saber, es un secreeetooo {self.__Clave}")

    def getSecreto(self, pw):
        if (pw == "Pestill0!"):
            self.__secreto()

        else:
            print("Acceso Denegado")


demo = Demo()
demo.publico()
demo._privado()
#demo._Demo__secreto()


demo.getSecreto("!")
print(dir(demo))

    
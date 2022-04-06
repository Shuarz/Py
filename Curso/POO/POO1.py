class Coche():

    def __init__(self):            #esto seria un constructor, despues de declarar el contructor, poner todo identado y el self

        self.__largoChasis=250 #creamos una propiedad de la clase ("largo coche") #las carecteriscas comunes, seria el estado inicial, los de "fabrica"
        self.__anchochasis=120
        self.__ruedas=4        #estamos encapsulando las ruedas, no se puede modificar fuera del constructor
        self.__enMarcha=False

    def arrancar(self, arrancamos): # (su comportamiento) esto un metodo que pertenece a una clase, la funcion no pertenece a una clase #sefl es igual a this
        self.__enMarcha=arrancamos #le pasamos por parametro si esta en marcha o no ahora, cuando llamamos a la funcion

        if(self.__enMarcha):
            chequeo = self.__chequeoInterno()


        if(self.__enMarcha and chequeo):
            
            return "el coche esta en marcha" 

        elif(self.__enMarcha and chequeo == False):

            return "algo esta mal en el chequeo"

        else:
            return "el coche esta parado"

    def estado(self):
        print("el coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchochasis, " y un largo de ", self.__largoChasis)



    def __chequeoInterno(self): #lo encapsulamos para que se use dentro de la clase
        print("realizando el chequeo interno...")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

            return True

        else:

            return False




miCoche = Coche() #creacion de mi objeto ("instaciar de una clase") (aca no se usa new para instaciar)

print("el largo del coche es: ", miCoche.largoChasis) #el punto es para acceder a la propiedad de la clase
print("el coche tiene ", miCoche.ruedas, " ruedas")

print(miCoche.arrancar(True)) #ahora neceita parametro

miCoche.estado()

print("-------- a continuacion creamos el segundo objeto-----------------")


miCocheDos=Coche()


print(miCoche.arrancar(False)) #hay que ponerlo dentro de un print, porque devuelve un string


miCoche.estado()

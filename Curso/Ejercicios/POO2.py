class Vehiculo():

    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enMarcha=True

    def acelerar(self):

        self.acelera=True

    def frenar(self):

        self.frena=True

    def estado(self):
        print("marca; ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.enMarcha, "\nacelarando: ", self.acelera, "\nfrenado: ", self.frena)


class Furgonetta(Vehiculo):

    def carga(self, cargar):
        self.cargado=cargar

        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgonetta esta vacia"


class Moto(Vehiculo): #dentro de los parentesis ponemos la clase que hereda
    hcaballito=""
    def caballito(self):
        self.hcaballito="voy haciendo el caballito" #sin el self, no hago referencia a la variable caballito

    def estado(self):  #para que pueda agregar mas propiedades a estado y no dañar la de vehiculo, sobreescribo en la clase moto y agrego lo que quiero
        print("marca; ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.enMarcha, "\nacelarando: ", self.acelera, "\nfrenado: ", self.frena, 
        "\n", self.caballito)


class VElectricos(Vehiculo):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo) #viaja a la clase padre, se instancia y ya tiene el contructor hecho con los atributos

        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True



miMoto=Moto("honda", "cbr") #le pasamos los parametros de la marca y modelo

miMoto.caballito()

miMoto.estado()

miFurgonetta=Furgonetta("renault", "kangoo")

print(miFurgonetta.arrancar(True))


class BicicletaElectrica(VElectricos, Vehiculo): #cuando herada dos clases, siempre usa primero la que le pasamos primero
    pass

miBici=BicicletaElectrica("honda", "12333")
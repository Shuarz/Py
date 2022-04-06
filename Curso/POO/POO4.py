class coche():

    def desplazamiento(self):
        print("me muevo en cuatro ruedas")

class moto():

    def desplazamiento(self):
        print("me muevo en dos ruedas")

class camion():

    def desplazamiento(self):
        print("me muevo en seis ruedas")


def desplazamientoVehiculo(vehiculo):

    vehiculo.desplazamiento()

miVehiculo=moto()

desplazamientoVehiculo(miVehiculo) #aca se crea el polimorfismo, cambia el valor a camion y sabe que hace referencia a desplazamiento del camion


'''
miVehiculo=moto()

miVehiculo.desplazamiento()

miVehiculo=coche()

miVehiculo.desplazamiento()



miVehiculo.desplazamiento()

'''
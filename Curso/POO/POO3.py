class Persona():

    def __init__(self, nombre, edad, lugarResidencia):

        self.nombre=nombre

        self.edad=edad

        self.lugarResidencia = lugarResidencia

    def descripcion(self):

        print("nombre:", self.nombre, " edad:", self.edad, " lugar:", self.lugarResidencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado) #la funcion "super" llama a la funcion padre

        self.salario=salario

        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion() 

        print("salario:", self.salario, "antiguedad:", self.antiguedad)

Manuel=Empleado(1500, 15, "manuel", 55, "colon")

Manuel.descripcion()



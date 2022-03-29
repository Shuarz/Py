print("Programa becas año 2022")

distanciaEscuela = int(input("introcude distancia al colegio en km "))
print(distanciaEscuela)

numeroHermanos = int(input("introduce cantidad de hermanos en el centro"))
print(numeroHermanos)

salarioFamiliar = int(input("introduce salario anual bruto"))
print(salarioFamiliar)

if distanciaEscuela >40 and numeroHermanos >2 and salarioFamiliar <= 20000:  #tambien se puede suplantar por un "OR" y acepta dos condiciones o solo esa
    
    print("tienes derecho a una beca")

else:

    print("no tienes derecho a una")
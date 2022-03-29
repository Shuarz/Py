salarioPresidente = int(input("Introduce salario presidente"))
print("salario presidente " + str(salarioPresidente)) #convierte el dato entero en texto para mostrar

salarioDirector = int(input("Introduce salario director"))
print("salario presidente " + str(salarioDirector)) 

salarioJefeArea = int(input("Introduce salario jefe"))
print("salario presidente " + str(salarioJefeArea)) 

salarioAdministrativo = int(input("Introduce salario administrativo"))
print("salario presidente " + str(salarioAdministrativo)) 

if salarioPresidente<salarioDirector<salarioJefeArea<salarioAdministrativo: #todas las operaciones se cumplieron
    print("todo funciona bien")

else: print("algo esta mal")

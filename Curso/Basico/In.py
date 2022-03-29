print("Asignaturas Optativas Año 2022")
print("Asignaturas Optativas:\n \nInformatica grafica \nPruebas de Software \nUsabilidad y Accesibilidad")

opcion= input("Escribe la asignatura escogida: ")

asigntatura = opcion.lower()

if asigntatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    
    print("asignatura elegida " + asigntatura)

else:

    print("la asignatura escogida no esta contemplada")

from ast import For


print("programa de evaluacion de notas de alumno")

notaAlumno=input("introduce la nota del alumno ") #imput toma el dato y aparte en los parentesis le ponemos info

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspendio"
	return valoracion #guardamos el valor de la comparacion
	

print(evaluacion(int(notaAlumno))) #con el int le decimos que esta tomando un numero entero


nombre="pildoras informaticas"

contador=0

for i in nombre:

	if i==" ":
		continue  #llega al caracter espacio, "lo saltea", sirve para que cuente ciertas cosas
	contador+=1


print(contador)



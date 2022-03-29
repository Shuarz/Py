import math #para el tercer ejecicio importamos la clase math con sus funciones (haremos eso con nuestras propias funciones)

i=1 #tipico de while,cumple la funcion hasta que termine

while i<10:

    print("ejecucion" + str(i))
    i=i+1 #contador

print("termino la ejecucion")





edad = int(input("introduce tu edad por favor: "))  #while con rango de edad hasta que pongas una edad correspondiente

while edad>0 and edad<100:
    print("has introducido una edad erronea, vuelve a intertarlo")
    edad = int(input("introduce tu edad por favor: "))

print("gracias")
print("edad del aspirante" + str(edad))





print("programa de calculo de raiz cuadrada")

numero=int(input("introduce un numero por favor: "))

intentos = 0

while numero<0:
    print("no se puede hallar la raiz de un numero negativo")

    if intentos ==2:
        print("demasiados intentos, el programa finalizo")
        break;

    numero=int(input("introduce un numero Positivo por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos <2:
    solucion=math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + "es" + str(solucion))
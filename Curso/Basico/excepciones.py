import math

def suma(numeroUno, numeroDos):
    return numeroUno+numeroDos

def resta(numeroUno, numeroDos):
    return numeroUno-numeroDos

def multiplica(numeroUno, numeroDos):
    return numeroUno*numeroDos

def divide(numeroUno, numeroDos):
    try: #aca capturamos el evento y generamos una excepcion, le pedimos que lo intente al menos
        return numeroUno/numeroDos

    except ZeroDivisionError: #aca la excepcion
        print("no se puede dividir por cero")
        return "operacion erronea" #aca lo que devuelve

    finally: #este se ejecuta siempre para informar, no importa si funciono o no el codigo
        print("calculo finalizado")


while True:
    try:

        opcionUno=(int(input("ingrese el primer numero: ")))

        opcionDos=(int(input("ingrese el segundo numero: ")))

        break

    except ValueError:
        print("los valores introducidos no son correctos, intentelo nuevamente")


operacion=input("introduce la operacion a realizar (suma - resta - multiplica - divide): ")


if operacion=="suma":
    print(suma(opcionUno, opcionDos))

elif operacion=="resta":
    print(resta(opcionUno, opcionDos))

elif operacion=="multiplica":
    print(multiplica(opcionUno, opcionDos))

elif operacion=="divide":
    print(divide(opcionUno, opcionDos))

else:
    print("operacion no contemplada")


'''                                            #comentado para que no rompa, pero lo importante aca en la funcion "raise"
def calcularRaiz(numeroUno):

    if numeroUno<0:
        raise ValueError ("el numero no puede ser negativo") #aca con el raise estamos parando el codigo, despues lo mandamos a una variable nueva para mostrar un mensaje mas amigable al usuario

        else:
            return math.sqrt(numeroUno)

opcionUno=(int(input("ingrese un numero: ")))

try:
    print(calcularRaiz(opcionUno))

except ValueError as errorDeNumeroNegativo: #mensaje amigable al usuario

    print(errorDeNumeroNegativo)

    print("programa terminado")

'''
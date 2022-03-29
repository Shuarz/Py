def generaPares(limite):

    numero=1


    while numero<limite:

        yield numero*2 # yield: contruir un objeto iterable, con los valores de la lista en su interior y los va almacenado uno en uno

        numero + numero+1

devuelvePares=generaPares(10) #aca guardo el objeto iterable que devuelve la funcion


print(next(devuelvePares)) #me da el primer valor de la lista

print("aqui podria ir mas codigo")

print(next(devuelvePares))

print("aqui podria ir mas codigo")

print(next(devuelvePares))


for i in devuelvePares: #me da los primeros 10 pares por consola

    print(i)




def devuelveCiudades(*ciudades): #le estoy diendo que no se la cantidad
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento #el yield from es un for dentro de otro for(osea, busca dentro del listado que le mandades a buscar)
            #yield subElemento

ciudadesDevuelta=devuelveCiudades("madrid", "barcelona", "bilbalo", "valencia")

print(next(ciudadesDevuelta))

print(next(ciudadesDevuelta))

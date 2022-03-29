miLista=["maria", "pepe", "marta", "antonio"] * 3 #el multiplicador al lado de la lista multiplica la lista

miLista.append("sandra") #agrega al final de la lista append

miLista.insert(2, "jose") #te pide dos parametros, donde meter el nombre y el nombre

miLista.extend(["pablo", "lucia", "ana"]) #extender la lista ya creada

miLista.remove("pepe") #elimina a uno asignado

miLista.pop() #por defecto elimina el ultimo

miLista2=["santiago", 3, True, 47.59]

miLista3=miLista+miLista2

print(miLista3[:])

print(miLista[:]) #si quiero seleccionar un elemento, pongo el numero

print(miLista.index("maria")) #el numero que esta posicionado esa persona en la lista

print("pepe" in miLista) #te dice si esta pepe en la lista

#print(miLista[0:3]) estoy seleccionando una porciond de la lista
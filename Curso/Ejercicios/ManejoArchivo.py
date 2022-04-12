from io import open #crear un archivo externo ver "io" 
archivoExterno= open("archivo.txt", "w") #te pide dos parametros, el nombre del archivo y formato y que hacer con el (escribir, leer, o apend)

frase="estupendo dis para estudiar python \n el martes"

archivoExterno.write(frase)

archivoExterno.close()



archivoExterno= open("archivo.txt", "r")

texto=archivoExterno.read()

textoLineas=archivoExterno.readlines()

archivoExterno.close()

print(texto)

print(textoLineas[0]) #le inidcamos que accedemos al primer elemento/primera linea



archivoExterno= open("archivo.txt", "a")

archivoExterno.write("\n siempre es lindo") #agregamos una tercera linea en el texto

archivoExterno.close()


archivoExterno= open("archivo.txt", "r")

print(archivoExterno.read())

archivoExterno.seek(0) #con el seek, lo posicionamos donde querramos y apartir lee lo que quiere

print(archivoExterno.read()) #por defecto esta en la posicon cero, pero lo podemos poner donde querramos que arranque
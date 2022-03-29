print("verificaccion de acceso")

edadUsuario = int (input("introduce tu edad, por favor "))

if edadUsuario<18: #aca al final del if
    print("no puedes pasar")

elif edadUsuario>100:   #en python se usa el "elif" en ves del "elseif"
    print("edad incorrecta")

else: #acordarte los dos puntos despues del else
    print("puedes pasar")

print("programa finalizado")
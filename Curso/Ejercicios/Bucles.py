for EstacionesAño in ["verano", "otoño", "invierno", "primavera"]: #en vez de for "i=5;i<5;i++" se pone "for variable in listado(array)"
    print(EstacionesAño)




for i in ["pildoras", "informatica", 3]:
    print("hola", end =" ") #esto sirve para que no lo muestre en formato lista, sino seguido, el espacio blanco estre comillas, le agrega un espacio a la palabra





email = False
miEmail = input("introduce tu direccion de email: ") 

for i in miEmail:
    
    if(i=="@"): #aca podemos usar el for para corroborar que sea un mail, ya que recorre caracter por caracter

        email=True

if email==True:
    print("El email es correcto")

else:
    print("el email no es correcto")




for i in range(5):  #este seria el mas parecido al for que se usa en la mayoria de lenguajes
    print("hola")
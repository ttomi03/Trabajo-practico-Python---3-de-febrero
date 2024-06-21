import secrets, string, sys

# les paso un diccionario donde cada valor tendra una cadena, es decir letras tiene una cadena del alfabeto en mayusculas y minusculas, numeros tiene la cadena de numeros del 0 al 9 y lo mismo con caracteres

diccionario = {
  "letras": string.ascii_letters,
  "numeros": string.digits,
  "caracteres": string.punctuation,
}

print( "---------- GENERADOR DE CONTRASEÑAS ---------- ")
opcion= int (input("Seleccione una de las siguientes opciones:\n " "1- Generar contraseña solo de letras\n" "2- Generar contraseña solo de numeros\n" "3- Generar contraseña Letras y Numeros\n" "4- Generar contraseña letras, numeros, caracteres\n" "0-Salir\n"))

if opcion == 1:
    largo= int(input("De cuantos caracteres quiere la contraseña?"))
    acum= ""
    contra=""
    for i in range (largo):
        contra= contra.join(secrets.choice("letras"))
        acum= acum + contra
    print(acum)
elif opcion == 2:
    largo= int(input("De cuantos caracteres quiere la contraseña?"))
    acum= ""
    contra= ""
    for i in range (largo):
        contra= contra.join(secrets.choice(diccionario["numeros"]))
        acum= acum + contra
    print(acum)
elif opcion == 3:
    largo= int(input("De cuantos caracteres quiere la contraseña?"))
    acum = ''.join(secrets.choice(diccionario["letras"] + diccionario["numeros"]) for _ in range(largo))
    print(acum)
elif opcion == 4:
    largo= int(input("De cuantos caracteres quiere la contraseña?"))
    acum = ''.join(secrets.choice(diccionario["letras"] + diccionario["numeros"]+ diccionario["caracteres"]) for _ in range(largo))
    print(acum)

elif opcion == 0:
    print("FIN DEL PROGRAMA")



# .join(secrets.choice(tipo))

# con ese comando podemos asignar a un strig que tome valores aleatorios de una lista (tipo)que le enviemos , en este caso la lista deberia ser una de las 3 del diccionario o una conbinacion.
import pickle, sys, os, random
def buscar_ticket(ticket):
        for i in dicccionario_ticket:
            if dicccionario_ticket["ticket"]== ticket:
                return dicccionario_ticket
        return None
opcionk=2
opcion=int(input("Seleccione una opcion\n 1-Alta ticket\n 2-Leer ticket\n 3-Salir\n"))
if opcion==1:
    while (opcionk != 2):
            dicccionario_ticket={
          "nombre": input("Ingrese su nombre\n"),
           "sector":input("Ingrese su sector\n"),
           "asunto":input("Ingrese asunto\n"),
           "problema": input("Ingrese su problema\n"),
           "ticket": random.randrange(1000, 9999),  
            }
            print("---------------------------------------")
            print("---------------------------------------")
            print("   SE GENERO EL SIGUIENTE TICKET   ")
            print("---------------------------------------")
            print("---------------------------------------")
            print("Su nombre:", dicccionario_ticket["nombre"], "  Ticket: ", dicccionario_ticket["ticket"]) 
            print("Sector: ", dicccionario_ticket["sector"])
            print("Asunto: ", dicccionario_ticket["asunto"])
            print("Problema: ", dicccionario_ticket["problema"])
            print("   Recordar su numero de ticket   ")
            print("---------------------------------------")
            with open('datos.bin','wb') as file:
                pickle.dump(dicccionario_ticket,file)
            opcionk=int(input("Quiere sacar otro ticket? 1-SI 2-NO\n"))

elif opcion==2:
    opcion_2=1
    while opcion_2 == 1: 
         with open ('datos.bin', 'rb') as file:
            dicccionario_ticket=pickle.load(file)
        
            ticketb2=int(input("Ingrese numero de ticket\n"))
            ticketb=buscar_ticket(ticketb2)
            print(ticketb) 
            opcion_2=int(input("DESEA VOLVER A LEER ? 1-SI 2-NO\n"))
elif opcion==3: 
    confirmacion=int(input("Desea cerrar el programa? 1-SI 2-NO\n"))
    if (confirmacion==1):
        print ("Gracias por usar el programa\n")
    elif (confirmacion==2):
        opcion=int(input("Seleccione una opcion\n 1-Alta ticket\n 2-Leer ticket\n 3-Salir\n"))
if opcion==1:
    
    while (opcion == 1):
        dicccionario_ticket={
          "nombre": input("Ingrese su nombre\n"),
           "sector":input("Ingrese su sector\n"),
           "asunto":input("Ingrese asunto\n"),
           "problema": input("Ingrese su problema\n"),
           "ticket": random.randrange(1000, 9999),  
        }
        print("---------------------------------------")
        print("---------------------------------------")
        print("   SE GENERO EL SIGUIENTE TICKET   ")
        print("---------------------------------------")
        print("---------------------------------------")
        print("Su nombre:", dicccionario_ticket["nombre"], "  Ticket: ", dicccionario_ticket["ticket"]) 
        print("Sector: ", dicccionario_ticket["sector"])
        print("Asunto: ", dicccionario_ticket["asunto"])
        print("Problema: ", dicccionario_ticket["problema"])
        print("   Recordar su numero de ticket   ")
        print("---------------------------------------")
        with open('datos.bin','wb') as file:
            pickle.dump(dicccionario_ticket,file)
        opcion=int(input("Quiere sacar otro ticket? 1-SI 2-NO\n"))
elif opcion==2:
    opcion_2=1
    while opcion_2 == 1: 
         with open ('datos.bin', 'rb') as file:
            dicccionario_ticket=pickle.load(file)
        
            ticketb2=int(input("Ingrese numero de ticket\n"))
            ticketb=buscar_ticket(ticketb2)
            print(ticketb) 
            opcion_2=int(input("DESEA VOLVER A LEER ? 1-SI 2-NO\n"))
elif opcion==3: 
    confirmacion=int(input("Desea cerrar el programa? 1-SI 2-NO\n"))
    if (confirmacion==1):
        print ("Gracias por usar el programa\n")
      
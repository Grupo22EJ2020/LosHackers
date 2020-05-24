print ("Bienvenido al Menu Principal")
print("Administrar Empleados =1")
print("Administrar Cursos =2")
print("Administrar Temas =3")
print("Administrar Videos =4")
Menu=int(input("Que opcion del MENU desea elegir: "))

if Menu==1:
    print("*"*20)
    print("Agregar =1")
    print("Borrar =2")
    print("Modificar =3")
    print("Consultar todo =4")
    opcion=int(input("Que opcion elige: "))

    if opcion==1:
        def main():
            archivoA=open("./archivos/Empleados.txt",'a')
            idEmpleado=(input("Ingrese su numero de Empleado: "))
            nombre=(input("Ingrese su Nombre: "))
            direccion=(input("Ingrese su Direccion: "))
            archivoA.write(idEmpleado + "|"+ nombre + "|" + direccion + "|" + "\n")
            archivoA.close()
        main()

    elif opcion==2:
        def main2():
            borrar=(input("Que numero de IdEmpleado deseas borrar: "))
            archivoB=open("./archivos/Empleados.txt",'r')
            miarchivo = open("./archivos/Nuevo.txt",'x')
            miarchivo.close()
            miarchivo = open("./archivos/Nuevo.txt",'w')
            
            for renglon in archivoB:
                datosempleado = renglon.split('|')
                ide=datosempleado[0]
                nom=datosempleado[1]
                dire=datosempleado[2]
                
                if ide!=borrar:
                    miarchivo.write(ide + "|"+ nom + "|" + dire + "|" + "\n")

            archivoB.close()

            from os import remove
            remove("./archivos/Empleados.txt")

            miarchivo= open("./archivos/Nuevo.txt","r")
            archivodestino = open("./archivos/Empleados.txt","w")
            archivodestino.write(miarchivo.read())
            miarchivo.close()
            archivodestino.close()

            from os import remove
            remove("./archivos/Nuevo.txt")
        main2()


    elif opcion==3:
        pass






        



            




    
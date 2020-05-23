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
        archivoA=open("./archivos/Empleados.txt",'a')
        idEmpleado=(input("Ingrese su numero de Empleado: "))
        nombre=(input("Ingrese su Nombre: "))
        direccion=(input("Ingrese su Direccion: "))
        archivoA.write(idEmpleado + "|"+ nombre + "|" + direccion)
        archivoA.close()



    
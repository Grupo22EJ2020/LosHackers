print ("Bienvenido al Menu Principal")
print("Administrar Empleados=1")
print("Administrar Cursos=2")
print("Administrar Temas=3")
print("Administrar Videos=4")
print("Administrar de Temas asignados a un Curso=5")
print("Administracion de Videos asignado a un Tema=6")
Menu=int(input("Que opcion del MENU desea elegir: "))

if Menu==1:
    print("*"*40)
    print("SUBMENU")
    print("Agregar=1")
    print("Borrar=2")
    print("Modificar=3")
    print("Consultar Todo=4")
    print("*"*20)
    opcion=int(input("Que opcion elige: "))


    if opcion==1:
        def main():
            print("Eligio la opcion de Agregar")
            print("*"*40)
            archivoA=open("./archivos/Empleados.txt",'a')
            idEmpleado=(input("Ingrese su numero de Empleado: "))
            nombre=(input("Ingrese su Nombre: "))
            direccion=(input("Ingrese su Direccion: "))
            archivoA.write(idEmpleado + "|"+ nombre + "|" + direccion + "|" + "\n")
            archivoA.close()
        main()

    elif opcion==2:
        def main2():
            print("Eligio la opcion de Eliminar")
            print("*"*20)
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
        def main3():
            numero = 0
            print("Eligió la opcion de Modificar")
            print("*"*30)
            numero = input("Ingrese el numero del empleado que desea modificar: ")
            print("*"*30)
            archivoM = open("./archivos/Empleados.txt","r")
            lineas = archivoM.readlines()
            archivoM.close()
            archivoM = open("./archivos/Empleados.txt","w")

            for linea in lineas:
                if linea[0] == numero:
                    idEmpleado = (input("Ingrese su IdEmpleado nuevo: "))
                    nombre = (input("Ingrese su Nombre de Empleado nuevo: "))
                    direccion = (input("Ingrese su Direccion de Empleado nuevo: "))
                    archivoM.write(idEmpleado + "|" + nombre + "|" + direccion +"|"+ "\n")
                else:
                    archivoM.write(linea)
            archivoM.close()
        main3()
    
    elif opcion==4:
        def main4():
            contador=0
            print("Eligio la opción de mostrar todos los Empleados")
            print("*"*50)
            archivoT = open("./archivos/Empleados.txt")
            for linea in archivoT:
                linea = linea.rstrip("\n")
                contador=contador+1
                print(f"Numero de Registro {contador}  :  {linea}")
            archivoT.close()
        main4()

elif Menu==2:
    print("*"*40)
    print("SUBMENU")
    print("Agregar=1")
    print("Borrar=2")
    print("Modificar=3")
    print("Consultar Todo=4")
    print("*"*20)
    opcion=int(input("Que opcion elige: "))

    if opcion==1:
        def main():
            print("Eligio la opcion de Agregar")
            print("*"*40)
            archivoA=open("./archivos/Cursos.txt",'a')
            idCurso=(input("Ingrese su numero de id curso: "))
            Descripcion=(input("Ingrese su Descripcion: "))
            idempleado=(input("Ingrese su id empleado: "))
            archivoA.write(idCurso + "|"+ Descripcion + "|" + idempleado + "|" + "\n")
            archivoA.close()
        main()

    elif opcion==2:
        def main2():
            print("Eligio la opcion de Eliminar")
            print("*"*20)
            borrar=(input("Que numero de IdCurso deseas borrar: "))
            archivoB=open("./archivos/Cursos.txt",'r')
            miarchivo = open("./archivos/Nuevo.txt",'x')
            miarchivo.close()
            miarchivo = open("./archivos/Nuevo.txt",'w')
            
            for renglon in archivoB:
                datosempleado = renglon.split('|')
                idc=datosempleado[0]
                des=datosempleado[1]
                idE=datosempleado[2]
                
                if idc!=borrar:
                    miarchivo.write(idc + "|"+ des + "|" + idE + "|" + "\n")

            archivoB.close()

            from os import remove
            remove("./archivos/Cursos.txt")

            miarchivo= open("./archivos/Nuevo.txt","r")
            archivodestino = open("./archivos/Cursos.txt","w")
            archivodestino.write(miarchivo.read())
            miarchivo.close()
            archivodestino.close()

            from os import remove
            remove("./archivos/Nuevo.txt")
        main2()

    elif opcion==3:
        def main3():
            numero = 0
            print("Eligió la opcion de Modificar")
            print("*"*30)
            numero = input("Ingrese el numero del idCurso que desea modificar: ")
            print("*"*30)
            archivoM = open("./archivos/Cursos.txt","r")
            lineas = archivoM.readlines()
            archivoM.close()
            archivoM = open("./archivos/Cursos.txt","w")

            for linea in lineas:
                if linea[0] == numero:
                    idCurso = (input("Ingrese su IdCurso nuevo: "))
                    Descripcion = (input("Ingrese su Descripcion de Empleado nuevo: "))
                    idempleado = (input("Ingrese su id empleado nuevo: "))
                    archivoM.write(idCurso + "|" + Descripcion + "|" + idempleado +"|"+ "\n")
                else:
                    archivoM.write(linea)
            archivoM.close()
        main3()
    
    elif opcion==4:
        def main4():
            contador=0
            print("Eligio la opción de mostrar todos los Cursos")
            print("*"*50)
            archivoT = open("./archivos/Cursos.txt")
            for linea in archivoT:
                linea = linea.rstrip("\n")
                contador=contador+1
                print(f"Numero de Registro {contador}  :  {linea}")
            archivoT.close()
        main4()

elif Menu ==3:
    print("*"*40)
    print("SUBMENU")
    print("Agregar=1")
    print("Borrar=2")
    print("Modificar=3")
    print("Consultar Todo=4")
    print("*"*20)
    opcion=int(input("Que opcion elige: "))

    if opcion==1:
        def main():
            print("Eligio la opcion de Agregar")
            print("*"*40)
            archivoA=open("./archivos/Tema.txt",'a')
            idTema=(input("Ingrese su numero de Tema: "))
            Nombre=(input("Ingrese su Nombre: "))
            archivoA.write(idTema + "|"+ Nombre + "|" + "\n")
            archivoA.close()
        main()

    elif opcion==2:
        def main2():
            print("Eligio la opcion de Eliminar")
            print("*"*20)
            borrar=(input("Que numero de IdTema deseas borrar: "))
            archivoB=open("./archivos/Tema.txt",'r')
            miarchivo = open("./archivos/Nuevo.txt",'x')
            miarchivo.close()
            miarchivo = open("./archivos/Nuevo.txt",'w')
            
            for renglon in archivoB:
                datosempleado = renglon.split('|')
                idt=datosempleado[0]
                Nom=datosempleado[1]
                
                
                if idt!=borrar:
                    miarchivo.write(idt + "|"+ Nom + "|" + "\n")

            archivoB.close()

            from os import remove
            remove("./archivos/Tema.txt")

            miarchivo= open("./archivos/Nuevo.txt","r")
            archivodestino = open("./archivos/Tema.txt","w")
            archivodestino.write(miarchivo.read())
            miarchivo.close()
            archivodestino.close()

            from os import remove
            remove("./archivos/Nuevo.txt")
        main2()

    elif opcion==3:
        def main3():
            numero = 0
            print("Eligió la opcion de Modificar")
            print("*"*30)
            numero = input("Ingrese el numero del Tema que desea modificar: ")
            print("*"*30)
            archivoM = open("./archivos/Tema.txt","r")
            lineas = archivoM.readlines()
            archivoM.close()
            archivoM = open("./archivos/Tema.txt","w")

            for linea in lineas:
                if linea[0] == numero:
                    idTema = (input("Ingrese su IdTema nuevo: "))
                    Nombre = (input("Ingrese su Nombre del tema nuevo: "))
                    
                    archivoM.write(idTema + "|" + Nombre + "|" + "\n")
                else:
                    archivoM.write(linea)
            archivoM.close()
        main3()
     
    elif opcion==4:
        def main4():
            contador=0
            print("Eligio la opción de mostrar todos los Temas")
            print("*"*50)
            archivoT = open("./archivos/Tema.txt")
            for linea in archivoT:
                linea = linea.rstrip("\n")
                contador=contador+1
                print(f"Numero de Registro {contador}  :  {linea}")
            archivoT.close()
        main4()

elif Menu == 4:
    print("*"*40)
    print("SUBMENU")
    print("Agregar=1")
    print("Borrar=2")
    print("Modificar=3")
    print("Consultar Todo=4")
    print("*"*20)
    opcion=int(input("Que opcion elige: "))

    if opcion == 1:
        def main():
            print("Eligio la opcion de Agregar")
            print("*"*40)
            archivoA=open("./archivos/videos.txt",'a')
            idvideos=(input("Ingrese el numero del video: "))
            NOMBRE=(input("Ingrese el Nombre del video: "))
            Url=(input("Ingrese el url del video: "))
            FechaPub=(input("Ingrese la fecha publicacion del video: "))
            archivoA.write(idvideos + "|"+ NOMBRE + "|" + Url + "|" + FechaPub + "|" + "\n")
            archivoA.close()
        main()

    elif opcion == 2:
        def main2():
            print("Eligio la opcion de Eliminar")
            print("*"*20)
            borrar=(input("Que numero de idvideo deseas borrar: "))
            archivoB=open("./archivos/videos.txt",'r')
            miarchivo = open("./archivos/Nuevo.txt",'x')
            miarchivo.close()
            miarchivo = open("./archivos/Nuevo.txt",'w')
            
            for renglon in archivoB:
                datosvideo = renglon.split('|')
                idv=datosvideo[0]
                NOM=datosvideo[1]
                url=datosvideo[2]
                fechaPub=datosvideo[3]
                
                if idv!=borrar:
                    miarchivo.write(idv + "|"+ NOM + "|" + url + "|" + fechaPub + "|" + "\n")

            archivoB.close()

            from os import remove
            remove("./archivos/videos.txt")

            miarchivo= open("./archivos/Nuevo.txt","r")
            archivodestino = open("./archivos/videos.txt","w")
            archivodestino.write(miarchivo.read())
            miarchivo.close()
            archivodestino.close()

            from os import remove
            remove("./archivos/Nuevo.txt")
        main2()

    elif opcion == 3:
        def main3():
            numero = 0
            print("Eligió la opcion de Modificar")
            print("*"*30)
            numero = input("Ingrese el numero del video que desea modificar: ")
            print("*"*30)
            archivoM = open("./archivos/videos.txt","r")
            lineas = archivoM.readlines()
            archivoM.close()
            archivoM = open("./archivos/videos.txt","w")

            for linea in lineas:
                if linea[0] == numero:
                    idvideos = (input("Ingrese el idvideo nuevo: "))
                    NOM = (input("Ingrese el nombre del video nuevo: "))
                    Url = (input("Ingrese el url del video nuevo: "))
                    FechaPub = (input("Ingrese la fecha de publicacion nueva: "))
                    archivoM.write(idvideos + "|" + NOM + "|" + Url + "|" + FechaPub + "|" + "\n")
                else:
                    archivoM.write(linea)
            archivoM.close()
        main3()

    elif opcion == 4:
        def main4():
            contador=0
            print("Eligio la opción de mostrar todos los Videos")
            print("*"*50)
            archivoT = open("./archivos/videos.txt")
            for linea in archivoT:
                linea = linea.rstrip("\n")
                contador=contador+1
                print(f"Numero de Registro {contador}  :  {linea}")
            archivoT.close()
        main4()

elif Menu==5:
    print("*"*40)
    print("SUBMENU")
    print("Agregar=1")
    print("Borrar=2")
    print("Modificar=3")
    print("Consultar Todo=4")
    print("*"*20)
    opcion=int(input("Que opcion elige: "))

    if opcion==1:
        def main():
            print("Eligio la opcion de Agregar")
            print("*"*40)
            archivoA=open("./archivos/Curso_Tema.txt",'a')
            idCursoTe=(input("Ingrese su numero de Id Curso Tema : "))
            idCurso=(input("Ingrese su Id Curso: "))
            IDTema=(input("Ingrese su Id Tema: "))
            archivoA.write(idCursoTe + "|"+ idCurso+ "|" + IDTema + "|" + "\n")
            archivoA.close()
        main()

    elif opcion==2:
        def main2():
            print("Eligio la opcion de Eliminar")
            print("*"*20)
            borrar=(input("Que numero de Id Curso Tema deseas borrar: "))
            archivoB=open("./archivos/Curso_Tema.txt",'r')
            miarchivo = open("./archivos/Nuevo.txt",'x')
            miarchivo.close()
            miarchivo = open("./archivos/Nuevo.txt",'w')
            
            for renglon in archivoB:
                datosCursoTema = renglon.split('|')
                idCT=datosCursoTema[0]
                IDCURSO=datosCursoTema[1]
                IDtema=datosCursoTema[2]
                
                if idCT!=borrar:
                    miarchivo.write(idCT + "|"+ IDCURSO + "|" + IDtema + "|" + "\n")

            archivoB.close()

            from os import remove
            remove("./archivos/Curso_Tema.txt")

            miarchivo= open("./archivos/Nuevo.txt","r")
            archivodestino = open("./archivos/Curso_Tema.txt","w")
            archivodestino.write(miarchivo.read())
            miarchivo.close()
            archivodestino.close()

            from os import remove
            remove("./archivos/Nuevo.txt")
        main2()

    elif opcion==3:
        def main3():
            numero = 0
            print("Eligió la opcion de Modificar")
            print("*"*30)
            numero = input("Ingrese el numero de Id Curso Tema que desea modificar: ")
            print("*"*30)
            archivoM = open("./archivos/Curso_Tema.txt","r")
            lineas = archivoM.readlines()
            archivoM.close()
            archivoM = open("./archivos/Curso_Tema.txt","w")

            for linea in lineas:
                if linea[0] == numero:
                    IdCursoTe = (input("Ingrese su Id Curso Tema nuevo: "))
                    IdCurso = (input("Ingrese su Id Curso nuevo: "))
                    IdTema = (input("Ingrese su Id Tema nuevo: "))
                    archivoM.write(IdCursoTe + "|" + IdCurso + "|" + IdTema +"|"+ "\n")
                else:
                    archivoM.write(linea)
            archivoM.close()
        main3()

    elif opcion==4:
        def main4():
            contador=0
            print("Eligio la opción de mostrar todos los Cursos Temas")
            print("*"*50)
            archivoT = open("./archivos/Curso_Tema.txt")
            for linea in archivoT:
                linea = linea.rstrip("\n")
                contador=contador+1
                print(f"Numero de Registro {contador}  :  {linea}")
            archivoT.close()
        main4()

elif Menu==6:
    print("*"*40)
    print("SUBMENU")
    print("Agregar=1")
    print("Borrar=2")
    print("Modificar=3")
    print("Consultar Todo=4")
    print("*"*20)
    opcion=int(input("Que opcion elige: "))

    if opcion==1:
        def main():
            print("Eligio la opcion de Agregar")
            print("*"*40)
            archivoA=open("./archivos/Curso_Tema_Video.txt",'a')
            idCursoTv=(input("Ingrese su numero de Id Curso Tema Video: "))
            idCT=(input("Ingrese su Id Curso Tema: "))
            idVideo=(input("Ingrese su Id Video: "))
            archivoA.write(idCursoTv + "|"+ idCT + "|" + idVideo + "|" + "\n")
            archivoA.close()
        main()

    elif opcion==2:
        def main2():
            print("Eligio la opcion de Eliminar")
            print("*"*20)
            borrar=(input("Que numero de Id Curso Tema Video deseas borrar: "))
            archivoB=open("./archivos/Curso_Tema_Video.txt",'r')
            miarchivo = open("./archivos/Nuevo.txt",'x')
            miarchivo.close()
            miarchivo = open("./archivos/Nuevo.txt",'w')
            
            for renglon in archivoB:
                datosCursoTemaVideo = renglon.split('|')
                idctv=datosCursoTemaVideo[0]
                idCT=datosCursoTemaVideo[1]
                idv=datosCursoTemaVideo[2]
                
                if idctv!=borrar:
                    miarchivo.write(idctv + "|"+ idCT + "|" + idv + "|" + "\n")

            archivoB.close()

            from os import remove
            remove("./archivos/Curso_Tema_Video.txt")

            miarchivo= open("./archivos/Nuevo.txt","r")
            archivodestino = open("./archivos/Curso_Tema_Video.txt","w")
            archivodestino.write(miarchivo.read())
            miarchivo.close()
            archivodestino.close()

            from os import remove
            remove("./archivos/Nuevo.txt")
        main2()

    elif opcion==3:
        def main3():
            numero = 0
            print("Eligió la opcion de Modificar")
            print("*"*30)
            numero = input("Ingrese el numero del Curso Tema Video que desea modificar: ")
            print("*"*30)
            archivoM = open("./archivos/Curso_Tema_Video.txt","r")
            lineas = archivoM.readlines()
            archivoM.close()
            archivoM = open("./archivos/Curso_Tema_Video.txt","w")

            for linea in lineas:
                if linea[0] == numero:
                    idCursoTV = (input("Ingrese su Id Curso Tema Video nuevo: "))
                    idCT = (input("Ingrese su Id Curso Tema nuevo: "))
                    idVideo = (input("Ingrese Id Video nuevo: "))
                    archivoM.write(idCursoTV + "|" + idCT + "|" + idVideo +"|"+ "\n")
                else:
                    archivoM.write(linea)
            archivoM.close()
        main3()

    elif opcion==4:
        def main4():
            contador=0
            print("Eligio la opción de mostrar todos los Cursos Temas Videos")
            print("*"*50)
            archivoT = open("./archivos/Curso_Tema_Video.txt")
            for linea in archivoT:
                linea = linea.rstrip("\n")
                contador=contador+1
                print(f"Numero de Registro {contador}  :  {linea}")
            archivoT.close()
        main4()




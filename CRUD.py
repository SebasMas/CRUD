tareas = []
continuar = True
while continuar:
  print("!!!INGRESE 5 TAREAS!!!")
  print("1 - Registrar Tarea")
  print("2 - Lista de Tareas")
  print("3 - Modificar Tareas")
  print("4 - Eliminar Tareas")
  print("5 - Tiempo promedio de las tareas registradas")
  print("6 - Tarea con mas duracion")
  print("7 - Tarea con menos duracion")
  print("8 - El numero de tareas que no requiren desplazamiento")
  opcion = int(input("Ingrese la opcion: "))
  if opcion == 1:
    tarea = input("Ingrese la tarea a registrar: ")
    tiempo = int(input("Ingrese el tiempo en minutos que tomara esta tarea: "))
    desplazamiento = int(input("¿Esta tarea requiere desplazamiento (1 o 2): "))
    tareas.append([tarea, tiempo, desplazamiento])
    print("--------------------------------------------------")
  elif opcion == 2:
    print("Tareas registradas")
    for i, tarea in enumerate (tareas):
        mostrarDesplazamiento = "No"
        if tarea[2] == 1:
            mostrarDesplazamiento = "Si"
        print(f"{i} - Descripcion: {tarea[0]} Duracion: {tarea[1]} Desplazamiento: {mostrarDesplazamiento} ")
    print("--------------------------------------------------")
  elif opcion == 3:
    for i, tarea in enumerate (tareas):
        mostrarDesplazamiento = "No"
        if tarea[2] == 1:
            mostrarDesplazamiento = "Si"
        print(f"{i} - Descripcion: {tarea[0]} Duracion: {tarea[1]} Desplazamiento: {mostrarDesplazamiento} ")
    print("--------------------------------")
    codigo = int(input("Ingrese el codigo de la tarea:  "))
    if(codigo>len(tareas)):
      print("Tarea no encontrada")
    else:
      nuevatarea = input("Ingrese la nueva tarea: ")
      if(nuevatarea != " "):
        tareas[codigo][0] = nuevatarea
      nuevotiempo = input("Ingrese el nuevo tiempo para la tarea: ")
      if(nuevotiempo != " "):
        tareas[codigo][1] = nuevotiempo
      nuevodesplazamiento = int(input("Actualice el desplazamiento (1 para si - 2 para no: "))
      if(nuevodesplazamiento != " "):
        tareas[codigo][2]
      for i, tarea in enumerate(tareas):
        print(i, " ", tarea)
        print("--------------------------------------------------")
  elif opcion == 4:
    print("Pasos para eliminar")
    for i, tarea in enumerate(tareas):
      print(i, " ", tarea)
    print("------------------------------------")
    codigo = int(input("Ingrese el codigo de la tarea a eliminar: "))
    if(codigo>len(tareas)):
      print("Tarea no encontrada!!!!")
    else:
      tareaeliminada = tareas.pop(codigo)
      print("La tarea", tareaeliminada, "ha sido eliminada" )
      print("-----------------------------------")
      for i, tarea in enumerate(tareas):
        print(i, " ", tarea) 
      print("------------------------------------")
  elif opcion == 5 :
       print(tareas)
       tiempos= [int(input("Ingrese el  tiempo de la primera tarea: ")), int(input("Ingrese el  tiempo de la segunda tarea: ")), int(input("Ingrese el  tiempo de la tercera tarea: ")), int(input("Ingrese el  tiempo de la cuarta tarea: ")),int(input("Ingrese el  tiempo de la quinta tarea: "))]
       print("La suma de todos los tiempos es: ", sum(tiempos))
       promedio = (sum(tiempos)/len(tiempos))
       print("El promedio de todos los tiempos es: ", (promedio)) 
       print("--------------------------------------------------------")
  elif opcion == 6 :
      listadetiempos = []
      for tarea in tareas:
        listadetiempos.append(tarea[1])
      maxtiempo = max(listadetiempos)
      print(maxtiempo)
    
  elif opcion == 7:
      listadetiempos = []
      for tarea in tareas:
        listadetiempos.append(tarea[1])
      mintiempo = min(listadetiempos)
      print(mintiempo)
  elif opcion == 8:
      listadedesplazamientos = []
      for tarea in tareas:
        if tarea[2] == 2:
         listadedesplazamientos.append(tarea[2])
      print(len(listadedesplazamientos))
       

        
       
      
                          
       


       

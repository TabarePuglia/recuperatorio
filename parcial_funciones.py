import os
#from os import *
import datetime
import json

lista_proyecto = [{"id":1,"nombre":"Pora","descripcion":"Cancha de futbol","fecha de inicio":"20/08/2020","fecha de fin":"10/10/2021","presupuesto":500000,"estado":"Activo"},
                  {"id":2,"nombre":"Winer","descripcion":"Cancha de futbol","fecha de inicio":"01/07/2010","fecha de fin":"30/03/2021","presupuesto":200000,"estado":"Finalizado"},
                  {"id":3,"nombre":"Union","descripcion":"Cancha de futbol","fecha de inicio":"20/11/2015","fecha de fin":"30/11/2023","presupuesto":300000,"estado":"Activo"},
                  {"id":4,"nombre":"Boca","descripcion":"Cancha de futbol","fecha de inicio":"20/11/2020","fecha de fin":"31/12/2020","presupuesto":300000,"estado":"Finalizado"},
                  {"id":5,"nombre":"Agropecuarios","descripcion":"Cancha de futbol","fecha de inicio":"20/01/2012","fecha de fin":"30/10/2021","presupuesto":300000,"estado":"Cancelado"}]
  


def cantidad_de_proyectos(proyectos:dict)->bool: #Funcion que verifica si la lista tiene menos de 50 proyectos
    bandera = True
    if len(proyectos) >= 50:
        print("Se a alcanzado el numero maximo de proyectos")
        bandera = False
    return bandera


def imprimir_menu(): #funcion que imprime el menu
    print("\nSeleccione una opción:")
    print("1. Ingresar un proyecto")
    print("2. Modificar un proyecto")
    print("3. cancelar un proyecto")
    print("4. Comprobar proyectos")
    print("5. Mostrar proyectos")
    print("6. Calcular promedio")
    print("7. Buscar proyecto por nombre")
    print("8. Ordenar proyecto")
    print("9. retomar proyecto")
    print("10. Reporte de presupuesto")
    print("11. Reporte por nombre")
    print("12. Mostrar Proyectos terminados en pandemia")
    print("13. Mostrar proyectos que duraron menos de 3 años")
    print("14. Salir")

def validar_opcion(mensaje, mensaje_error): #valida si el usuario ingreso una opcion valida
    opcion = input(mensaje)
    opcion = int(opcion)
    while opcion > 14 or opcion < 1:
        opcion = input(mensaje_error)
        opcion = int(opcion)
    return opcion


def validar_nombre_apellido(mensaje,mensaje_error)->str: #Esta es una funcion que valida que un str tenga solo 
    dato = input(mensaje)
    dato = dato.replace(" ","")                                 #caracteres alfabeticos
    while len(dato) == 0 or len(dato) > 30 or (not dato.isalpha()):
        dato = input(mensaje_error)
        dato = dato.replace(" ","")    
    dato = dato.capitalize()
    return dato

def validar_texto_alphanumerico(cadena:str)->bool: #Esta funcion valida si un texto es alphanumerico
    aux = cadena.replace(" ","")     
    if aux.isalnum():
        bandera = True
    else:
        bandera = False
    return bandera


def validar_descripcion(mensaje,mensaje_error)->str: #Esta funcion valida si la descripcion es valida
    dato = input(mensaje)
    aux = validar_texto_alphanumerico(dato)
    while len(dato) == 0 or len(dato) > 200 or (not aux):
        dato = input(mensaje_error)
        aux = validar_texto_alphanumerico(dato)
    dato = dato.capitalize()
    return dato
            
#print(validar_descripcion("BLA BLAA BLA DESCRIPCION :","Esto ta mal :"))
#print(validar_texto_alphanumerico("asdsa2323%$%$"))
#print(validar_nombre_apellido("Escribi aca:","Esto ta mal :"))

def validar_presupuesto(mensaje,mensaje_error)->int: #valida si el presupuesto es un numero y si esta dentro de los parametros
    
    presupuesto = input(mensaje)
    while not (presupuesto.isdigit() and int(presupuesto) >= 50000):
        presupuesto = input(mensaje_error)
    return int(presupuesto)

#print(validar_presupuesto("Presupuesto :","Error, reingrese el presupuesto :"))


def validar_estado(mensaje , mensaje_error)->str: #valida si el estado es alguno de los definidos
    estado = input(mensaje)
    estado = estado.capitalize()
    
    while estado != "Activo" and estado != "Finalizado" and estado != "Cancelado":
        estado = input(mensaje_error)
        estado = estado.capitalize()
    return estado

def ingresar_fecha(): #Valida una fecha ingresada por el usuario
    dia = input("Ingrese el dia (1-31): ")
    while (not dia.isdigit()) or int(dia) == 0 or int(dia) > 31:
        dia = input("ERROR, Ingrese un dia valido (1-31): ")
    dia = int(dia)
    mes = input("Ingrese el mes (1-12): ")
    while (not mes.isdigit()) or int(mes) == 0 or int(mes) > 12:
        mes = input("ERROR, Ingrese un mes valido (1-12): ") 
    anio = input("Ingrese el año: ")
    while (not anio.isdigit()) or int(anio) == 0 or int(anio) < 2000:
        anio = input("ERROR, Ingrese un año valido: ")

    fecha = f"{dia}/{mes}/{anio}"
    return fecha

def comparar_fechas(fecha_inicio:str,fecha_fin:str)-> bool: # compara 2 fechas y valida si la fecha de fin es mayor a la de inicio
    bandera = True
    fecha_inicio = fecha_inicio.split("/")
    fecha_fin = fecha_fin.split("/")
    for i in range(0,2):
        fecha_fin[i] = int(fecha_fin[i])
        fecha_inicio[i] = int(fecha_inicio[i])
    if fecha_inicio[2] > fecha_fin[2]:
        bandera = False
    else:
        if fecha_inicio[2] == fecha_fin[2]:
            if fecha_inicio[1] > fecha_fin[1]:
                bandera = False
            else:
                if fecha_inicio[1] == fecha_fin[1]:
                    if fecha_inicio[0] > fecha_fin[0]:
                        bandera = False
        return bandera

def validar_id(mensaje,mensaje_error): # valida si el id es un digito
    id = input(mensaje)

    while not (id.isdigit()):
        id =input(mensaje_error)
    id = int(id)
    return id

#print(validar_id("ingrese id","Error, ingrese un id valido"))


#print(validar_fecha())
def mostrar_proyecto (proyecto:dict,informacion): # muestra un proyecto
    for clave in proyecto:            
        informacion += str(proyecto[clave]) + " | "  
    print(informacion)

def mostrar_proyectos(lista_proyectos:dict): # muestra una lista de proyectos
    print ("PROYECTO\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO |\n")
    for proyecto in lista_proyectos:
        mostrar_proyecto(proyecto,"")


def confirmar_si_no(mensaje,mensaje_error)->bool: # valida si el usuario quiere seguir con la funcion
    respuesta = input(mensaje)
    respuesta = respuesta.lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input(mensaje_error)
        respuesta = respuesta.lower()
    if respuesta == "si":
        return True
    else:
        return False


def ingresar_proyecto(lista_proyectos:list,id): #funcion para ingresar un proyecto
    bandera = True
    if cantidad_de_proyectos(lista_proyectos):
        proyecto = {}
        id_proyecto = id
        nombre = validar_nombre_apellido("Ingrese nombre del nuevo proyecto: ","ERROR, Ingrese un nombre correcto: ")
        descripcion = validar_descripcion("Ingrese la descripcion del proyecto: ","ERROR, Ingrese una descripcion valida: ")
        print("Fecha de inicio")
        fecha_inicio = ingresar_fecha()
        print("Fecha de finalizacion")
        fecha_fin = ingresar_fecha()
        while (not comparar_fechas(fecha_inicio,fecha_fin)):
            print("ERROR, no puede finalizar antes de iniciar")
            fecha_fin = ingresar_fecha()    
        presupuesto = validar_presupuesto("Ingrese el presupuesto del proyecto: ","ERROR, Ingrese un presupuesto valido: ")
        estado = validar_estado("Ingrese el estado el protecto(Activo-Finalizado-cancelado): ","ERROR,Ingrese un estado valido (Activo-Finalizado-cancelado): ")
        proyecto["id"] = id_proyecto
        proyecto["nombre"] = nombre
        proyecto["descripcion"] = descripcion
        proyecto["fecha de inicio"] = fecha_inicio
        proyecto["fecha de fin"] = fecha_fin
        proyecto["presupuesto"] = presupuesto
        proyecto["estado"] = estado
        print("PROYECTO\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO |\n")
        mostrar_proyecto(proyecto,"")
        if confirmar_si_no("¿Desea ingresar el nuevo Proyecto? Si o no : ","Ingrese una respuesta valida"):
            lista_proyectos.append(proyecto)
        else:
            print("Se cancelo el ingreso")
            bandera = False
    else:
        bandera = False

    return bandera

#print(lista_proyecto)
#fecha_inicio = ingresar_fecha()
#fecha_fin = ingresar_fecha()
#print(fecha_inicio)
#print(comparar_fechas(fecha_inicio,fecha_fin))
#mostrar_proyecto(lista_proyecto,"PROYECTO\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO |\n")

def buscar_proyecto(lista_proyectos:list,id_proyecto:int)->int: #busca un proyecto en la lista segun su id
    indice = None
    for proyecto in range(len(lista_proyectos)):
        for dato in lista_proyectos[proyecto]:
            if dato == "id":
                aux = lista_proyectos[proyecto][dato]
                aux = int(aux)
                if aux == id_proyecto:
                    indice = proyecto
                    
                    break
        
    return indice

#print(buscar_proyecto(lista_proyecto,2))

def mostrar_datos_modificables(): #Muestra los datos que se pueden modificar
    print("1. Nombre")
    print("2. Descripcion")
    print("3. Fecha de inicio")
    print("4. Fecha de fin")
    print("5. Presupuesto")
    print("6. Estado")
    print("7. salir")

def validar_dato_modificable(mensaje,mensaje_error)->int: #valida si el dato a modificar esta dentro de los parametros
    mostrar_datos_modificables()
    dato = input(mensaje)
    while not (dato.isdigit() and int(dato) < 8):
        mostrar_datos_modificables()
        dato = input(mensaje_error)
    return int(dato)

def modificar_proyecto(lista_proyectos:list,id_proyecto:int): #funcion para modificar un proyecto pasando su id
    bandera = True
    indice = buscar_proyecto(lista_proyectos,id_proyecto)
    if not indice == None:     
        while bandera:
            aux = lista_proyectos[indice]
            print("PROYECTO\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO |\n")
            mostrar_proyecto(aux,"")
            dato_a_modificar = validar_dato_modificable("Ingrese dato a modificar :","ERROR, Ingrese un dato valido")
            match dato_a_modificar:
                case 1:
                        modificacion = validar_nombre_apellido("Ingrese nombre del nuevo proyecto: ","ERROR, Ingrese un nombre correcto: ")
                        clave = "nombre"
                case 2:
                            modificacion = validar_descripcion("Ingrese la descripcion del proyecto: ","ERROR, Ingrese una descripcion valida: ")
                            clave = "descripcion"
                case 3:
                        print("Fecha de inicio")
                        modificacion = ingresar_fecha()
                        while comparar_fechas(lista_proyectos[indice]["fecha de fin"],modificacion):
                            modificacion = ingresar_fecha()
                        clave = "fecha de inicio"
                case 4:
                        print("Fecha de fin")
                        modificacion = ingresar_fecha()
                        while (not comparar_fechas(lista_proyectos[indice]["fecha de inicio"],modificacion)):
                                print("ERROR, no puede finalizar antes de iniciar")
                                print("Fecha de fin")
                                modificacion = ingresar_fecha()
                        clave = "fecha de fin"
                case 5:
                        modificacion = validar_presupuesto("Ingrese el presupuesto del proyecto: ","ERROR, Ingrese un presupuesto valido: ")  
                        clave = "presupuesto"
                case 6:  
                        modificacion = validar_estado("Ingrese el estado el protecto(Activo-Finalizado-cancelado): ","ERROR,Ingrese un estado valido (Activo-Finalizado-cancelado): ")
                        clave = "estado"
                case 7:
                        print("Saliendo")
                        break
            lista_proyectos[indice][clave] = modificacion
            print("El proyecto se modifico correctamente")
    else:
        print("NO se encontro proyecto")
    return lista_proyectos
        
#print(modificar_proyecto(lista_proyecto,2))

def cancelar_proyecto(lista_proyectos:dict,id_proyecto): #funcion para cancelar un proyecto pasando su id
    bandera = True
    indice = buscar_proyecto(lista_proyectos,id_proyecto)
    if not indice == None:
        if confirmar_si_no("Esta seguro de cancelar este proyecto: ","Dato invalido,esta seguro: "):
            lista_proyectos[indice]["estado"] = "Cancelado"
            print("Estado modificado a :Cancelado")
        else:
            ("Se cancelo la funcion")
    else:
         print("Se cancelo la funcion")
    return lista_proyectos

#print(cancelar_proyecto(lista_proyecto,3))

def actualizar_fecha_lista(lista_proyectos,fecha_hoy): # funcion para actualizar todos los proyectos activos que su fecha de finalizacion haya pasado
    contador = 0
    for proyecto in range(len(lista_proyectos)):
       if not(comparar_fechas(fecha_hoy, lista_proyectos[proyecto]["fecha de fin"])):
            if lista_proyectos[proyecto]["estado"] != "Cancelado":
                lista_proyectos[proyecto]["estado"] = "Finalizado"
                contador += 1
    print(f"Se actualizaron {contador} proyectos")
    
    return lista_proyectos

#fecha_hoy = datetime.date.today()
#fecha_hoy = fecha_hoy.strftime("%d/%m/%Y")
#print(actualizar_fecha_lista(lista_proyecto,fecha_hoy))


def calcular_promedio_presupuesto(lista_proyectos): #funcion para calcular el promedio de los proyectos
    acumulador = 0
    contador = 0
    for proyecto in range(len(lista_proyectos)):
        aux = lista_proyectos[proyecto]["presupuesto"]
        aux = int(aux)
        acumulador += aux
        contador += 1
    promedio = acumulador/contador
    promedio = int(promedio)
    print(f"El promedio de los presupuestos de {contador} proyectos es {promedio}")


def buscar_por_nombre(lista_proyectos:list): #funcion para buscar un proyecto por su nombre
    indice = None
    nombre = validar_nombre_apellido("Ingrese el nombre a buscar: ","Error, Ingrese un nombre valido: ")
    nombre = nombre.replace(" ","")
    nombre = nombre.lower()
    for proyecto in range(len(lista_proyectos)):
        for dato in lista_proyectos[proyecto]:
            if dato == "nombre":
                aux = lista_proyectos[proyecto][dato]
                aux = aux.replace(" ","")
                aux = aux.lower()
                if aux == nombre:
                    indice = proyecto
    return indice

def mostrar_un_proyecto(lista_proyectos, indice): #Muestra un solo proyecto
    print ("PROYECTO\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO |\n")
    proyecto = lista_proyectos[indice]
    mostrar_proyecto(proyecto,"")


#print(buscar_por_nombre(lista_proyecto))
def mostrar_menu_ordenar(): #Muestra los datos por los que se pueden ordenar
    print("1. Nombre")
    print("2. presupuesto") 
    print("3. fecha de inicio") 

def mostrar_forma_ordenar(): #Muestra las formas en la que se puede ordenar
    print("1. de mayor a menor")
    print("2. de menor a mayor")  


def ordenar_proyectos(lista_proyectos)-> dict: # ordena la lista por los parametros pasados
    mostrar_menu_ordenar()
    indice = input("Ingrese la forma de ordenar :")
    while (not indice.isdigit()) and (indice > 4 or indice < 1):
         modo =input("Error, Ingrese el modo de ordenar :")
    indice = int(indice)
    mostrar_forma_ordenar()
    modo = input("Ingrese el modo de ordenar :")
    while (not modo.isdigit()) and (modo > 3 or modo < 1):
        mostrar_forma_ordenar()
        indice = input("Error, Ingrese la forma de ordenar :")
    modo = int(modo)
    match modo:
        case 1:
            match indice:
                case 1:
                    for i in range(len(lista_proyectos)):
                        for j in range(i+1,len(lista_proyectos),1):
                            if(lista_proyectos[i]["nombre"] < lista_proyectos[j]["nombre"]):
                                aux = lista_proyectos[i]
                                lista_proyectos[i] = lista_proyectos[j]
                                lista_proyectos[j] = aux
                case 2:
                    for i in range(len(lista_proyectos)):
                        for j in range(i+1,len(lista_proyectos),1):
                            if(lista_proyectos[i]["presupuesto"] < lista_proyectos[j]["presupuesto"]):
                                aux = lista_proyectos[i]
                                lista_proyectos[i] = lista_proyectos[j]
                                lista_proyectos[j] = aux
                case 3:
                        for i in range(len(lista_proyectos)):
                            fecha_inicio = lista_proyectos[i]["fecha de inicio"]
                            fecha_inicio = fecha_inicio.split("/")
                            for j in range(i+1,len(lista_proyectos),1):
                                fecha_fin = lista_proyectos[j]["fecha de inicio"]
                                fecha_fin = fecha_fin.split("/")
                                for f in range(0,2):
                                    fecha_fin[f] = int(fecha_fin[f])
                                    fecha_inicio[f] = int(fecha_inicio[f])
                                if fecha_inicio[2] < fecha_fin[2]:
                                    aux = lista_proyectos[i]
                                    lista_proyectos[i] = lista_proyectos[j]
                                    lista_proyectos[j] = aux
                                elif fecha_inicio[2] == fecha_fin[2]:
                                    if fecha_inicio[1] < fecha_fin[1]:
                                        aux = lista_proyectos[i]
                                        lista_proyectos[i] = lista_proyectos[j]
                                        lista_proyectos[j] = aux
                                    elif fecha_inicio[1] == fecha_fin[1]:
                                        if fecha_inicio[0] < fecha_fin[0]:
                                            aux = lista_proyectos[i]
                                            lista_proyectos[i] = lista_proyectos[j]
                                            lista_proyectos[j] = aux
        case 2:
            match indice:
                case 1:
                    for i in range(len(lista_proyectos)):
                        for j in range(i+1,len(lista_proyectos),1):
                            if(lista_proyectos[i]["nombre"] > lista_proyectos[j]["nombre"]):
                                aux = lista_proyectos[i]
                                lista_proyectos[i] = lista_proyectos[j]
                                lista_proyectos[j] = aux
                case 2:
                    for i in range(len(lista_proyectos)):
                        for j in range(i+1,len(lista_proyectos),1):
                            if(lista_proyectos[i]["presupuesto"] > lista_proyectos[j]["presupuesto"]):
                                aux = lista_proyectos[i]
                                lista_proyectos[i] = lista_proyectos[j]
                                lista_proyectos[j] = aux
                case 3:
                        for i in range(len(lista_proyectos)):
                            fecha_inicio = lista_proyectos[i]["fecha de inicio"]
                            fecha_inicio = fecha_inicio.split("/")
                            for j in range(i+1,len(lista_proyectos),1):
                                fecha_fin = lista_proyectos[j]["fecha de inicio"]
                                fecha_fin = fecha_fin.split("/")
                                for f in range(0,2):
                                    fecha_fin[f] = int(fecha_fin[f])
                                    fecha_inicio[f] = int(fecha_inicio[f])
                                if fecha_inicio[2] > fecha_fin[2]:
                                    aux = lista_proyectos[i]
                                    lista_proyectos[i] = lista_proyectos[j]
                                    lista_proyectos[j] = aux
                                elif fecha_inicio[2] == fecha_fin[2]:
                                    if fecha_inicio[1] > fecha_fin[1]:
                                        aux = lista_proyectos[i]
                                        lista_proyectos[i] = lista_proyectos[j]
                                        lista_proyectos[j] = aux
                                    elif fecha_inicio[1] == fecha_fin[1]:
                                        if fecha_inicio[0] > fecha_fin[0]:
                                            aux = lista_proyectos[i]
                                            lista_proyectos[i] = lista_proyectos[j]
                                            lista_proyectos[j] = aux
    return lista_proyectos

def retomar_proyecto(lista_proyectos,fecha_hoy)-> dict: #funcion para retomar un proyecto el cual su fecha de finalizacion no haya pasado
    id_a_buscar = validar_id("Ingrese el id del proyecto a retomar : ","Erro, Ingrese un id valido : ")
    proyecto = buscar_proyecto(lista_proyectos,id_a_buscar)
    if lista_proyectos[proyecto]["estado"] == "Cancelado":
        fecha_fin = lista_proyectos[proyecto]["fecha de fin"]
        if comparar_fechas(fecha_hoy,fecha_fin):
            print("2")
            lista_proyectos[proyecto]["estado"] = "Activo"
            print("Se modifico el estado a Activo")
    return lista_proyectos

#print(ordenar_proyectos(lista_proyecto))

#print(retomar_proyecto(lista_proyecto,fecha_hoy))
#print(buscar_proyecto(lista_proyecto,0))

def listar_csv(nombre_archivo): #convierte un archivo csv a lista
    """
    Recibe como parametro la dirección relativa de un archivo CSV y devuelve
    el contenido como una lista de diccionarios
    """
    with open(nombre_archivo,"r",encoding="utf-8") as archivo:
        lista_archivo = archivo.readlines()
        csv_listado =[]
        if len(lista_archivo) != 0:
            claves = (lista_archivo[0].replace("\n","")).split(",")
            for i in range(1,len(lista_archivo),1):
                aux ={}
                datos = (lista_archivo[i].replace("\n","")).split(",")
                for j in range(len(claves)):
                    aux[claves[j]] = datos[j]
                csv_listado.append(aux)
        return csv_listado
lista = listar_csv("Proyectos.csv") 

def normalizar_datos(lista_csv)-> dict: #normaliza los datos en el formato a trabajar
    if len(lista_csv) != 0:
        for proyecto in range(len(lista_csv)):
            id = lista_csv[proyecto]["id"]
            presupuesto =lista_csv[proyecto]["presupuesto"]
            presupuesto = presupuesto.replace("$","")
            fecha_inicio = lista_csv[proyecto]["fecha de inicio"]
            fecha_fin = lista_csv[proyecto]["fecha de fin"]
            fecha_inicio = fecha_inicio.split("-")
            fecha_fin = fecha_fin.split("-")
            lista_csv[proyecto]["presupuesto"] = int(presupuesto)
            lista_csv[proyecto]["id"] = int(id)
            lista_csv[proyecto]["fecha de inicio"] = f"{fecha_inicio[0]}/{fecha_inicio[1]}/{fecha_inicio[2]}"
            lista_csv[proyecto]["fecha de fin"] = f"{fecha_fin[0]}/{fecha_fin[1]}/{fecha_fin[2]}"
    return lista_csv

def desnormalizar_datos(lista_proyectos): #vuelve los datos a su estado original
    if len(lista_proyectos) != 0:
        for proyecto in range(len(lista_proyectos)):
                fecha_inicio = lista_proyectos[proyecto]["fecha de inicio"]
                fecha_fin = lista_proyectos[proyecto]["fecha de fin"]
                fecha_inicio = fecha_inicio.replace("/","-")
                fecha_fin = fecha_fin.replace("/","-")
                presupuesto_aux = f"$"
                presupuesto = str(lista_proyectos[proyecto]["presupuesto"])
                presupuesto_final = presupuesto_aux + presupuesto
                lista_proyectos[proyecto]["presupuesto"] = presupuesto_final
                lista_proyectos[proyecto]["fecha de inicio"] = fecha_inicio
                lista_proyectos[proyecto]["fecha de fin"] = fecha_fin
    return lista_proyectos

#print(desnormalizar_datos(lista_proyecto))
#print(normalizar_datos(lista))
def guardar_datos(lista_proyectos,nombre_archivo): #convierte una lista a archivo csv 
    if len(lista_proyectos) != 0:
        claves = lista_proyectos[0].keys()
        primer_linea = (",").join(list(lista_proyecto[0].keys()))
        primer_linea += "\n"
        lista_archivo = [primer_linea]
        for i in range(0,len(lista_proyectos),1):
            cadena = ""
            for clave in claves:

                if clave == "estado":
                    if i +1 != len(lista_proyectos):
                        cadena += f"{lista_proyectos[i][clave]}\n"
                    else:
                        cadena += f"{lista_proyectos[i][clave]}"
                else:
                    cadena += f"{lista_proyectos[i][clave]},"
            lista_archivo.append(cadena)
        with open(nombre_archivo,"w+",encoding="utf-8") as archivo:
            archivo.writelines(lista_archivo)

#print(guardar_datos(lista_proyecto,"pora.txt"))

def finalizados_json(lista_proyectos): #pasa todos los proyectos finalizados a un archivo json
    lista_aux = []
    for proyectos in range(len(lista_proyectos)):
        aux = lista_proyectos[proyectos]["estado"]
        if aux == "Finalizado":
            lista_aux.append(lista_proyectos[proyectos])

    with open("ProyectosFinalizados.json","w",encoding="utf-8") as archivo:
        json.dump(lista_aux,archivo)


#finalizados_json(lista_proyecto)

def generar_reporte_total(lista_proyectos,fecha_hoy): #genera un reporte que sean mayor al presupuesto pasado
    presupuesto = validar_presupuesto("Ingrese el presupuesto : ","ERROR, Ingrese el presupuesto")
    i =1
    nombre_reporte = f"Reporte N{i}.txt"
    if os.path.exists(nombre_reporte):
        while os.path.exists(f"Reporte N{i}.txt"):
            i +=1
    nombre_reporte = f"Reporte N{i}.txt"
    primera_linea = f"Reporte N{i} fecha:{fecha_hoy} | presupuesto mayores a {presupuesto}"
    primera_linea += "\n"
    lista_archivo = [primera_linea]
    claves = lista_proyectos[0].keys()
    for i in range(0,len(lista_proyectos),1):
        cadena = ""
        aux = lista_proyectos[i]["presupuesto"]
        aux = int(aux)
        if  aux >= presupuesto:
            for clave in claves:

                if clave == "estado":
                    if i +1 != len(lista_proyectos):
                        cadena += f"{lista_proyectos[i][clave]}\n"
                    else:
                        cadena += f"{lista_proyectos[i][clave]}"
                else:
                    cadena += f"{lista_proyectos[i][clave]}|"
            lista_archivo.append(cadena)
        
    with open(nombre_reporte,"w+",encoding="utf-8") as archivo:
        archivo.writelines(lista_archivo)
    print("Reporte generado")
       
#fecha_hoy = datetime.date.today()
#fecha_hoy = fecha_hoy.strftime("%d/%m/%Y")
#generar_reporte_total(lista_proyecto,fecha_hoy)

def generar_reporte_nombre(lista_proyectos,fecha_hoy): #genera un reporte del proyecto del cual se paso el nombre
    i =1
    nombre_reporte = f"Reporte por nombre N{i}.txt"
    if os.path.exists(nombre_reporte):
        while os.path.exists(f"Reporte por nombre N{i}.txt"):
            i +=1
    nombre_reporte = f"Reporte por nombre N{i}.txt"
    primera_linea = f"Reporte por nombre N{i} fecha:{fecha_hoy}"
    primera_linea += "\n"
    lista_archivo = [primera_linea]
    indice = buscar_por_nombre(lista_proyectos)
    if not indice == None:
        claves = lista_proyectos[0].keys()
        for i in range(0,len(lista_proyectos),1):
            cadena = ""
            if  indice == i:
                for clave in claves:
                    if clave == "estado":
                        if i +1 != len(lista_proyectos):
                            cadena += f"{lista_proyectos[i][clave]}\n"
                        else:
                            cadena += f"{lista_proyectos[i][clave]}"
                    else:
                        cadena += f"{lista_proyectos[i][clave]}|"
                lista_archivo.append(cadena) 
               
            with open(nombre_reporte,"w+",encoding="utf-8") as archivo:
                archivo.writelines(lista_archivo)
        print("Reporte generado")
    else:
        print("Error,Nombre no encontrado")

#generar_reporte_nombre(lista_proyecto,fecha_hoy)


def mostrar_proyectos_finalizados_pandemia(lista_proyectos): #funcion que muestra los proyectos finalizados entre (01/03/2020 y 31/12/2021)
    inicio_pandemia = f"01/03/2020"
    final_pandemia = f"31/12/2021"
    proyectos_finalizados_pandemia = []

    for proyecto in range(len(lista_proyectos)):
        if lista_proyectos[proyecto]["estado"] == "Finalizado":
            fecha_fin = lista_proyectos[proyecto]["fecha de fin"]
            if comparar_fechas(inicio_pandemia,fecha_fin):
                if (not comparar_fechas(final_pandemia,fecha_fin)):
                   proyectos_finalizados_pandemia.append(lista_proyectos[proyecto])
    
    if len(proyectos_finalizados_pandemia) == 0:
        print("No se encontraron proyectos Finalizados en pandemia (01/03/2020)-(31/12/2021)")
    else:       
        mostrar_proyectos(proyectos_finalizados_pandemia)

mostrar_proyectos_finalizados_pandemia(lista_proyecto)
def mostrar_proyectos_corta_duracion(lista_proyectos): #funcion que muestra los proyectos finalizados en menos de 3 años
    proyecto_corta_duracion = []
    for proyecto in range(len(lista_proyectos)):
        fecha_inicio = lista_proyectos[proyecto]["fecha de inicio"]
        fecha_fin = lista_proyectos[proyecto]["fecha de fin"]
        fecha_inicio = fecha_inicio.split("/")
        fecha_fin = fecha_fin.split("/") 
        for i in range(len(fecha_inicio)):      
            fecha_inicio[i] = int(fecha_inicio[i])
            fecha_fin[i] = int(fecha_fin[i])
        resto_anios = fecha_fin[2] - fecha_inicio[2]
        resto_meses = fecha_inicio[1] - fecha_fin[1]
        resto_dias = fecha_inicio[0] - fecha_fin[0]
        print(f"{lista_proyectos[proyecto]["nombre"]}{resto_anios} | {resto_meses} | {resto_dias}")
        if (resto_anios < 3 and resto_anios > 0):

            proyecto_corta_duracion.append(lista_proyectos[proyecto])
        else:
            if resto_anios == 3:
                if resto_meses  > 0:
                    proyecto_corta_duracion.append(lista_proyectos[proyecto])
                else:
                    if resto_meses == 0:
                        if resto_dias > 0:
                            proyecto_corta_duracion.append(lista_proyectos[proyecto])
            elif resto_anios == 0:
                if resto_meses  < 0:
                    proyecto_corta_duracion.append(lista_proyectos[proyecto])
                else:
                    if resto_meses == 0:
                        if resto_dias < 0:
                            proyecto_corta_duracion.append(lista_proyectos[proyecto])
    if len(proyecto_corta_duracion) == 0:
        print("No se encontraron proyectos que duraran menos de 3 años")
    else:
        mostrar_proyectos(proyecto_corta_duracion)

#mostrar_proyectos_corta_duracion(lista_proyecto)

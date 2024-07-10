from os import *
from parcial_funciones import *
import datetime 
lista_csv = listar_csv("Proyectos.csv")
proyectos = normalizar_datos(lista_csv)
id_auto_incremental = 0

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1
    
def decrementar_id():
    global id_auto_incremental
    id_auto_incremental +=-1

def menu():
    global id_auto_incremental
    global proyectos
    while(True):
        imprimir_menu()
        opcion = validar_opcion("Ingrese su opcion:","Opcion invalida")
        system('cls') #Windows
        match opcion:
            case 1:
                incrementar_id()
                id_a_usar = id_auto_incremental + len(proyectos)
                if ingresar_proyecto(proyectos,id_a_usar):
                     print("SE DIO DE ALTA CORRECTAMENTE")
                else:
                    decrementar_id()
                    print("ALTA CANCELADA")
              
            case 2:
                id_proyecto = validar_id("Ingrese el id : ","Error, ingrese un id valido : ")
                proyectos = modificar_proyecto(proyectos,id_proyecto)

            case 3:
                id_proyecto = validar_id("Ingrese el id : ","Error, ingrese un id valido : ")
                proyectos = cancelar_proyecto(proyectos,id_proyecto)
            case 4:
                fecha_hoy = datetime.date.today()
                fecha_hoy = fecha_hoy.strftime("%d/%m/%Y")
                proyectos = actualizar_fecha_lista(proyectos,fecha_hoy)
                
            case 5:
                mostrar_proyectos(proyectos)
            case 6:
                calcular_promedio_presupuesto(proyectos)
            case 7:
                indice = buscar_por_nombre(proyectos)
                mostrar_un_proyecto(proyectos, indice)
            case 8:
                proyectos = ordenar_proyectos(proyectos)
            case 9:
                fecha_hoy = datetime.date.today()
                fecha_hoy = fecha_hoy.strftime("%d/%m/%Y")
                proyectos = retomar_proyecto(proyectos,fecha_hoy)
            case 10:
                    fecha_hoy = datetime.date.today()
                    fecha_hoy = fecha_hoy.strftime("%d/%m/%Y")
                    generar_reporte_total(proyectos,fecha_hoy)         
            case 11:
                    fecha_hoy = datetime.date.today()
                    fecha_hoy = fecha_hoy.strftime("%d/%m/%Y")
                    generar_reporte_nombre(proyectos,fecha_hoy)
            case 12:
                  mostrar_proyectos_finalizados_pandemia(proyectos)

            case 13:
                  mostrar_proyectos_corta_duracion(proyectos)
                    
            case 14:
                    print("Saliendo del sistema...")
                    proyectos = desnormalizar_datos(proyectos)
                    finalizados_json(proyectos)
                    guardar_datos(proyectos,"Proyectos.csv")
                    break
        input("Presione enter para continuar...")
menu()    
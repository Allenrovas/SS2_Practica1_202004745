import inquirer
from colorama import Fore, Style
import crearmodelo
import borrarmodelo


def borrar_modelo():
    borrarmodelo.borrar_modelo()
    print("Se ha borrado el modelo")


def crear_modelo():
    crearmodelo.crear_modeloDB()
    print("Se ha creado el modelo")

def extraer_informacion():
    ruta_archivos = input("Ingrese la ruta de los archivos de carga: ")
    print(f"Se ha extraído la información de la ruta: {ruta_archivos}")

def cargar_informacion():
    print("Se ha cargado la información al modelo")

def realizar_consultas():
    print("Se han realizado las consultas y se han guardado los resultados en un archivo de texto")

def salir():
    print("Saliendo del programa")
    exit()


# Definir las preguntas del menú
questions = [
    inquirer.List('opcion',
                    message="Selecciona una opción:",
                    choices=[
                        ('a) Borrar modelo', borrar_modelo),
                        ('b) Crear modelo', crear_modelo),
                        ('c) Extraer información', extraer_informacion),
                        ('d) Cargar información', cargar_informacion),
                        ('e) Realizar consultas', realizar_consultas),
                        (Fore.RED + 'f) Salir' + Style.RESET_ALL, salir),
                    ],
                ),
]

print(Fore.GREEN + "-----------------------------------------" + Style.RESET_ALL)
print(Fore.GREEN + "Seminario de Sistemas 2 - Practica 1" + Style.RESET_ALL)
print(Fore.GREEN + "-----------------------------------------" + Style.RESET_ALL)
print(Fore.GREEN + "Allen Giankarlo Román Vásquez - 202004745" + Style.RESET_ALL)
print(Fore.GREEN + "-----------------------------------------" + Style.RESET_ALL)





while True:
    # Ejecutar el menú
    answer = inquirer.prompt(questions)

    # Procesar la opción seleccionada
    opcion_seleccionada = answer['opcion']
    opcion_seleccionada()  # Llama a la función seleccionada
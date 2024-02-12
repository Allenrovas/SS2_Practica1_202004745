import inquirer
from colorama import Fore, Style
import crearmodelo
import borrarmodelo
import extraer
import carga
import menuconsulta


def borrar_modelo():
    borrarmodelo.borrar_modelo()


def crear_modelo():
    crearmodelo.crear_modeloDB()

def extraer_informacion():
    extraer.extraer_informacion()
    

def cargar_informacion():
    carga.cargar_informacion()

def realizar_consultas():
    menuconsulta.menu_consulta()

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
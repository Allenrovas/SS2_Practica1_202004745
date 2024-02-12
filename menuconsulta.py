import inquirer
from colorama import Fore, Style
import consulta_1
import consulta_2
import consulta_3
import consulta_4
import consulta_5
import consulta_6
import consulta_7
import consulta_8
import consulta_9
import consulta_10


def consulta1():
    print("")
    print(Fore.GREEN + "Consulta 1: SELECT COUNT(*) de las tablas" + Style.RESET_ALL)
    print("")
    consulta_1.consulta_1()



def consulta2():
    print("")
    print(Fore.GREEN + "Consulta 2: Cantidad de tsunamis por año" + Style.RESET_ALL)
    print("")
    consulta_2.consulta_2()

def consulta3():
    print("")
    print(Fore.GREEN + "Consulta 3: Tsunamis por país y año" + Style.RESET_ALL)
    print("")
    consulta_3.consulta_3()

def consulta4():
    print("")
    print(Fore.GREEN + "Consulta 4: Promedio total de daños en millones de dólares" + Style.RESET_ALL)
    print("")
    consulta_4.consulta_4()

def consulta5():
    print("")
    print(Fore.GREEN + "Consulta 5: Top 5 de países con más muertes" + Style.RESET_ALL)
    print("")
    consulta_5.consulta_5()

def consulta6():
    print("")
    print(Fore.GREEN + "Consulta 6: Top 5 de años con más muertes" + Style.RESET_ALL)
    print("")
    consulta_6.consulta_6()

def consulta7():
    print("")
    print(Fore.GREEN + "Consulta 7: Top 5 de años con más tsunamis" + Style.RESET_ALL)
    print("")
    consulta_7.consulta_7()

def consulta8():
    print("")
    print(Fore.GREEN + "Consulta 8: Top 5 de países con más casas destruidas" + Style.RESET_ALL)
    print("")
    consulta_8.consulta_8()

def consulta9():
    print("")
    print(Fore.GREEN + "Consulta 9: Top 5 de países con más casas dañadas" + Style.RESET_ALL)
    print("")
    consulta_9.consulta_9()

def consulta10():
    print("")
    print(Fore.GREEN + "Consulta 10: Promedio de altura máxima del agua por país" + Style.RESET_ALL)
    print("")
    consulta_10.consulta_10()



def menu_consulta():
    
    questions = [
        inquirer.List('opcion',
                        message="Selecciona una opción:",
                        choices=[
                            ('1) Consulta 1: SELECT COUNT(*) de las tablas', consulta1),
                            ('2) Consulta 2: Cantidad de tsunamis por año', consulta2),
                            ('3) Consulta 3: Tsunamis por país y año', consulta3),
                            ('4) Consulta 4: Promedio total de daños en millones de dólares', consulta4),
                            ('5) Consulta 5: Top 5 de países con más muertes', consulta5),
                            ('6) Consulta 6: Top 5 de años con más muertes', consulta6),
                            ('7) Consulta 7: Top 5 de años con más tsunamis', consulta7),
                            ('8) Consulta 8: Top 5 de países con más casas destruidas', consulta8),
                            ('9) Consulta 9: Top 5 de países con más casas dañadas', consulta9),
                            ('10) Consulta 10: Promedio de altura máxima del agua por país', consulta10),
                            (Fore.RED + '11) Regresar' + Style.RESET_ALL, "regresar"),
                        ],
                    ),
    ]
    print(Fore.GREEN + "-----------------------------------------" + Style.RESET_ALL)

    while True:
        # Ejecutar el menú
        answer = inquirer.prompt(questions)

        # Procesar la opción seleccionada
        if answer['opcion'] == "regresar":
            break
        else:
            answer['opcion']()

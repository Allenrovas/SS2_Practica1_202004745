from colorama import Fore, Style
import conexion_db
from tabulate import tabulate


def consulta_2():
    
    #Cantidad de tsunamis por año, usando tabla de hechos y tabla de tiempo
    query ="""
        SELECT t.tYear, COUNT(*) AS CantidadTsunamis
        FROM Tsunami ts
        INNER JOIN Tiempo t
        ON ts.id_tiempo = t.id_tiempo
        GROUP BY t.tYear
        ORDER BY t.tYear;
        """

    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conn.close()
        #escribir en el archivo Consultas/consulta_2.txt UTF-8
        headers = ["Año", "Cantidad de Tsunamis"]
        table = []
        with open("Consultas/consulta_2.txt", "w", encoding="utf-8") as f:
            for r in res:
                #Tabla de resultados
                table.append([r[0], r[1]])
                print(Fore.GREEN + f"En el año {r[0]} hubo {r[1]} tsunamis" + Style.RESET_ALL)
            f.write(tabulate(table, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")


from colorama import Fore, Style
from tabulate import tabulate
import conexion_db

def consulta_7():
    #Top 5 de años con más tsunamis
    query = """
        SELECT TOP 5 t.tYear, COUNT(t.tYear) AS TotalTsunamis
        FROM temporal t
        GROUP BY t.tYear
        ORDER BY TotalTsunamis DESC;
        """
    
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conn.close()
        #escribir en el archivo Consultas/consulta_7.txt UTF-8
        headers = ["Año", "Total de tsunamis"]
        table = []
        with open("Consultas/consulta_7.txt", "w", encoding="utf-8") as f:
            for r in res:
                #Tabla de resultados
                table.append([r[0], r[1]])
                print(Fore.GREEN + f"En el año {r[0]} hubo {r[1]} tsunamis" + Style.RESET_ALL)
            f.write(tabulate(table, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")
from colorama import Fore, Style
from tabulate import tabulate
import conexion_db

def consulta_9():
    #Top 5 de países con casas más dañadas
    query = """
        SELECT TOP 5 t.Country, SUM(t.totalHousesDamaged) AS TotalCasasDañadas
        FROM temporal t
        GROUP BY t.Country
        ORDER BY TotalCasasDañadas DESC;
        """
    
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conn.close()
        #escribir en el archivo Consultas/consulta_9.txt UTF-8
        headers = ["País", "Total de casas dañadas"]
        table = []
        with open("Consultas/consulta_9.txt", "w", encoding="utf-8") as f:
            for r in res:
                #Tabla de resultados
                table.append([r[0], r[1]])
                print(Fore.GREEN + f"El país {r[0]} tuvo {r[1]} casas dañadas" + Style.RESET_ALL)
            f.write(tabulate(table, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")
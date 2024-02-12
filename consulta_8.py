from colorama import Fore, Style
from tabulate import tabulate
import conexion_db

def consulta_8():
    #Top 5 de años con más casas destruidas
    query = """
        SELECT TOP 5 t.Country, SUM(t.totalHousesDestroyed) AS TotalCasasDestruidas
        FROM temporal t
        GROUP BY t.Country
        ORDER BY TotalCasasDestruidas DESC;
        """
    
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conn.close()
        #escribir en el archivo Consultas/consulta_8.txt UTF-8
        headers = ["País", "Total de casas destruidas"]
        table = []
        with open("Consultas/consulta_8.txt", "w", encoding="utf-8") as f:
            for r in res:
                #Tabla de resultados
                table.append([r[0], r[1]])
                print(Fore.GREEN + f"El país {r[0]} tuvo {r[1]} casas destruidas" + Style.RESET_ALL)
            f.write(tabulate(table, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")
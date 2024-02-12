from colorama import Fore, Style
from tabulate import tabulate
import conexion_db

def consulta_10():
    #Promedio de altura máxima de agua por país, sin tsunamis con altura de agua 0
    query = """
        SELECT t.Country, AVG(t.maxWaterHeight) AS PromedioAlturaMaxima
        FROM temporal t
        WHERE t.maxWaterHeight > 0
        GROUP BY t.Country
        ORDER BY PromedioAlturaMaxima DESC;
        """
        
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conn.close()
        #escribir en el archivo Consultas/consulta_10.txt UTF-8
        headers = ["País", "Promedio de altura de agua"]
        table = []
        with open("Consultas/consulta_10.txt", "w", encoding="utf-8") as f:
            for r in res:
                #Tabla de resultados
                table.append([r[0], r[1]])
                print(Fore.GREEN + f"El promedio de altura de agua en {r[0]} es de {r[1]} metros" + Style.RESET_ALL)
            f.write(tabulate(table, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")

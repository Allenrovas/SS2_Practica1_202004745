from colorama import Fore, Style
from tabulate import tabulate
import conexion_db

def consulta_4():
    #Promedio total de daños en millones de dólares por país omitiendo los que no tienen daños o son 0
    query = """
        SELECT c.countryName, AVG(ts.totalDamageMillionsDollars) AS PromedioDanos
        FROM Tsunami ts
        INNER JOIN Country c
        ON ts.id_country = c.id_country
        WHERE ts.totalDamageMillionsDollars > 0
        GROUP BY c.countryName
        ORDER BY PromedioDanos DESC;
        """

    
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conn.close()
        #Escribir en el archivo Consultas/consulta_4.txt
        headers = ["País", "Promedio de daños"]
        table = []
        with open("Consultas/consulta_4.txt", "w", encoding="utf-8") as f:
            for r in res:
                #Tabla de resultados
                table.append([r[0], r[1]])
                print(Fore.GREEN + f"El promedio de daños en {r[0]} es de {r[1]} millones de dólares" + Style.RESET_ALL)
            f.write(tabulate(table, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")
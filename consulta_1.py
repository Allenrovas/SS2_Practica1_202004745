from colorama import Fore, Style
import conexion_db
from tabulate import tabulate

def consulta_1():
    
    query = [
        """
        SELECT COUNT(*) FROM Country;
        """,
        """
        SELECT COUNT(*) FROM Tiempo;
        """,
        """
        SELECT COUNT(*) FROM MaxWaterHeight;
        """,
        """
        SELECT COUNT(*) FROM TsunamiEventValidity;
        """,
        """
        SELECT COUNT(*) FROM Tsunami;
        """,
        """
        SELECT COUNT(*) FROM temporal;
        """
    ]

    tabla = ["Country", "Tiempo", "MaxWaterHeight", "TsunamiEventValidity", "Tsunami", "temporal"]
    listaRespuestas = []
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        for q in query:
            cursor.execute(q)
            res = cursor.fetchone()
            listaRespuestas.append(res[0])
            print(Fore.GREEN + f"La tabla {tabla[query.index(q)]} tiene {res[0]} registros" + Style.RESET_ALL)
            print("")
        conn.close()
        #escribir en el archivo Consultas/consulta_1.txt
        headers = ["Tabla", "Cantidad de registros"]
        table = []
        with open("Consultas/consulta_1.txt", "w") as f:
            for i in range(len(tabla)):
                table.append([tabla[i], listaRespuestas[i]])
            f.write(tabulate(table, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")
    


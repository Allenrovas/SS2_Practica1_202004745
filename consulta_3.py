from colorama import Fore, Style
from tabulate import tabulate
import conexion_db

def consulta_3():
    '''
    Tsunamis por país y que se muestran los años que han tenido tsunamis de la
    siguiente forma:
    País Año 1 Año 2 Año 3
    Guatemala 1901 1902 1903
    '''
    query = [
        """
        DECLARE @cols AS NVARCHAR(MAX);
        """,
        """
        DECLARE @query AS NVARCHAR(MAX);
        """,
        """
        SELECT @cols = STUFF((SELECT ',' + QUOTENAME(tYear)
        FROM Tiempo
        ORDER BY tYear
        FOR XML PATH(''), TYPE
        ).value('.', 'NVARCHAR(MAX)'),1,1,'');
        """,
        """
        SET @query = 'SELECT countryName, ' + @cols + ' from
        (
        SELECT DISTINCT t.tYear, c.countryName
        FROM Tsunami ts
        INNER JOIN Country c
        ON ts.id_country = c.id_country
        INNER JOIN Tiempo t
        ON ts.id_tiempo = t.id_tiempo
        ) src
        pivot
        (
        MAX(tYear)
        for tYear in (' + @cols + ')
        ) piv';
        """,
        """
        EXECUTE(@query);
        """
    ]

    conn = conexion_db.connect()

    if conn is not None:
        try:
            cursor = conn.cursor()
            full_query = '\n'.join(query)
            cursor.execute(full_query)
            res = cursor.fetchall()

            # Escribir en el archivo Consultas/consulta_3.txt
            headers = ["País", "Años"]
            table = []
            with open("Consultas/consulta_3.txt", "w", encoding="utf-8") as f:
                for r in res:
                    country = r[0]
                    years = r[1:]  # Años sin el nombre del país
                    formatted_years = ' '.join(str(year) for year in years if year is not None)
                    table.append([country, formatted_years])
                    print(Fore.GREEN + country + " | " + formatted_years + Style.RESET_ALL)
                f.write(tabulate(table, headers, tablefmt="fancy_grid"))
                
                    


                    

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        finally:
            conn.close()
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")

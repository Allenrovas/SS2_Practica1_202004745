import conexion_db
from colorama import Fore, Style

def extraer_informacion():

    #comprobar que la tabla temporal existe
    query = """
    IF OBJECT_ID('temporal') IS NOT NULL
    SELECT 1 AS res
    ELSE
    SELECT 0 AS res
    """
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        conn.close()
        if res[0] == 1:
            pass
        else:
            print(Fore.RED + "No se ha creado el modelo" + Style.RESET_ALL)
            print("")
            return
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")
        return
    
    query= """
    BULK INSERT temporal
    FROM 'D:\\UNIVERSIDAD\\2024 Primer Semestre\\Seminario de Sistemas 2\\Laboratorio\\SS2_Practica1_202004745\\historial_tsumamis.csv'
    
    WITH
    (
        FIELDTERMINATOR = ',',
        ROWTERMINATOR = '\n',
        FIRSTROW = 3
    );
    """
    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        print(Fore.GREEN + "Se ha cargado la información al modelo" + Style.RESET_ALL)
        print("")
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")
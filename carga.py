import conexion_db
from colorama import Fore, Style

def cargar_informacion():

    query = ["""
    INSERT INTO Country(countryName)
    (SELECT DISTINCT Country FROM temporal);
    """
    ,
    """
    INSERT INTO Tiempo(tYear)
    (SELECT DISTINCT tYear FROM temporal);
    """
    ,
    """
    INSERT INTO MaxWaterHeight(MaxWaterHeight)
    (SELECT DISTINCT MaxWaterHeight FROM temporal);
    """
    ,
    """
    INSERT INTO TsunamiEventValidity(tsunamiEventValidity)
    (SELECT DISTINCT tsunamiEventValidity FROM temporal);
    """
    ,
    """
    INSERT INTO Tsunami(
    totalDeaths,
    totalDamageMillionsDollars,
    totalHousesDestroyed,
    totalHousesDamaged,
    id_country,
    id_tiempo,
    id_maxWaterHeight,
    id_tsunamiEventValidity
    )
    (SELECT temporal.totalDeaths, 
    temporal.totalDamageMillionsDollars, 
    temporal.totalHousesDestroyed, 
    temporal.totalHousesDamaged,
    (SELECT TOP 1 id_country FROM Country WHERE Country.countryName = temporal.Country),
    (SELECT TOP 1 id_tiempo FROM Tiempo WHERE Tiempo.tYear = temporal.tYear),
    (SELECT TOP 1 id_maxWaterHeight FROM MaxWaterHeight WHERE MaxWaterHeight.MaxWaterHeight = temporal.MaxWaterHeight),
    (SELECT TOP 1 id_tsunamiEventValidity FROM TsunamiEventValidity WHERE TsunamiEventValidity.tsunamiEventValidity = temporal.tsunamiEventValidity)
    FROM temporal);"""
             ]

    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        for q in query:
            cursor.execute(q)
            conn.commit()
        conn.close()
        print(Fore.GREEN + "Se ha cargado la información al modelo" + Style.RESET_ALL)
        print("")
    else:
        print(Fore.RED + "No se pudo conectar a la base de datos" + Style.RESET_ALL)
        print("")


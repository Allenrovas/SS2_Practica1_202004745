import conexion_db

def crear_modeloDB():

    query = """
    CREATE TABLE temporal(
    id_temporal INT PRIMARY KEY IDENTITY,
    tYear INT DEFAULT 0,
    tMonth INT DEFAULT 0,
    tDay INT DEFAULT 0,
    tHour INT DEFAULT 0,
    tMinute INT DEFAULT 0,
    tSecond INT DEFAULT 0,
    tsunamiEventValidity INT DEFAULT 0,
    tsunamiCauseCode INT DEFAULT 0,
    tsunamiEarthquakeMagnitude FLOAT DEFAULT 0,
    tsunamiDeposits INT DEFAULT 0,
    Latitude FLOAT DEFAULT 0,
    Longitude FLOAT DEFAULT 0,
    MaxWaterHeight FLOAT DEFAULT 0,
    NumberRunups INT DEFAULT 0,
    tsunamiMagnitudes INT DEFAULT 0,
    tsunamiIntensity INT DEFAULT 0,
    totalDeaths INT DEFAULT 0,
    totalMissing INT DEFAULT 0,
    totalMissingDescription VARCHAR(100) DEFAULT '',
    totalInjuries INT DEFAULT 0,
    totalDamageMillionsDollars FLOAT DEFAULT 0,
    totalDamageDescription VARCHAR(100),
    totalHousesDestroyed INT DEFAULT 0,
    totalHousesDamaged INT DEFAULT 0,
    Country VARCHAR(100),
    locationName VARCHAR(100)
    );

    CREATE TABLE Country(
        id_country INT IDENTITY(1,1) PRIMARY KEY,
        countryName VARCHAR(100)
    );

    CREATE TABLE Tiempo(
        id_tiempo INT IDENTITY(1,1) PRIMARY KEY,
        tYear INT DEFAULT 0
    );

    CREATE TABLE Totales(
        id_totales INT IDENTITY(1,1) PRIMARY KEY,
        totalDeaths INT DEFAULT 0,
        totalDamageMillionsDollars FLOAT DEFAULT 0,
        totalHousesDestroyed INT DEFAULT 0,
        totalHousesDamaged INT DEFAULT 0
    );

    CREATE TABLE MaxWaterHeight(
        id_maxWaterHeight INT IDENTITY(1,1) PRIMARY KEY,
        MaxWaterHeight FLOAT DEFAULT 0
    );

    CREATE TABLE TsunamiEventValidity(
        id_tsunamiEventValidity INT IDENTITY(1,1) PRIMARY KEY,
        tsunamiEventValidity INT DEFAULT 0
    );

    CREATE TABLE Tsunami(
        id_tsunami INT IDENTITY(1,1) PRIMARY KEY,
        id_country INT,
        id_tiempo INT,
        id_totales INT,
        id_maxWaterHeight INT,
        id_tsunamiEventValidity INT,
        FOREIGN KEY (id_country) REFERENCES Country(id_country),
        FOREIGN KEY (id_tiempo) REFERENCES Tiempo(id_tiempo),
        FOREIGN KEY (id_totales) REFERENCES Totales(id_totales),
        FOREIGN KEY (id_maxWaterHeight) REFERENCES MaxWaterHeight(id_maxWaterHeight),
        FOREIGN KEY (id_tsunamiEventValidity) REFERENCES TsunamiEventValidity(id_tsunamiEventValidity)
    );
    """

    conn = conexion_db.connect()

    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Se ha creado el modelo")
    else:
        print("No se pudo conectar a la base de datos")

    
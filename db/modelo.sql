/*CREAR BASE DE DATOS*/

CREATE DATABASE semi2_practica1;

USE semi2_practica1;

/*BORRAR MODELO*/
SELECT CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_NAME = 'Tsunami' AND CONSTRAINT_NAME LIKE 'FK_%';

DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Tiempo;
DROP TABLE IF EXISTS MaxWaterHeight;
DROP TABLE IF EXISTS TsunamiEventValidity;
DROP TABLE IF EXISTS Tsunami;
DROP TABLE IF EXISTS temporal;

/*CREAR MODELO*/
CREATE TABLE temporal(
tYear INT DEFAULT 0,
tMonth INT DEFAULT 0,
tDay INT DEFAULT 0,
tHour INT DEFAULT 0,
tMinute INT DEFAULT 0,
tSecond FLOAT DEFAULT 0,
tsunamiEventValidity INT DEFAULT 0,
tsunamiCauseCode INT DEFAULT 0,
tsunamiEarthquakeMagnitude FLOAT DEFAULT 0,
tsunamiDeposits INT DEFAULT 0,
Latitude FLOAT DEFAULT 0,
Longitude FLOAT DEFAULT 0,
MaxWaterHeight FLOAT DEFAULT 0,
NumberRunups INT DEFAULT 0,
tsunamiMagnitudes FLOAT DEFAULT 0,
tsunamiIntensity FLOAT DEFAULT 0,
totalDeaths INT DEFAULT 0,
totalMissing INT DEFAULT 0,
totalMissingDescription VARCHAR(100) DEFAULT '',
totalInjuries INT DEFAULT 0,
totalDamageMillionsDollars FLOAT DEFAULT 0,
totalDamageDescription VARCHAR(100),
totalHousesDestroyed INT DEFAULT 0,
totalHousesDamaged INT DEFAULT 0,
Country VARCHAR(100) DEFAULT '',
locationName VARCHAR(100) DEFAULT ''
);

CREATE TABLE Country(
    id_country INT IDENTITY(1,1) PRIMARY KEY,
    countryName VARCHAR(100)
);

CREATE TABLE Tiempo(
    id_tiempo INT IDENTITY(1,1) PRIMARY KEY,
    tYear INT DEFAULT 0
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
    id_maxWaterHeight INT,
    id_tsunamiEventValidity INT,
    totalDeaths INT DEFAULT 0,
    totalDamageMillionsDollars FLOAT DEFAULT 0,
    totalHousesDestroyed INT DEFAULT 0,
    totalHousesDamaged INT DEFAULT 0
    FOREIGN KEY (id_country) REFERENCES Country(id_country),
    FOREIGN KEY (id_tiempo) REFERENCES Tiempo(id_tiempo),
    FOREIGN KEY (id_maxWaterHeight) REFERENCES MaxWaterHeight(id_maxWaterHeight),
    FOREIGN KEY (id_tsunamiEventValidity) REFERENCES TsunamiEventValidity(id_tsunamiEventValidity)
);

/*EXTRAER INFORMACION DE TEMPORAL A MODELO*/
BULK INSERT temporal
FROM 'D:\\UNIVERSIDAD\\2024 Primer Semestre\\Seminario de Sistemas 2\\Laboratorio\\SS2_Practica1_202004745\\historial_tsumamis.csv'

WITH
(
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 3
);

/*INSERTAR INFORMACION A MODELO*/
INSERT INTO Country(countryName)
(SELECT DISTINCT Country FROM temporal);

INSERT INTO Tiempo(tYear)
(SELECT DISTINCT tYear FROM temporal);

INSERT INTO MaxWaterHeight(MaxWaterHeight)
(SELECT DISTINCT MaxWaterHeight FROM temporal);

INSERT INTO TsunamiEventValidity(tsunamiEventValidity)
(SELECT DISTINCT tsunamiEventValidity FROM temporal);

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
FROM temporal);

/*CONSULTA 1*/
SELECT COUNT(*) FROM Country;

SELECT COUNT(*) FROM Tiempo;

SELECT COUNT(*) FROM MaxWaterHeight;

SELECT COUNT(*) FROM TsunamiEventValidity;

SELECT COUNT(*) FROM Tsunami;

SELECT COUNT(*) FROM temporal;

/*CONSULTA 2*/
SELECT t.tYear, COUNT(*) AS CantidadTsunamis
FROM Tsunami ts
INNER JOIN Tiempo t
ON ts.id_tiempo = t.id_tiempo
GROUP BY t.tYear
ORDER BY t.tYear;

/*CONSULTA 3*/
DECLARE @cols AS NVARCHAR(MAX);

DECLARE @query AS NVARCHAR(MAX);

SELECT @cols = STUFF((SELECT ',' + QUOTENAME(tYear)
FROM Tiempo
ORDER BY tYear
FOR XML PATH(''), TYPE
).value('.', 'NVARCHAR(MAX)'),1,1,'');

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

EXECUTE(@query);

/*CONSULTA 4*/

SELECT c.countryName, AVG(ts.totalDamageMillionsDollars) AS PromedioDanos
FROM Tsunami ts
INNER JOIN Country c
ON ts.id_country = c.id_country
WHERE ts.totalDamageMillionsDollars > 0
GROUP BY c.countryName
ORDER BY PromedioDanos DESC;

/*CONSULTA 5*/

SELECT TOP 5 t.Country, SUM(t.totalDeaths) AS TotalMuertes
FROM temporal t
GROUP BY t.Country
ORDER BY TotalMuertes DESC;

/*CONSULTA 6*/
SELECT TOP 5 t.tYear, SUM(t.totalDeaths) AS TotalMuertes
FROM temporal t
GROUP BY t.tYear
ORDER BY TotalMuertes DESC;

/*CONSULTA 7*/
SELECT TOP 5 t.tYear, COUNT(t.tYear) AS TotalTsunamis
FROM temporal t
GROUP BY t.tYear
ORDER BY TotalTsunamis DESC;

/*CONSULTA 8*/
SELECT TOP 5 t.Country, SUM(t.totalHousesDestroyed) AS TotalCasasDestruidas
FROM temporal t
GROUP BY t.Country
ORDER BY TotalCasasDestruidas DESC;

/*CONSULTA 9*/
SELECT TOP 5 t.Country, SUM(t.totalHousesDamaged) AS TotalCasasDañadas
FROM temporal t
GROUP BY t.Country
ORDER BY TotalCasasDañadas DESC;

/*CONSULTA 10*/
SELECT t.Country, AVG(t.maxWaterHeight) AS PromedioAlturaMaxima
FROM temporal t
WHERE t.maxWaterHeight > 0
GROUP BY t.Country
ORDER BY PromedioAlturaMaxima DESC;
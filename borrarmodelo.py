import conexion_db

def borrar_modelo():
    # Eliminar restricciones de clave externa
    query1 = """
    SELECT CONSTRAINT_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_NAME = 'Tsunami' AND CONSTRAINT_NAME LIKE 'FK_%';
    """

    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query1)
        constraints = cursor.fetchall()  # Obtener todos los nombres de las restricciones

        # Eliminar cada restricción encontrada
        for constraint in constraints:
            constraint_name = constraint[0]
            drop_constraint_query = f"ALTER TABLE Tsunami DROP CONSTRAINT {constraint_name};"
            cursor.execute(drop_constraint_query)

        conn.commit()
        conn.close()
        print("Se han eliminado las restricciones de clave externa")

    # Eliminar las tablas
    query2 = """
    DROP TABLE IF EXISTS Country;
    DROP TABLE IF EXISTS Tiempo;
    DROP TABLE IF EXISTS Totales;
    DROP TABLE IF EXISTS MaxWaterHeight;
    DROP TABLE IF EXISTS TsunamiEventValidity;
    DROP TABLE IF EXISTS Tsunami;
    DROP TABLE IF EXISTS temporal;
    """

    conn = conexion_db.connect()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(query2)
        conn.commit()
        conn.close()
        print("Se han eliminado las tablas")
    else:
        print("No se pudo conectar a la base de datos")
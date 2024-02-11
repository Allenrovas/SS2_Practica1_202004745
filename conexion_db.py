import pyodbc

def connect():
    server = 'localhost'
    database = 'semi2_practica1'
    driver = '{ODBC Driver 17 for SQL Server}'

    try:
        conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None
    
import pyodbc

# Datos de conexion a la BD SQL Server
DB_CONN = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=tcp:sqlDatabaseprueba.database.windows.net,1433;"
    "DATABASE=sqlDatabaseprueba;"
    "UID=adminsql;"
    "PWD=SqlAdmin123;"
    "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
)

# función para obtener la conexión a la base de datos
def get_connection():
    return pyodbc.connect(DB_CONN)

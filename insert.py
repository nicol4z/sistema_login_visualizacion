"""
Script para insertar registros de usuarios a la base de datos SQL Server desde un archivo JSON.

- Lee el archivo usuarios.json.
- Para cada usuario, obtiene nombre, rol, renta y genera una contraseña hasheada usando bcrypt.
- Ejecuta un procedimiento almacenado INSERT_USUARIO para insertar los datos.
"""

import json
import pyodbc
import bcrypt

# Archivo JSON que contiene la lista de usuarios a insertar
json_file = "usuarios.json"

try:
    # Conexión a la base de datos SQL Server mediante ODBC
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=tcp:sqldatabaseprueba.database.windows.net,1433;"
        "DATABASE=sqldatabaseprueba;"
        "UID=adminsql;"
        "PWD=SqlAdmin123;"
        "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )

    cursor = conn.cursor()

    # Cargar datos desde el archivo JSON
    with open(json_file, 'r', encoding='utf-8') as file:
        usuarios = json.load(file)

    # Recorrer usuarios y ejecutar el procedimiento almacenado
    for usuario in usuarios:
        nombre = usuario["nombre"]
        rol = usuario["rol"]
        renta = usuario["renta_mensual"]

        # Generar contraseña hasheada usando el nombre como clave (ejemplo)
        password_hash = bcrypt.hashpw(nombre.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Ejecutar procedimiento almacenado
        cursor.execute("EXEC INSERT_USUARIO ?, ?, ?, ?", nombre, rol, renta, password_hash)

    conn.commit()
    print("Inserciones realizadas correctamente")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    try:
        cursor.close()
        conn.close()
    except:
        pass

from database import get_connection
import bcrypt

# Servicio encargado de validar el usuario que intenta iniciar sesión
def login_user(username, password):
    # Primero se conecta a la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    # Se ejecuta el SP que busca el usuario por nombre
    cursor.execute("EXEC LOGIN_USER ?", username)
    row = cursor.fetchone()
    conn.close()

    # Si no encuentra nada, el usuario no existe
    if not row:
        return False, "Usuario no encontrado"

    # Validación de la contraseña usando bcrypt, comparando el hash de la BD
    hash_password = row[1]
    if not bcrypt.checkpw(password.encode(), hash_password.encode()):
        return False, "Contraseña incorrecta"

    # Si todo está bien, retorno exitoso junto con los datos
    return True, row

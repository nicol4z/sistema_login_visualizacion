import json
import os

# Servicio encargado de obtener la lista de usuarios, filtrada por rol del usuario logueado
def get_filtered_users(username, rol):
    # Abro el JSON donde están todos los usuarios registrados
    json_path = os.path.join(os.getcwd(), "usuarios.json")
    with open(json_path, "r", encoding="utf-8") as file:
        users_data = json.load(file)

    # si es admin, puede ver a todos los usuarios
    if rol == "admin":
        return users_data
    # si es supervisor ve supervisores y usuarios normales
    elif rol == "supervisor":
        return [u for u in users_data if u["rol"] in ["supervisor", "usuario"]]
    # si es usuario solo ve sus propios datos
    else:
        return [u for u in users_data if u["nombre"] == username]

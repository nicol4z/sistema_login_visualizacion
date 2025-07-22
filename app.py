# Archivo principal donde se define el sistema de rutas del proyecto.
# Aquí se conecta el backend completo usando Litestar con Jinja para las vistas.
# También se manejan las cookies de sesión y se conecta a los servicios definidos por separado.

from litestar import Litestar, get, post, Request, Response
from litestar.response import Template, Redirect
from litestar.template import TemplateConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.datastructures import Cookie
from litestar.exceptions import HTTPException
from litestar.static_files import create_static_files_router

# Se importan los servicios personalizados
from auth_service import login_user
from dashboard_service import get_filtered_users
from database import get_connection


# Ruta principal que carga la vista del login
@get("/")
async def index(request: Request) -> Template:
    return Template(template_name="login.html", context={})


# Ruta POST que gestiona el proceso de login.
# se Recibe los datos del formulario, valida con la base de datos y si es correcto genera las cookies.
@post("/login")
async def login(request: Request) -> Response:
    data = await request.json()
    username, password = data.get("username"), data.get("password")

    # Se utiliza el servicio login_user para validar credenciales
    valid, result = login_user(username, password)
    if not valid:
        raise HTTPException(status_code=401, detail=result)

    # En caso de login correcto se generan las cookies para mantener la sesion activa
    response = Response(
        content={"message": "Ingreso exitoso"},
        media_type="application/json",
        cookies=[Cookie(key="user", value=username, path="/")]
    )
    return response


# Ruta que carga el dashboard según el rol del usuario
# Se validan las cookies, recupera el rol desde BD, y filtra datos desde JSON.
@get("/dashboard")
async def dashboard(request: Request) -> Template:
    username = request.cookies.get("user")
    if not username:
        return Redirect("/")

    # Conexión rápida a BD solo para obtener datos básicos del usuario logueado
    conn = get_connection()
    cursor = conn.cursor()
    from queries import LOGIN_USER_QUERY
    cursor.execute(LOGIN_USER_QUERY, username)
    row = cursor.fetchone()
    conn.close()

    # Si no existe el usuario se fuerza redirect a login
    if not row:
        return Redirect("/")

    # Se obtiene el rol para poder filtrar los datos
    rol = row[2]
    users = get_filtered_users(username, rol)

    # Se devuelve la vista ya con los datos filtrados segun rol
    return Template(template_name="dashboard.html", context={"users": users, "rol": rol})


# Ruta para cerrar sesión, básicamente elimina la cookie y vuelve a la vista principal
@get("/logout")
async def logout(request: Request) -> Redirect:
    response = Redirect("/")
    response.cookies = [Cookie(key="user", value="", max_age=0, path="/")]
    return response


# Para poder servir los JS, CSS o imágenes directamente desde la carpeta static
static_files = create_static_files_router(path="/static", directories=["static"])


# Configuración principal de la aplicación con Litestar
app = Litestar(
    route_handlers=[index, login, dashboard, logout, static_files],
    template_config=TemplateConfig(
        directory="templates",
        engine=JinjaTemplateEngine
    ),
    debug=True 
)

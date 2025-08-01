# Sistema de Login y Visualización de Datos

## Descripción general
Aplicación web que permite a los usuarios iniciar sesión y visualizar información dependiendo de su rol. Existen tres tipos de rol: admin, supervisor y usuario. Cada rol tiene diferentes permisos para visualizar la información contenida en el dashboard.

## Tecnologías utilizadas
- Python 3.12
- Litestar como framework backend
- SQL Server para almacenar usuarios y contraseñas
- Jinja2 para renderizar las plantillas HTML
- Bootstrap para el diseño responsivo del frontend
- DataTables para tablas dinámicas
- jQuery para manejar el formulario de login con peticiones AJAX

## Requisitos para ejecutar el proyecto
- Tener Python 3.12 o superior instalado.
- Tener SQL Server funcionando con el procedimiento almacenado llamado LOGIN_USER.
- Tener un archivo `usuarios.json` para desplegar los datos en el dashboard.

### Paquetes de Python requeridos
- Litestar: `pip install litestar`
- PyODBC: `pip install pyodbc`
- Bcrypt: `pip install bcrypt`
- Jinja2: `pip install jinja2`
- Uvicorn: `pip install "uvicorn[standard]"`

## Instalación rápida de todos los paquetes:

- pip install -r requirements.txt



## Pasos para ejecutar el proyecto localmente
1. Clonar el repositorio desde GitHub.
2. Crear un entorno virtual:
    - Windows: `python -m venv venv`
    - Linux/MacOS: `python3 -m venv venv`
3. Activar el entorno virtual:
    - Windows: `venv\\Scripts\\activate`
    - Linux/MacOS: `source venv/bin/activate`
4. Instalar las dependencias usando pip.
5. Correr el servidor con: `uvicorn app:app --reload`
6. Acceder desde el navegador a `http://127.0.0.1:8000/`



## Notas finales
- La autenticación se maneja mediante SQL Server.
- La visualización de datos se gestiona desde el archivo usuarios.json.
- DataTables se utiliza para proporcionar funcionalidades de búsqueda y ordenamiento en tablas.


## Consideraciones
- La base de datos está montada en Azure SQL. Para facilitar su revisión sin necesidad de conexión a Azure, se incluye en el proyecto un archivo .bacpac con una copia completa de la base de datos.
- Puedes restaurar este archivo .bacpac en un entorno local usando SQL Server Management Studio (SSMS) mediante la opción “Importar archivo BACPAC”.
- este respaldo contiene las tablas, procedimientos almacenados y datos necesarios para probar el sistema sin conexión directa a Azure.
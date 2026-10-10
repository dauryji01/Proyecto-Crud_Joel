# Proyecto CRUD de Suplementos

Este proyecto es una aplicacion web desarrollada con Python y Flask para gestionar un inventario de suplementos. Permite registrar nuevos productos consultar los existentes editar su informacion y eliminarlos.

La idea principal es practicar el funcionamiento de un CRUD y entender como se conectan los formularios las rutas de Flask los modelos y la base de datos.

## Tecnologias y dependencias

Las dependencias del proyecto se encuentran en `requirements.txt`. Se instalan dentro de un entorno virtual para mantenerlas separadas de otros proyectos.

| Dependencia | Funcion |
|---|---|
| Flask | Maneja las rutas y las peticiones de la aplicacion web |
| Flask-SQLAlchemy | Conecta los modelos de Python con la base de datos |
| SQLAlchemy | Permite trabajar con los datos mediante objetos de Python |
| Flask-Migrate | Gestiona los cambios en la estructura de la base de datos |
| Alembic | Ejecuta las migraciones de la base de datos |
| Flask-WTF | Integra los formularios con Flask |
| WTForms | Define los campos y las validaciones de los formularios |
| Jinja2 | Inserta datos de Python dentro de las plantillas HTML |
| Werkzeug | Proporciona herramientas utilizadas por Flask |
| ItsDangerous | Maneja operaciones relacionadas con datos firmados y seguros |
| Blinker | Proporciona señales para comunicar eventos entre componentes |
| Click | Permite crear comandos para la terminal |
| MarkupSafe | Ayuda a manejar texto HTML de forma segura |
| Mako | Motor de plantillas utilizado por Alembic |
| Django | Framework web independiente incluido en la lista de dependencias |
| Django REST Framework | Herramientas para crear APIs con Django |
| asgiref | Utilidades relacionadas con el estandar ASGI |
| sqlparse | Analiza y organiza sentencias SQL |
| email-validator | Valida direcciones de correo electronico |
| dnspython | Herramientas para consultas DNS utilizadas por algunas librerias |
| idna | Maneja nombres de dominio internacionalizados |
| colorama | Facilita la salida de colores en la terminal |
| iniconfig | Lee configuraciones en formato INI |
| pytest | Permite ejecutar pruebas automatizadas |
| pluggy | Sistema de plugins utilizado por herramientas como pytest |
| Pygments | Resalta sintaxis de codigo |
| packaging | Maneja versiones y requisitos de paquetes |
| typing_extensions | Agrega herramientas adicionales de tipado para Python |
| tzdata | Proporciona datos de zonas horarias |
| MarkupSafe | Manejo seguro de texto para plantillas |
| SQLAlchemy | Herramientas ORM y acceso a bases de datos |

Tambien se incluyen versiones especificas de las dependencias para que la instalacion use las versiones indicadas en el archivo.

Nota: Django y Django REST Framework no forman parte del flujo principal de Flask que se describe en este README. Si no se usan en otra parte del proyecto se pueden revisar y eliminar de `requirements.txt` mas adelante.

## Instalacion en Windows

1. Descarga o clona el repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo `install.bat` si esta disponible. El instalador prepara el entorno virtual e instala las dependencias de `requirements.txt`.
4. Comprueba que la carpeta `env` se haya creado correctamente.

Si necesitas instalar las dependencias manualmente puedes ejecutar:

```bash
env\Scripts\python.exe -m pip install -r requirements.txt
```

### Actualizar la base de datos

Este paso es importante para que la aplicacion tenga las tablas necesarias para guardar los suplementos.

Ejecuta desde la carpeta principal del proyecto:

```bash
flask --app run:app db upgrade
```

Este comando aplica las migraciones disponibles. Las migraciones describen los cambios que deben realizarse en la estructura de la base de datos.

Si el comando `flask` no se reconoce o utiliza otra instalacion de Python puedes ejecutarlo a traves del entorno virtual:

```bash
env\Scripts\python.exe -m flask --app run:app db upgrade
```

No es necesario ejecutar `db init` cada vez que instalas el proyecto si la carpeta `migrations` ya existe.

## Ejecutar la aplicacion

Con las dependencias instaladas y la base de datos preparada ejecuta:

```bash
env\Scripts\python.exe run.py
```

Despues abre en el navegador la direccion local que muestre Flask en la terminal.

## Como funciona el codigo

### `run.py`

Es el punto de entrada de la aplicacion. Llama a `create_app()` para crear la aplicacion Flask y luego la inicia cuando ejecutas el archivo directamente.

### `app/__init__.py`

Contiene la funcion `create_app()` que configura la aplicacion.

- Crea la instancia de Flask.
- Carga la configuracion desde `config.py`.
- Inicializa SQLAlchemy para poder trabajar con la base de datos.
- Inicializa Flask-Migrate para gestionar las migraciones.
- Registra las rutas de la aplicacion.

### `config.py`

Guarda la configuracion general como la clave secreta y la direccion de la base de datos SQLite.

La clave secreta se utiliza entre otras cosas para proteger las sesiones y los formularios. En un proyecto real no conviene dejar una clave sensible escrita directamente en el codigo.

### `app/models.py`

Define el modelo `Suplemento`. Un modelo representa la estructura de los datos que se guardan en la base de datos.

Cada suplemento tiene los siguientes campos:

- `id`: identificador unico del registro.
- `nombre`: nombre del suplemento.
- `marca`: marca del producto.
- `categoria`: categoria a la que pertenece.
- `precio`: precio del producto.
- `cantidad`: unidades disponibles.

SQLAlchemy utiliza esta clase para representar los registros de la tabla en Python.

### `app/forms.py`

Define el formulario `SuplementoForm` con sus campos y reglas de validacion.

Por ejemplo los campos de nombre marca y categoria deben tener contenido. El precio y la cantidad tambien tienen reglas para evitar valores negativos.

Cuando Flask recibe los datos del formulario puede comprobarlos antes de guardar los cambios.

### `app/routes.py`

Define las rutas que conectan las direcciones web con las funciones de Python.

- `/`: consulta los suplementos guardados y los envia a la plantilla principal.
- `/crear`: muestra el formulario y registra un suplemento cuando los datos son validos.
- `/editar/<int:id>`: busca un suplemento por su identificador y permite actualizarlo.
- `/eliminar/<int:id>`: busca un suplemento y lo elimina mediante una peticion POST.

Las rutas son el punto donde se coordina lo que solicita el usuario con las operaciones de la aplicacion.

## Como se guardan los datos

El flujo general del programa es el siguiente:

1. El usuario abre una pagina y Flask muestra una plantilla HTML.
2. La plantilla presenta un formulario con campos para introducir los datos del suplemento.
3. El usuario completa el formulario y lo envia.
4. Flask recibe la peticion y `Flask-WTF` junto con `WTForms` permite validar los datos.
5. Si los datos son validos la ruta crea o modifica un objeto `Suplemento`.
6. SQLAlchemy utiliza `db.session.add()` para agregar un registro nuevo o `db.session.delete()` para eliminarlo.
7. `db.session.commit()` confirma los cambios en SQLite.
8. Cuando se consulta la pagina principal la aplicacion recupera los registros y los envia a la plantilla para mostrarlos.

Por ejemplo al crear un suplemento el codigo toma los valores del formulario y crea un objeto:

```python
suplemento = Suplemento(
    nombre=form.nombre.data,
    marca=form.marca.data,
    categoria=form.categoria.data,
    precio=form.precio.data,
    cantidad=form.cantidad.data
)
```

Luego lo agrega a la sesion y confirma el cambio:

```python
db.session.add(suplemento)
db.session.commit()
```

La sesion permite organizar las operaciones pendientes y `commit()` las guarda de forma permanente en la base de datos.

## Estructura del proyecto

```text
Proyecto-Crud_Joel/
├── app/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── index.html
│       ├── crear.html
│       └── editar.html
├── env/
├── instance/
│   └── suplementos.db
├── migrations/
├── test/
├── testing/
├── config.py
├── requirements.txt
└── run.py
```

- `app/`: contiene la logica principal de la aplicacion.
- `templates/`: contiene las paginas HTML que Flask renderiza.
- `static/`: contiene archivos estaticos como CSS.
- `instance/`: guarda la base de datos local.
- `migrations/`: contiene los cambios versionados de la estructura de la base de datos.
- `test/` y `testing/`: carpetas destinadas a pruebas.
- `env/`: entorno virtual local. No es necesario subirlo al repositorio porque se puede volver a crear.
- `requirements.txt`: lista las dependencias que necesita el proyecto.
- `run.py`: inicia la aplicacion.

## Operaciones CRUD

CRUD significa crear consultar actualizar y eliminar datos.

En este proyecto esas operaciones corresponden a:

- Create: registrar un suplemento.
- Read: consultar los suplementos guardados.
- Update: editar los datos de un suplemento.
-Delete: eliminar un suplemento.

Estas operaciones forman la base del funcionamiento de la aplicacion.
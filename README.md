# Clean Architecture Python Project.

Proyecto de Web API en FastAPI con Python aplicando los principios de Clean Code, inyección de dependencias y usando la arquitectura de Clean Architecture apuntando a una Base de Datos de MySQL o MariaDb.

## Requisitos generales
* Tener instalado algun editor de código fuente como Visual Studio Code o Pycharm.
* Tener instalado MySQL o MariaDb como gestor de Base de Datos.

### Windows
* Instalar el [compilador de Python](https://www.python.org/downloads/windows/) como Administrador. Debe instalarse todos sus componentes y activar algunas configuraciónes adicionales del sistema operativo de Windows como permitir que los nombres de las carpetas tengan nombres largos. Una vez instalado Python, reinicie el equipo y pruebe com el comando: ```$ python --version```

### MacOS
* Siga las instrucciones de instalación en este [enlace.](https://www.python.org/downloads/macos/)

### Linux
* Para en el caso de Linux Ubuntu y sus variantes, se debe instalar **pip** para instalar cualquier paquete en Python:

```
$ sudo apt install python3-pip -yq
```
* Para ejecutar FastApi, debe instalarse **uvicorn**, que es un servidor local para aplicaciones FastApi:

```
$ sudo apt install uvicorn -yq
```
* Con esto, ya se puede ejecutar cualquier proyecto de FastApi de Python ejecutando: ``` $ uvicorn main:app --reload ```. Pero usando Visual Studio Code con los componentes adicionales mencionados en esta descripción se facilita la compilación de código fuente de este proyecto.
* Para otras distribuciones de Linux, el proceso es similar.

### Otras plataformas

* Siga las instrucciones de instalación en este [enlace.](https://www.python.org/download/other/)

## Variables de entorno
Deben configurarse las siguientes variables de entorno para su correcta ejecución:

```
DATABASE_URL_MYSQL = mysql+pymysql://username:password@host:3306/database_name
DATABASE_URL_MARIA_DB = mariadb+aiomysql://username:password@host:3306/database_name
API_KEY = myapikey
POOL_SIZE = 20
MAX_OVERFLOW = 0
POOL_TIMEOUT = 30
POOL_RECYCLE = 1800
MAX_NUMBER_CONCURRENT_REQUESTS = 10
MAX_EXECUTION_TIME = 10
REQUEST_MAX_NUMBER = 100
```
Este proyecto tiene los paquetes pymysl y psycopg2 para conexiones a PostgreSQL.

### Windows
En la ventana de **Variables de Entorno** guardar estas variables.

### No Windows
En Mac, Linux, UNIX y otras plataformas, debe guardarse las variables de entorno de la siguente manera:

```
export DATABASE_URL_MYSQL = mysql+pymysql://username:password@host:3306/database_name
export DATABASE_URL_MARIA_DB = mariadb+aiomysql://username:password@host:3306/database_name
export API_KEY = myapikey
export POOL_SIZE = 20
export MAX_OVERFLOW = 0
export POOL_TIMEOUT = 30
export POOL_RECYCLE = 1800
export MAX_NUMBER_CONCURRENT_REQUESTS = 10
export MAX_EXECUTION_TIME = 10
export REQUEST_MAX_NUMBER = 100
```
En Linux Ubuntu, mantener estas variables editando el archivo ```~/.bashrc``` escribiendo las líneas anteriormente mencionadas y ejecutar el siguiente comando para que se guarden las variables y reiniciar el equipo:

```
$ source ~/.bashrc && sudo reboot
```
Las variables de entorno ya están cargadas al arrancar el equipo y se puede ejecutar este proyecto sin problema. Para la conexión a MariaDb, debe tener instalado [MariaDb Connector](https://mariadb.com/downloads/connectors/connectors-data-access/c-connector) antes de instalar los paquetes de este proyecto. En el caso de Linux Ubuntu, basta con este comando:

```
$ sudo apt-get install libmariadb3 libmariadb-dev
```

## Instalación de paquetes.
Ejecutar este comando para instalar los componentes de Python en el equipo:

```
$ pip install -r requeriments.txt
```

Lo más sano es crear un entorno virtual:

```
$ sudo python3 -m venv venv
$ source venv/bin/activate
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
$ deactivate
```

En el caso de Windows, será esto:

```
$ pip install virtualenv
$ cd my-project
$ virtualenv --python C:\Path\To\Python\python.exe venv
$ .\venv\Scripts\activate
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
$ deactivate
```
## Visual Studio Code
En caso de que no se tenga alguna configuración para correr este proyecto, agregar en la carpeta **./vscode** un archivo llamado **launch.json** con la siguiente estructura:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Depurador de Python: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app",
                "--reload"
            ],
            "jinja": true,
            "justMyCode": true,
            "console": "integratedTerminal",
            "env": {"PYTHONUNBUFFERED": "1"}
        }
    ]
}
```

Los componentes necesarios para ejecutar y depurar este proyecto son:

* autoDocstring - Python Docstring Generator
* Better Commands
* Code Runner
* Code Spell Checker
* Dash
* Django
* EditorConfig for VS Code
* Even Better TOML
* Git Graph
* Git History
* GitIgnore
* GitLens
* IntelliCode
* IntelliCode API Usage Examples
* iSort
* Jinja
* Jupyter Keymap
* Jupyter Notebook Renderers
* Jupyter Cell Tags
* Jupyter Slide Show
* Live Share
* LiveCode for Python
* MagicPython
* Markdown All in One
* Markdownlint
* Mintlify Doc Writer for Python, JavaScript, TypeScript, C++, PHP, Java, C#, Ruby & more
* Mdoc - Markdown Documentation Viewer
* Open in GitHub, Bitbucket, Gitlab, VisualStudio.com
* Postman
* Prettier - Code Formatter
* Project Manager
* Pylance
* Python
* Python Coding Tools
* Python Config
* Python Debugger
* Python Environment Manager
* Python Extended
* Python Indent
* Python Path
* Python Resource Monitor
* Python snippets
* Python Test Explorer for Visual Studio Code
* Python Type Hint
* python-snippets
* Qt for Python
* Sonarlint
* Test Adapter Converter
* Test Explorer Live Share
* Test Explorer UI
* Wolf
* XML
* YAML

## Base de Datos
El script de Base de Datos para MariaDB o MySQL se encuentra en la carpeta **init_db**. Antes de ejecutar este proyecto, ejecute el script SQL en una Base de Datos creada en MariaDB o MySQL. Basado en este [enlace.](https://docs.sqlalchemy.org/en/20/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mariadbconnector)

## Referencias:
* [Understanding Clean Architecture](https://levelup.gitconnected.com/clean-architecture-86c4f03e4771)
* [Dependency injection and inversion of control in Python](https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html)
* [Dependency injection in Python](https://snyk.io/blog/dependency-injection-python/)
* [SQLAlchemy for MySQL and MariaDB](https://docs.sqlalchemy.org/en/20/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mariadbconnector)
* [How to connect Python programs to MariaDB](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/)
* [Using SQLAlchemy with MariaDB Connector/Python: Part 1](https://mariadb.com/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-1/)
* [Using SQLAlchemy with MariaDB Connector/Python: Part 2](https://mariadb.com/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-2/)
* [Repository Pattern with Context Variables in Async Python](https://medium.com/@sawaamun/repository-pattern-with-context-variables-in-async-python-519728211d67)
  
Sería todo. Disfrutenlo.

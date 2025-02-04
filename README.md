# Timefly-Backend

Timefly-Backend es una API REST diseñada para gestionar el registro de llegadas y salidas de personal. Este proyecto está construido utilizando Django y Django Rest Framework, y está configurado para usar una base de datos SQLite.

## Tecnologías

Este proyecto utiliza las siguientes tecnologías:

- **Python 3.12.3**: Lenguaje de programación utilizado para el desarrollo del backend.
- **Django 5.1.4**: Framework web de alto nivel que fomenta el desarrollo rápido y el diseño limpio y pragmático.
- **Django Rest Framework 3.15.2**: Framework poderoso y flexible para construir APIs web.
- **Dotenv 1.0.1**: Herramienta para cargar variables de entorno desde un archivo `.env`.
- **SQLite3**: Sistema de gestión de bases de datos relacional ligero.

## Configuración del Proyecto

### Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/IamRodion/Timefly-Backend.git
   cd Timefly-Backend
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:

   Crea un archivo `.env` en el directorio raíz del proyecto que define la clave secreta de Django y más configuraciones necesarias para el funcionamiento del proyecto:

   ```bash
   python deploy.py
   ```

   Se verá el siguiente menú, el cual se puede navegar usando las flechas o números. Y enter para seleccionar la opción:

   ```
                     DEPLOY.PY

   [1] Configuración para desarrollo
   [2] Configuración para servidor
   [0] Cerrar deploy.py
   ```

   Ten en cuenta que sí eliges la opción **Configuración para servidor** debes configurar manualmente Apache, Nginx, Guvicorn o el servidor http que uses.

### Ejecución

1. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   python manage.py makemigrations api
   python manage.py migrate
   ```

2. Crea un usuario administrador para acceder a la ruta /admin/

   ```bash
   python manage.py createsuperuser
   ```

3. Re-organiza los archivos "static" en una sola ruta raíz "static"

   ```bash
   python manage.py collectstatic
   ```

4. Inicia el servidor:

   ```bash
   python manage.py runserver
   ```

5. Accede a la API en `http://localhost:8000`.

## Endpoints

### /

- **GET /**: Muestra la documentación

### /api/

- **GET /api/Worker/**: Obtiene una lista de todos los trabajadores registrados.
- **POST /api/Worker/**: Crea un nuevo trabajador. Requiere un cuerpo de solicitud con los campos `firstname`, `lastname`, `email`, `employee_id`, `department`, `hire_date`, y `active`.

- **GET /api/Worker/employee/{employee_id}/**: Obtiene una lista de todos los trabajadores registrados.

- **GET /api/Worker/{id}/**: Obtiene los detalles de un trabajador específico por su `id`.
- **PUT /api/Worker/{id}/**: Actualiza la información de un trabajador específico. Requiere un cuerpo de solicitud con los campos a actualizar.
- **DELETE /api/Worker/{id}/**: Elimina un trabajador específico por su `id`.

- **GET /api/TimeEntry/**: Obtiene una lista de todos los registros de tiempo.
- **POST /api/TimeEntry/**: Crea un nuevo registro de tiempo. Requiere un cuerpo de solicitud con los campos `worker`, `time`, y `entry_type`.

- **GET /api/TimeEntry/{id}/**: Obtiene los detalles de un registro de tiempo específico por su `id`.
- **PUT /api/TimeEntry/{id}/**: Actualiza un registro de tiempo específico. Requiere un cuerpo de solicitud con los campos a actualizar.
- **DELETE /api/TimeEntry/{id}/**: Elimina un registro de tiempo específico por su `id`.

### /admin/

- **/admin/**: Interfaz de administración de Django para gestionar los modelos y datos de la aplicación. Requiere autenticación de usuario administrador.

## Estructura del Proyecto

- **api/models.py**: Define los modelos `Worker` y `TimeEntry` para representar a los trabajadores y sus registros de tiempo.
- **Timefly/settings.py**: Configuración del proyecto, incluyendo aplicaciones instaladas, base de datos, y CORS.
- **README.md**: Documentación del proyecto.

## Modelos

### Worker

Modelo que representa a un trabajador con los siguientes campos:

- `firstname`: Nombre del trabajador.
- `lastname`: Apellido del trabajador.
- `email`: Correo electrónico del trabajador.
- `employee_id`: Identificador único del trabajador.
- `department`: Departamento al que pertenece el trabajador.
- `hire_date`: Fecha de contratación.
- `active`: Estado activo del trabajador.

### TimeEntry

Modelo que representa un registro de tiempo con los siguientes campos:

- `worker`: Referencia al trabajador asociado.
- `time`: Fecha y hora del registro.
- `entry_type`: Tipo de registro (Entrada o Salida).

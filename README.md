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

   Crea un archivo `.env` en el directorio raíz del proyecto y define la clave secreta de Django:

   ```bash
   python secret_key_gen.py
   ```

### Ejecución

1. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

2. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

3. Accede a la API en `http://localhost:8000`.

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
- `employe_id`: Identificador único del trabajador.
- `department`: Departamento al que pertenece el trabajador.
- `hire_date`: Fecha de contratación.
- `active`: Estado activo del trabajador.

### TimeEntry

Modelo que representa un registro de tiempo con los siguientes campos:

- `worker`: Referencia al trabajador asociado.
- `time`: Fecha y hora del registro.
- `entry_type`: Tipo de registro (Entrada o Salida).
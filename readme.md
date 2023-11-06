# Aplicación de Tareas con Autenticación - Flask

Esta es una aplicación web de gestión de tareas desarrollada con Flask que incluye autenticación de usuarios. Los usuarios pueden crear, ver, actualizar y eliminar tareas después de autenticarse en la aplicación.

Si quieres ejecutar el sitio en tu entorno para mejorar la aplicación o practicar por tu cuenta puedes seguir leyendo :)

## Requisitos

- Python 3.x
- PostgreSQL instalado y configurado
- Conocimiento básico de Flask

## Configuración del Proyecto

Siga estos pasos para configurar y ejecutar la aplicación:

1. Clona el repositorio desde GitHub:

   ```bash
   git clone https://github.com/tuusuario/tu-proyecto.git
   cd tu-proyecto
   ```
2. Crea un entorno virtual para el proyecto:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   ```Linux/macOS
   source venv/bin/activate o . venv/bin/activate
   ```
   ```Linux/macOS
   venv\Scripts\activate
   ```
4. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
5. Configura las variables de entorno necesarias. Debes establecer las siguientes variables en tu entorno:
   ```bash
    FLASK_APP=app
    FLASK_ENV=development
    FLASK_DATABASE_USER=tu_usuario_de_postgresql
    FLASK_DATABASE_PASSWORD=tu_contraseña_de_postgresql
    FLASK_DATABASE_HOST=tu_host_de_postgresql
    FLASK_DATABASE=tu_nombre_de_base_de_datos
    SECRET_KEY=una_clave_secreta 
   ```
6. Inicializa la base de datos. Ejecuta el siguiente comando para crear las tablas necesarias en la base de datos: 
   
   ```bash
   flask init-db
   ```
7. Ejecuta la aplicación:
    ```bash
   flask run
   ```



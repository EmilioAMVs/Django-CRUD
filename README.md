TaskMaster - Lista de Tareas

TaskMaster es una aplicación web que permite a los usuarios gestionar sus tareas de manera eficiente. Los usuarios pueden crear, editar, eliminar y visualizar sus tareas, con la opción de asignar prioridades y fechas límite. Está desarrollado con Django como framework de backend y Bootstrap para el frontend, proporcionando una experiencia visual intuitiva y responsiva.

Características

	•	Gestión de Tareas: Los usuarios pueden crear tareas con un título, descripción, prioridad (normal o alta), estado, y fechas de creación y cumplimiento.
	•	Autenticación: Cada tarea está asociada a un usuario, por lo que es necesario registrarse e iniciar sesión para gestionar las tareas.
	•	Prioridades: Las tareas pueden tener dos niveles de prioridad: normal o alta.
	•	Fechas Importantes: Cada tarea registra su fecha de creación y la fecha en que se espera que se complete.
	•	Estado de la Tarea: Los usuarios pueden actualizar el estado de la tarea (completada o pendiente).
	•	Interfaz Responsiva: La interfaz está diseñada con Bootstrap, lo que asegura que se vea bien en cualquier dispositivo.

Tecnologías Utilizadas

	•	Backend: Django 5.1.1
	•	Sistema de autenticación de usuarios integrado.
	•	Forms personalizados para la creación y edición de tareas.
	•	Frontend: Bootstrap 5
	•	Estilos consistentes y responsivos para una mejor experiencia de usuario.
	•	Base de Datos: SQLite (por defecto, pero puede ser cambiada a cualquier base de datos soportada por Django).
	•	Despliegue: Azure Web Services
	•	Desplegado como una aplicación en la nube con soporte para escalabilidad.

Instalación y Configuración

Requisitos Previos

	•	Python 3.8 o superior.
	•	Virtualenv para aislar el entorno del proyecto.
	•	Django 5.1.1 instalado.

Instrucciones de Instalación

	1.	Clonar este repositorio:

git clone https://github.com/EmilioAMVs/Django-CRUD.git
cd taskmaster


	2.	Crear un entorno virtual e instalar dependencias:

python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt


	3.	Aplicar las migraciones para la base de datos:

python manage.py migrate


	4.	Iniciar el servidor de desarrollo:

python manage.py runserver


	5.	Acceder a la aplicación en http://localhost:8000.

Despliegue en Azure

Para desplegar en Azure, asegúrate de:

	•	Configurar las variables de entorno como ALLOWED_HOSTS y CSRF_TRUSTED_ORIGINS.
	•	Asegurar que tienes los archivos requirements.txt y Procfile para el despliegue.


Este README cubre los aspectos esenciales del proyecto, desde las funcionalidades hasta la instalación y despliegue.
**_TaskMaster - Lista de Tareas_** 

TaskMaster es una aplicación web que permite a los usuarios gestionar sus tareas de manera eficiente. Los usuarios pueden crear, editar, eliminar y visualizar sus tareas, con la opción de asignar prioridades y fechas límite. Está desarrollado con Django como framework de backend y Bootstrap para el frontend, proporcionando una experiencia visual intuitiva y responsiva. Además de un deploy en Azure.
<br><br><br>
**Características**
<br><br>
**• Gestión de Tareas:** 
 	Los usuarios pueden crear tareas con un título, descripción, prioridad (normal o alta), estado, y fechas de creación y cumplimiento.<br><br>
**• Autenticación:** 
 	Cada tarea está asociada a un usuario, por lo que es necesario registrarse e iniciar sesión para gestionar las tareas.<br><br>
**• Prioridades:** 
 	Las tareas pueden tener dos niveles de prioridad: normal o alta.<br><br>
**• Fechas Importantes:** 
 	Cada tarea registra su fecha de creación y la fecha en que se espera que se complete.<br><br>
**• Estado de la Tarea:** 
 	Los usuarios pueden actualizar el estado de la tarea (completada o pendiente).<br><br>
**• Interfaz Responsiva:** 
 	La interfaz está diseñada con Bootstrap, lo que asegura que se vea bien en cualquier dispositivo.
<br><br><br><br>
**Tecnologías Utilizadas**
<br><br>
**• Backend:** Django 5.1.1
	Sistema de autenticación de usuarios integrado.
	Forms personalizados para la creación y edición de tareas.

**• Frontend:** Bootstrap 5
	Estilos consistentes y responsivos para una mejor experiencia de usuario.

**• Base de Datos:** PostgreSQL
	Base de Datos en la nube en Railway App
 
**• Despliegue:** Azure Web Services
	Desplegado como una aplicación en la nube con soporte para escalabilidad.

<br><br>
**Instalación y Configuración**
<br><br><br>
**Requisitos Previos:**

• Python 3.12<br><br>
• Virtualenv para aislar el entorno del proyecto.<br><br>
• Django 5.1.1 instalado.<br><br>
• Las demas dependencias se encuentran declaradas en el archivo _**requeriments.txt**_

 
<br><br>
**Instrucciones de Instalación**

1. Clonar este repositorio:

		git clone https://github.com/EmilioAMVs/Django-CRUD.git
		cd Django-CRUD


2. Crear un entorno virtual e instalar dependencias:

		python -m venv venv
		source venv/bin/activate   # En Windows: venv\Scripts\activate
		pip install -r requirements.txt


3.	Aplicar las migraciones para la base de datos:

		python manage.py migrate


4.	Iniciar el servidor de desarrollo:

		python manage.py runserver


5.	Para el entorno de producción acceder a:
   
		https://taskmaster.azurewebsites.net

Despliegue en Azure

Para desplegar en Azure, asegúrate de:

	• Configurar las variables de entorno como ALLOWED_HOSTS y CSRF_TRUSTED_ORIGINS.
	• Asegurarse de que el archivo requirements.txt este actualizado con todas las dependencias.



# DESARROLLADO POR: 
**JOEL ALEXANDER RAMIREZ NUÑEZ**
# Se realiza el proyecto cumpliendo con los siguientes requerimientos satisfactoriamente:
- 1: Modulo para Registro de Usuarios: 127.0.0.1:8000/register 
- 2: Login o inicio de Sesión para Usuarios 127.0.0.1:8000/login
- 3: Sala de chat publica 127.0.0.1:8000/chat
- 4: Eliminación de mensajes por parte de los usuarios  127.0.0.1:8000/chat


# BACKEND
- 1: Se realiza el BACKEND en Django: 
  
- 2: Se Utiliza Base de Datos SQLite para facilitar la portabilidad de los datos y poder realizar pruebas con información “usuarios y mensajes” Previamente ingresados.
- 3: Se Utiliza principalmente Django REST Framework en toda la implementación..
    GET 127.0.0.1:8000/users, GET 127.0.0.1:8000/users/:id, POST 127.0.0.1:8000/users, PUT 127.0.0.1:8000/users/:id, DELETE 127.0.0.1:8000/users/:id,
    GET 127.0.0.1:8000/messages, GET 127.0.0.1:8000/messages/:id, POST 127.0.0.1:8000/messages, PUT 127.0.0.1:8000/messages/:id, DELETE 127.0.0.1:8000/messages/:id,
- 4: Se Utilizan las vistas basadas en templates que nos ofrece Django.

# Observaciones y Puntos a Mejorar
En este proyecto para poder generar una similitud con el tiempo real de la mensajería, utilicé jquery, puesto que de esta manera se pueden observar todos los mensajes e interacciones que tienen los usuarios en la sala de CHAT,  cabe resaltar que lo ideal en este tipo de proyectos es utilizar Channels para que la respuesta y la vista de todos los mensajes de los usuarios logeados sea en tiempo real; La implementación de channels me genero algunos conflictos de sistema, por ello no logre implementarla completamente y decidí utilizar Jquery para sustituir este comportamiento en el <div> que contiene la mensajería. 


# Paso 1: Descargar el repositorio
# Paso 2: Configurar Entorno
Preferiblemente utilizar un Virtualenv.
Este se instala con el siguiente comando  virtualenv env
- 1: Activar Entorno virtual  “cd env/scripts”
- 2: Posterior a activar el entorno virtual instalar los requerimientos para el proyecto  “pip install -r requirements.txt”

# Paso 3: Una vez configurado el entorno virtual e instalados todos los requierements, procedemos a ejecutar el proyecto. “Python manage.py runserver”

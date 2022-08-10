# FECODER

Entrega del Proyecto final

Aplicación web estilo blog programada en Python y Django.

## Inicio

Es posible acceder al proyecto de dos formas:

1. Descargando el repositorio desde GitHub haciendo clic [aquí](https://github.com/ShaditCuber/FECODER_APP/tree/new). 

2. Directamente desde el sitio web subido a Heroku mediante el siguiente [enlace](https://fecoder.herokuapp.com/).

## Requisitos previos

Si opta por la primera opción (descargar el Proyecto desde GitHub), deberá contar con una serie de requisitos previos.

+ Python
+ Pip
+ Virtualenv
+ Django
+ Módulos extras

### Instalación de componentes necesarios

#### Instalar Python
1. Ir a [python.org/downloads](https://www.python.org/downloads/) y descargar la última versión de python.
2. Luego de descargar el archivo, ejecutarlo y proceder con la instalación.

**SUGERENCIA**: Se recomienda agregar Python al PATH durante la instalación.

####  Instalar pip
+ ```python -m pip install -U pip```

####  Instalar virtualenv
+ ```pip install virtualenv```

####  Crear un nuevo entorno virtual:

1. Crear una carpeta para el entorno virtual, ej.: ```entorno```
2. Acceder a la carpeta creada: ```cd entorno```
3. Crear el entorno: ```python -m virtualenv fecoder-env```
4. Activar el entorno: ```cd fecoder-env\Scripts\activate.bat```

####  Instalar Django y el resto de los módulos utilizados

+ Ir a la carpeta del proyecto clonada desde git.
+ Estando ubicado en la carpeta del proyecto
+ Instalar los módulos: ```pip install -r requirements.txt```

-asgiref, dj-database-url, Django, django-ckeditor, django-js-asset, gunicorn, Pillow, psycopg2, python-decouple, sqlparse, tzdata, whitenoise-

## Navegación del sitio
Al ingresar al sitio web, en la cabecera se encuentra la **barra de navegación**. A la izquierda está ubicado el logo del blog con la opción **Inicio** y a la derecha las opciones **Ingresar y Registro**.

En el cuerpo de la página aparecen los últimos posts creados, un cuadro de búsqueda y un formulario de contacto.

**Creación de nuevos usuarios**
Pasos para crear un usuario:

1. Clic sobre el menú "**Registro**" de la barra de navegación.
2. Completar los campos correspondientes.
3. Clic sobre el botón "**Registrarme**".

**Ingreso de usuarios**
Pasos para ingresar con un usuario creadi:

1. Clic sobre el menú "**INGRESAR**" de la barra de navegación.
2. Completar los campos correspondientes.
3. Clic sobre el botón "**INICIAR SESIÓN**".

En caso de no recordar su contraseña puede hacer clic sobre el botón **"OLVIDÉ LA CONTRASEÑA"**, escribir su correo electrónico y luego dar clic sobre el botón **"Enviar Correo"**.

**Búsqueda de posts**
Pasos para buscar un post:

1. Ir al formulario de búsqueda ubicado en la parte superior derecha de la página de inicio.
2. Escribir el nombre del post que se desea buscar.
3. Clic sobre el botón "Buscar".

**Contactarse con el blog**
En la parte inferior de la página de inicio, seguir los siguientes pasos:

1. Escribir un nombre de contacto.
2. Escribir un cellular de contacto.
3. Escribir un correo de contacto.
4. Escribir el mensaje.
5. Presionar el botón "**Enviar**"


## Ingreso como Usuario
Pasos para ingresar como Usuario

1. Clic sobre el menú "**INGRESAR**" de la barra de navegación.
2. Completar los campos con los datos correspondientes.
3. Clic sobre el botón "**INICIAR SESIÓN**"

Al ingresar al sitio web como Usuario, en la cabecera se encuentra la **barra de navegación**. A la izquierda está ubicado el logo del blog con la opción **Inicio** y a la derecha la opción **Subir Post y un desplegable con las opciones Mis Posts, Ver Perfil, Editar Perfil, Cambiar Contraseña, Chats y Cerrar Sesión**".

Desde el menu "**Subir Post**" es possible crear nuevos Posts y subirlos al blog.


**Crear un nuevo Post**
Pasos para crear un post:

1. Clic sobre el menú "**Subir Post**" de la barra de navegación.
2. Completar los campos correspondientes.
3. Elegir una imagen. 
4. Clic sobre el botón "**Enviar**".

Si los datos ingresados son correctos, se informará por pantalla y se guardará el post dentro de la base de datos. Una vez creado el post, éste se mostrará en la página de inicio.

Si existe algún error con los datos ingresados, se informará por pantalla y no se guardará el post dentro de la base de datos.


## Ingreso como administrador
Pasos para ingresar como administrador

1. Clic sobre el menú "**INGRESAR**" de la barra de navegación.
2. Completar los campos de Usuario y Contraseña con admin y admin.
3. Clic sobre el botón "**INICIAR SESIÓN**"

Al ingresar al sitio web como administrador, en la cabecera se encuentra la **barra de navegación**. A la izquierda está ubicado el logo del blog con la opción **Inicio** y a la derecha las opciones **Usuarios, Contactos, Subir Post y un desplegable con las opciones Mis Posts, Ver Perfil, Editar Perfil, Cambiar Contraseña, Chats y Cerrar Sesión***".

Desde el menú "Usuarios", es possible Eliminar, Editar o Desactivar un Usuario.
Desde el menu "Contacto" es possible realizer búsquedas de los contactos.
Desde el menu "Subir Post" es possible crear nuevos Posts y subirlos al blog.


**Crear un nuevo Post**
Pasos para crear un post:

1. Clic sobre el menú "**Subir Post**" de la barra de navegación.
2. Completar los campos correspondientes.
3. Elegir una imagen. 
4. Clic sobre el botón "**Enviar**".

Si los datos ingresados son correctos, se informará por pantalla y se guardará el post dentro de la base de datos. Una vez creado el post, éste se mostrará en la página de inicio.

Si existe algún error con los datos ingresados, se informará por pantalla y no se guardará el post dentro de la base de datos.


**Uso del chat**
Pasos para utilizar el chat:

1. Desde el menu desplegable ubicado en la cabecera, ir a la opción "**Chats**".
2. Clic en el menu "Salas".
3. Elegir una sala para chatear hacienda clic en el botón "**Chaterar**" de la sala correspondiente.
4. Escribir el mensaje
5. Clic en el botón "**Enviar**".

Para salir del chat y regresar al sitio web, hacer clic en el botón "**Salir**" ubicado en la cabecera.

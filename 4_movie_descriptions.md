## Descripciones de películas

En esta etapa del proyecto se utilizará la API de openAI para generar descripciones de algunas películas que se agregarán a la base de datos.
Para esto, el archivo ``movie_titles.json`` que se encuentra en la raíz del proyecto, tiene una lista de películas a las que se le agregará información.

El archivo [movie_descriptions.py](movie_descriptions.py) muestra los pasos para utilizar la api de openai para obtener la descripción de las películas en la lista.
En este archivo se pueden ver dos funciones principales:

1. Creación de una función auxiliar para comunicarse con la api
2. Creación de un prompt que nos ayude a pedir de forma correcta la descripción de las películas.

Cuando ejecute el script, deberá ver en la consola algo de la siguiente forma:

![Fork 1](imgs/md1.png)

Puede ver que se imprime el nombre de la película, el prompt completo y la descripción obtenida.

El archivo que se genera al correr todo el script (incluyendo las lineas comentadas) genera un archivo ``movie_descriptions.json``
que se va a utilizar para alimentar la base de datos de películas. Para esto nos vamos a dirigir a la carpeta ``DjangoProjectBase``. Asumiendo que la consola está en el directorio raíz del proyecto ``ProyectoPeliculas2023-2_Taller3``, en la consola escriba lo siguiente:

````shell
cd DjangoProjectBase
````
Si corre el servidor se dará cuenta que este es el proyecto que se creó en el workshop 2

````shell
python manage.py runserver
````
![Fork 1](imgs/md2.png)

Ahora dentro de la carpeta de la app movie debe crear una carpeta management y dentro de esta una carpeta commands. Después, debe crear el archivo add_descriptions_db.py.

![Fork 1](imgs/md2.png)






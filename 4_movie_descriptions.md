## Descripciones de películas

En esta etapa del proyecto se utilizará la API de openAI para generar descripciones de algunas películas que se agregarán a la base de datos.
Para esto, el archivo ``movie_titles.json`` que se encuentra en la raíz del proyecto, tiene una lista de películas a las que se le agregará información.

El archivo [movie_descriptions.py](movie_descriptions.py) muestra los pasos para utilizar la api de openai para obtener la descripción de las películas en la lista.
En este archivo se pueden ver dos funciones principales:

1. Creación de una función auxiliar para comunicarse con la api
2. Creación de un prompt que nos ayude a pedir de forma correcta la descripción de las películas.

Cuando ejecute el script, deberá ver en la consola algo de la siguiente forma:

![Fork 1](imgs/md1.png)






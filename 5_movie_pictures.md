## Ilustraciones de pelíuclas

Ahora se utilizará la API de generación de imágenes de openAI para crear ilustraciones de las películas y modificar la imagen por defecto que se tiene en la base de datos.
Primero, se utilizará un script para entender el funcionamiento de la API y después se verá cómo se podría utilizar para modificar las imágenes de la base de datos.

En la consola va a volver al directorio raíz ``ProyectoPeliculas2023-2_Taller3``

````shell
cd ..
````

El script [movie_pictures.py](movie_pictures.py) muestra como conectarse a la API de generación de imágenes. En este caso, vamos a utilizar el título de la película como descripción, sin embargo, usted puede generar diferentes prompts para generar mejores ilustraciones, o utilizar la descripción de las películas.

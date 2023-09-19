## Ilustraciones de pelíuclas

Ahora se utilizará la API de generación de imágenes de openAI para crear ilustraciones de las películas y modificar la imagen por defecto que se tiene en la base de datos.
Primero, se utilizará un script para entender el funcionamiento de la API y después se verá cómo se podría utilizar para modificar las imágenes de la base de datos.

En la consola va a volver al directorio raíz ``ProyectoPeliculas2023-2_Taller3``

````shell
cd ..
````

El script [movie_pictures.py](movie_pictures.py) muestra como conectarse a la API de generación de imágenes. En este caso, vamos a utilizar el título de la película como descripción, sin embargo, usted puede generar diferentes prompts para generar mejores ilustraciones, o utilizar la descripción de las películas.

Cuando ejecute este script, debe ver en la consola el nombre de la película, la descripción y en una ventana a parte la ilustración creada por la API

![Fork 1](imgs/mp1.png)

Se podría crear un script para crear y modificar las imágenes de la base de datos en la carpeta ``movie/management/commands``. Por ejemplo, si se ubica el archivo [add_images_db.py](aux_files/add_images_db.py) en la carpeta mencionada y se ejecuta el comando:

````shell
python manage.py add_images_db
````

Se estaría consultando la API de openAI de generación de imágenes para crear una imagen nueva para cada archivo de la base de datos. En este caso, por cuestión de tiempo, se omitirá este paso. Las imágenes para cada película se pueden descargar del siguiente link:

[images](https://drive.google.com/file/d/1-j6Q-AwrxO9q-BhPRHCp_MS2V6OYIhod/view?usp=sharing)

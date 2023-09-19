#importar librerías
import os
import openai
import json
from dotenv import load_dotenv, find_dotenv

#Se lee del archivo .env la api key de openai
_ = load_dotenv('openAI.env')
openai.api_key  = os.environ['openAI_api_key']

#Se carga la lista de películas de movie_titles.json
with open('movie_titles.json', 'r') as file:
    file_content = file.read()
    movies = json.loads(file_content)

print(movies[0])


#Se genera una función auxiliar que ayudará a la comunicación con la api de openai
#Esta función recibe el prompt y el modelo a utilizar (por defecto gpt-3.5-turbo)
#devuelve la consulta hecha a la api

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

#Definimos una instrucción general que le vamos a dar al modelo 

instruction = "Vas a actuar como un aficionado del cine que sabe describir de forma clara, concisa y precisa \
cualquier película en menos de 200 palabras. La descripción debe incluir el género de la película y cualquier \
información adicional que sirva para crear un sistema de recomendación."

#Definimos el prompt
movie = movies[0]['title']
prompt = f"{instruction} Has una descripción de la película {movie}"

print(prompt)

#Utilizamos la función para comunicarnos con la api
response = get_completion(prompt)

print(response)



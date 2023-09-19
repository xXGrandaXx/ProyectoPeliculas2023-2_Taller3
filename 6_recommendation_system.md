## Sistema de recomendación

Para el sistema de recomendación de películas se utilizará la API de generación de embeddings de openAI. De forma general, un embedding es una representación numérica de cualquier fenómeno, puede ser una  imagen, un video, o como en este caso, texto.

![Fork 1](imgs/sr1.svg)

__Concepto Básico:__ Un embedding es básicamente una proyección de un objeto no vectorial en un espacio vectorial. En el contexto de PLN, los embeddings convierten palabras o frases en vectores de números reales.

__Utilidad:__ Estos vectores capturan la semántica y las relaciones contextuales entre las palabras. Palabras con significados similares o que a menudo aparecen en el mismo contexto tendrán embeddings similares, es decir, sus vectores estarán cerca en el espacio vectorial.

El script [movie_recommendations.py](movie_recommendations.py)

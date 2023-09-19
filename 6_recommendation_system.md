## Sistema de recomendación

Para el sistema de recomendación de películas se utilizará la API de generación de embeddings de openAI. De forma general, un embedding es una representación numérica de cualquier fenómeno, puede ser una  imagen, un video, o como en este caso, texto.

![Fork 1](imgs/sr1.svg)

__Concepto Básico:__ Un embedding es básicamente una proyección de un objeto no vectorial en un espacio vectorial. En el contexto de PLN, los embeddings convierten palabras o frases en vectores de números reales.

__Utilidad:__ Estos vectores capturan la semántica y las relaciones contextuales entre las palabras. Palabras con significados similares o que a menudo aparecen en el mismo contexto tendrán embeddings similares, es decir, sus vectores estarán cerca en el espacio vectorial.

Se utilizará una medida de similitud muy conocida para calcular qué tan parecido es un prompt de entrada con las descripciones de las películas. 

La similitud de coseno mide el coseno del ángulo entre dos vectores, en este caso, dos embeddings. Es una métrica popular para calcular la similitud en espacios de alta dimensión como el de los embeddings.

Funciona de la siguiente manera:

    Fórmula: La similitud de coseno entre dos vectores AA y BB se calcula como el producto punto de los vectores dividido por el producto de sus magnitudes:

\[
similitud(A,B)=A⋅B∥A∥∥B∥similitud(A,B)=∥A∥∥B∥A⋅B
\]​

Donde $A⋅B$ es el producto punto de los vectores y $∥A∥$ y $∥B∥$ son las magnitudes (o normas) de los vectores A y B respectivamente.

    Rango de Valores: La similitud de coseno produce un valor entre -1 y 1. Un valor de 1 indica que los vectores son idénticos en dirección, un valor de -1 indica que son opuestos y un valor de 0 indica que son ortogonales (no relacionados).

    Aplicación a Embeddings: Cuando se utiliza con embeddings, la similitud de coseno permite determinar qué tan similares son semánticamente dos palabras o frases. Si sus embeddings son cercanos en el espacio vectorial (es decir, tienen un ángulo pequeño entre ellos), su similitud de coseno será cercana a 1.

En resumen, la similitud de coseno compara la orientación de dos vectores en lugar de su magnitud, siendo una métrica esencial para evaluar la similitud semántica entre embeddings en el procesamiento del lenguaje natural.

El script [movie_recommendations.py](movie_recommendations.py)

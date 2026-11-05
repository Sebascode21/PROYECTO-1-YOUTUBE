# PROYECTO 1 YOUTUBE MX

Es un estudio sobre los datos de los videos virales de Mexico para aquellas personas que quieran ver las metricas para ver si su video es viral.

## La pregunta
¿Cuáles son los videos mas virales de Mexico?

## Los datos

- De dónde salen: (https://www.kaggle.com/datasets/datasnaek/youtube-new)
- Cuántos son: (40451) filas y (16) columnas
- Qué es cada fila: (un video)

## Qué he limpiado y por qué

- Nos hemos quedado con las columnas más relevantes para el caso y se cambiaron a español. Se observó que la columna "descripción" tenía un 10 por ciento en huecos y se procedió a rellenarlos con "sin descripción". También se encontraron 49 filas duplicadas y se procedió a eliminarlas. Con los ID duplicados, nos quedamos con el primero de cada una y con más visualizaciones.

## Lo que he encontrado
1- Se ha descubierto que muy pocos vídeos son virales (3635 videos) y tienen la gran mayoría de comentarios. Consideramos virales en este caso, los vÍdeos iguales o mayores a 500.000 visualizaciones.
2- Observamos en la categorÍa 24 cómo tiene más vídeos pero no son los más virales respecto a las categorías 23, 20 y 10, con menos vídeos y más virales.
3- Se han observado vídeos virales, pero con 0 o pocos comentarios debido a la temática del vídeo, que no genera comentarios.

## La app
En la app se pueden filtrar videos por categorías, numero de visualizaciones y etiquetas. Se pueden buscar videos por nombres, se pueden ver graficas sobre las medianas de visualizaciones, la mediana de me gusta y la mediana de no me gusta, así como buscar los parámetros de tu video para ver si puede ser viral.

## Cómo ejecutarlo

1. Crear un entorno e instalar las librerías: `pip install -r requirements.txt`
2. El EDA está en `eda.ipynb`.
3. La app se abre con `streamlit run app.py`.

## Autor

Sebastian parras/https://github.com/Sebascode21/PROYECTO-1-YOUTUBE

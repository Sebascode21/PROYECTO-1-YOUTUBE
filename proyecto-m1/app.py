# La app de mi proyecto
# Para verla, en la terminal: streamlit run app.py
# Son los mismos pasos que en app_pisos.py y app_titanic.py. Si te atascas, busca el mismo paso allí.



# Paso 1. La página
# 1.1 Importa streamlit y pandas.
# 1.2 Pon el nombre de la pestaña del navegador, la página a todo lo ancho y un título que diga de qué va tu proyecto.
# 1.3 Debajo, una o dos frases con st.write: qué pregunta responde la app y de dónde salen los datos.
from pathlib import Path
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Los videos trending de Mexico",
    page_icon="▶️",
    layout="wide"
)

st.title("VIDEOS TRENDING EN MEXICO")

st.write("¿Que hace que un video llegue a tendencias en Youtube Mexico?")

# Paso 2. Los datos
# 2.1 La función cargar_datos, con @st.cache_data encima, que lea "datos/datos_limpios.csv" y lo devuelva.
#     La limpieza ya está hecha en el cuaderno, así que la función solo lee y devuelve, como en la carta del bar.
# 2.2 Llama a la función y guarda la tabla en una variable con el nombre de tus datos.
RUTA= Path(__file__).parent/"datos"/"datos_limpios.csv"
@st.cache_data
def cargar_datos():
    return pd.read_csv(RUTA)

videos= cargar_datos()
 


# Paso 3. Los filtros
# 3.1 En la barra de la izquierda (with st.sidebar:), al menos dos filtros:
#     un desplegable o unos botones para una columna de texto, con "Todos" al principio,
#     y una barra para una columna de números.
with st.sidebar:
    st.image("data:image/png;base64,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", use_container_width=True)
    st.header("Filtros")
    categorias=sorted(videos["categoria"].unique())
    categorias.insert(0,"todas")
    categoria=st.selectbox("categoria", categorias)

    num_visualizaciones= st.slider("Numero Visualizaciones",0,1000000,0,100000)

    etiquetas= st.radio("etiquetas",["si","No"])


# Paso 4. Filtrar
# 4.1 Empieza con filtrados = tu tabla, y después aplica un filtro por cada widget, como en los pisos.
filtrados=videos

if categoria != "todas":
    filtrados=filtrados[filtrados["categoria"]==categoria]
    
filtrados=filtrados[filtrados["visualizaciones"]>=num_visualizaciones]

if etiquetas=="si":
    filtrados=filtrados[filtrados["etiquetas"]!="[none]"]
else:
    filtrados=filtrados[filtrados["etiquetas"]=="[none]"]


# Paso 5. Si no queda nada
# 5.1 Si filtrados está vacía, saca un aviso con st.warning y para el programa con st.stop().
if len(filtrados)==0:
    st.warning("no hay categorias que cumplan los filtros")
    st.stop()


# Paso 6. Las métricas
# 6.1 Tres métricas en columnas, con los números más importantes para tu pregunta.
col1,col2,col3=st.columns(3)
with col1:
    st.metric("videos",len(filtrados))

with col2:
    st.metric("media de visualizaciones",round(filtrados["visualizaciones"].mean(),2))

with col3:
    st.metric("numero comentarios",filtrados["numero comentarios"].sum())


# Paso 7. Las pestañas
# 7.1 Al menos dos pestañas: una con la tabla filtrada y otra con dos gráficos.
# 7.2 Si tus datos tienen latitud y longitud, otra pestaña con el mapa.
tab1,tab2,tab3=st.tabs(["videos","graficos","¿Es tu video viral?"])
with tab1:
    st.header("Los videos filtrados")
    st.dataframe(filtrados)
    st.subheader("Busca un video")
    texto=st.text_input("Escribe un titulo")
    if texto !="":
        encontrados=videos[videos["titulo"].str.contains(texto,case=False)]
        st.dataframe(encontrados)

with tab2:
    colx,coly,colv=st.columns(3)
    with colx:
        st.subheader("visualizaciones mediana por categoria")
        media_visualizaciones=filtrados.groupby("id categoria")["visualizaciones"].median().sort_values(ascending=False)
        st.bar_chart(media_visualizaciones,horizontal=True)

    with coly:
        st.subheader("Mediana de me gusta por categoria")
        media_megusta=filtrados.groupby("id categoria")["me gusta"].median().sort_values(ascending=False)
        st.bar_chart(media_megusta,horizontal=True)

    with colv:
        st.subheader("Mediana de no me gusta por categoria")
        media_nogusta=filtrados.groupby("id categoria")["no me gusta"].median().sort_values(ascending=False)
        st.bar_chart(media_nogusta,horizontal=True)

# Paso 8. Una pregunta para el usuario
# 8.1 Una última pestaña con una pregunta, como "¿Cuánto cobrarías por tu piso?" o "¿Te habrías salvado?":
#     el usuario elige algo y la app le contesta con lo que dicen los datos.
with tab3:
    st.subheader("¿Podria ser tu video viral?")
    mi_categoria=st.selectbox("Categoria",sorted(videos["categoria"].unique()))
    mis_visual=st.slider("Visualizaciones",0,1000000,100000)
    mis_etiquetas=st.radio("Etiquetas",["si","No"])

    parecidos=videos[videos["categoria"]==mi_categoria]
    parecidos=videos[videos["visualizaciones"]>=mis_visual]
    sin_etiquetas=parecidos["etiquetas"].isna()|(parecidos["etiquetas"]=="[none]")
    if mis_etiquetas=="si":
        parecidos=parecidos[~sin_etiquetas]
    else:
        parecidos=parecidos[sin_etiquetas]


    if len(parecidos)==0:
        st.warning("No hay videos parecidos")
        st.stop()

    visualizacion=parecidos["visualizaciones"].median()
    mediana_visual=videos["visualizaciones"].median()

    st.metric("Videos como el tuyo",len(parecidos))
    st.metric("Mediana de visualizaciones de videos parecidos", int(visualizacion))
   

    umbral_viral=500000

    if visualizacion >=umbral_viral:
        st.success("Tu video es viral!")
    else:
        st.error("Tu video no es viral")

    st.subheader("Videos parecidos al tuyo")
    st.dataframe(parecidos)
import streamlit as st  # Importar Streamlit para la interfaz
from gtts import gTTS  # Importar la librería de Google para la conversión de texto a voz

def generar_audiolibro(texto, idioma, archivo_salida):  # Función que convierte texto en un archivo de audio
    tts = gTTS(text=texto, lang=idioma, tld='com')  # Crear el objeto de voz con el texto, idioma y acento
    tts.save(archivo_salida)  # Guardar el archivo de audio con el nombre proporcionado

# Título para la interfaz
st.title("Generador de Audiolibros")

# Caja de texto para ingresar el texto a convertir
texto_usuario = st.text_area("Escribe el texto aquí:")

# Diccionario para los idiomas disponibles
idiomas_disponibles = {
    "Español (es)": "es",
    "Inglés (en)": "en",
    "Francés (fr)": "fr",
    "Alemán (de)": "de"
}

# Menú desplegable para seleccionar el idioma
idioma_seleccionado = st.selectbox("Elige un idioma:", list(idiomas_disponibles.keys()))

# Diccionario para los acentos disponibles
acentos_disponibles = {
    "com": "Estados Unidos",
    "co.uk": "Reino Unido",
    "ca": "Canadá",
    "com.au": "Australia",
    "co.in": "India"
}

# Menú desplegable para seleccionar el acento
acento_seleccionado = st.selectbox("Selecciona un acento:", list(acentos_disponibles.keys()))

# Botón para generar el audiolibro
if st.button("Crear Audiolibro"):
    if texto_usuario:  # Verificar si se ha introducido un texto
        archivo_audio = "audiolibro_generado.mp3"  # Nombre del archivo de salida
        generar_audiolibro(texto_usuario, idiomas_disponibles[idioma_seleccionado], archivo_audio)  # Crear el audio
        st.audio(archivo_audio, format="audio/mp3")  # Reproducir el audiolibro generado
    else:
        st.error("Por favor, introduce un texto para generar el audiolibro.")  # Error si no se ingresa texto

import streamlit as st
from PIL import Image
import os
import time

from agent import invoke_agent

# Configuración general
st.set_page_config(page_title="Cargador de Imágenes", layout="centered")
st.title("🎨 Visualizador de Imágenes")

# Sidebar para subir imagen y ejecutar acción
st.sidebar.header("📁 Subir imagen")
uploaded_file = st.sidebar.file_uploader("Selecciona una imagen", type=["png", "jpg", "jpeg"])

# Mostrar vista previa si se cargó imagen
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.sidebar.image(image, caption="Vista previa", use_container_width=True)
    except Exception as e:
        st.sidebar.error(f"No se pudo mostrar la imagen: {e}")

# Botón de acción
if uploaded_file:

    if st.sidebar.button("💾 Cargar Informacion"):
            # Crear carpeta 'img' si no existe
            os.makedirs("img", exist_ok=True)

            # Ruta absoluta del archivo guardado
            filename = uploaded_file.name
            relative_path = os.path.join("img", filename)
            absolute_path = os.path.abspath(relative_path)

            # Guardar imagen en la carpeta
            image.save(relative_path)

            # Mostrar confirmación y ruta
            st.sidebar.success("✅ Imagen cargada con éxito")

            # Invocar al agente
            agent_response = invoke_agent(absolute_path)

            # Crear contenedor vacío para animación
            placeholder = st.empty()

            # Simular la escritura palabra por palabra
            words = agent_response.split()
            result = ""
            for word in words:
                result += word + " "
                placeholder.markdown(f"{result}")
                time.sleep(0.05)  # Puedes ajustar la velocidad aquí
            
            placeholder.markdown(agent_response)
else:
    st.info("Por favor, sube una imagen desde el panel lateral.")


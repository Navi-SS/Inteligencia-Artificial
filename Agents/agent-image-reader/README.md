
# 🖼️ Streamlit OCR Viewer con Agente Inteligente

Este proyecto permite a los usuarios subir imágenes a través de una interfaz interactiva hecha con **Streamlit**, visualizar una vista previa y ejecutar un agente que utiliza **IA y OCR** (Reconocimiento Óptico de Caracteres) para extraer texto estructurado desde la imagen. El resultado se muestra con un efecto dinámico de "escritura palabra por palabra" para mejorar la experiencia del usuario.

---

## 📁 Estructura del Proyecto

```
.
├── main.py          # Interfaz Streamlit y flujo principal
├── agent.py         # Agente OCR basado en LangGraph y Ollama
├── img/             # Carpeta donde se guardan imágenes subidas
└── README.md        # Documentación del proyecto
```

---

## 🚀 Requisitos

- Python 3.9+
- [Streamlit](https://streamlit.io)
- PIL (Pillow)
- [LangChain](https://python.langchain.com)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Ollama](https://ollama.com)
- Un modelo como `gemma3:4b-it-q4_K_M` descargado en Ollama

Instala dependencias necesarias:

```bash
pip install streamlit pillow langchain langgraph langchain-ollama
```

---

## ▶️ Cómo usar

1. Ejecuta el archivo principal:

```bash
streamlit run main.py
```

2. Desde la interfaz:
   - Sube una imagen (formatos permitidos: JPG, PNG, JPEG).
   - Observa la vista previa.
   - Haz clic en el botón `💾 Cargar Información`.
   - Verás cómo el texto extraído se escribe palabra por palabra en la pantalla.

---

## 📄 Descripción de Archivos

### `main.py`

Este archivo contiene la **interfaz gráfica con Streamlit**:

- Muestra un `sidebar` para subir imágenes.
- Guarda la imagen en la carpeta `img/` al presionar el botón.
- Muestra el resultado del agente con una animación palabra por palabra.
- Usa `invoke_agent` desde `agent.py`.

### `agent.py`

Este módulo contiene la **lógica del agente OCR**:

- Convierte imágenes a Base64 (`encode_image_to_base64`).
- Usa el modelo `gemma3` vía Ollama con **streaming activado**.
- Procesa la imagen para extraer texto y devolverlo en formato Markdown estructurado.
- Usa **LangGraph** para construir un flujo tipo grafo con nodos:
  - `run`: Procesa la imagen.
  - `optional`: Imprime el estado final.
- La función `invoke_agent(file_path)` ejecuta todo el flujo y devuelve el resultado.

---

## 💡 Funcionalidades Destacadas

- ✅ Carga y visualización de imágenes en Streamlit
- 🧠 OCR utilizando IA generativa vía Ollama
- ✨ Animación de texto en tiempo real (palabra por palabra)
- 🧱 Estructura modular separando lógica e interfaz
- 🧬 Grafo de estado para el flujo del agente con LangGraph

---

## 📌 Notas Adicionales

- Asegúrate de tener corriendo **Ollama** localmente y tener cargado el modelo `gemma3:4b-it-q4_K_M`.
- Puedes cambiar el modelo por cualquier otro compatible con imágenes y texto.
- El resultado de OCR depende de la calidad de la imagen y del modelo usado.

---

## 📷 Ejemplo de Uso

![demo](https://i.imgur.com/your_demo_image.gif)  
> Simulación de subida y análisis de imagen

---

## 🛠️ Futuras mejoras

- Agregar barra de progreso mientras se genera el texto
- Permitir subir múltiples imágenes
- Opción para descargar el texto procesado como `.md` o `.txt`
- Internacionalización (soporte multilenguaje en la interfaz)

---

## 🧑‍💻 Autor

Desarrollado con ❤️ por un apasionado de Python y Streamlit.

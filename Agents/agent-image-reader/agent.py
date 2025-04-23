# === Bibliotecas ===
import base64
from typing import TypedDict
from langgraph.graph import StateGraph
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama


# === Configuración ===
MODEL_NAME = "gemma3:4b-it-q4_K_M"

# === Utilidades ===
def encode_image_to_base64(image_path: str) -> str:
    """Convierte imagen a base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# === Agente OCR con Streaming ===
def perform_ocr_streaming(image_path: str):
    """Ejecuta OCR y transmite la salida al usuario."""
    image_base64 = encode_image_to_base64(image_path)

    # Configurar modelo con streaming
    model = ChatOllama(
        model=MODEL_NAME,
        temperature=0,
        streaming=True,
    )

    prompt = HumanMessage(
        content=[
            {
                "type": "text",
                "text": """Analyze the text in the provided image. Extract all readable content
                and present it in a structured Markdown format that is clear, concise, 
                and well-organized. Use proper formatting (e.g., headings, lists, code blocks).""",
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
            },
        ]
    )

    response_text = ""
    for chunk in model.stream([prompt]):
        if chunk.content:
            print(chunk.content, end="", flush=True)  # Muestra en tiempo real
            response_text += chunk.content

    return response_text

# === Nodos del grafo ===
def run(state):
    try:
        print("🧠 Procesando imagen con OCR (streaming)...\n")
        result = perform_ocr_streaming(state["file_path"])
        state["ocr_result"] = result
        return state
    except Exception as e:
        print(f"❌ Error en OCR: {e}")
        return state

def optional(state):
    print("\n✅ Proceso completado. Resultado almacenado en estado.")
    return state

# === Tipado del estado ===
class GraphState(TypedDict):
    file_path: str
    ocr_result: str

# === Grafo con LangGraph ===
workflow = StateGraph(GraphState)
workflow.add_node("entry", run)
workflow.add_node("info", optional)
workflow.add_edge("entry", "info")
workflow.set_entry_point("entry")
workflow.set_finish_point("info")
graph = workflow.compile()

# === Ejecutar ===
def invoke_agent(file_path):
    input_data = {"file_path": file_path}
    info = graph.invoke(input_data)
    return info["ocr_result"]

# input_data = {"file_path": "restaurant ticket 2.jpg"}
# graph.invoke(input_data)
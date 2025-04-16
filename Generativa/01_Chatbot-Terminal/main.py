from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Responde la pregunta de abajo.

Aqui esta el historial de la conversacion: {context}

Pregunta: {question}

Respuesta:
"""
# model_name = "hf.co/Qwen/Qwen2.5-Coder-3B-Instruct-GGUF:Q4_K_M"
model_name = "llama3.2:3b-instruct-q4_K_M"

model = OllamaLLM(model=model_name, streaming=True)  # Habilita streaming
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    """La función que maneja el chat conversacional
    """
    context = ""
    print("Bienvenido al chatbot, escribe 'adios' para salir.")
    while True:
        user_input = input("Tu: ")
        if user_input.lower() == "adios":
            break
        
        # Usar streaming
        for chunk in chain.stream({"context": context, "question": user_input}):
            print(chunk, end="", flush=True)
        print()  # Salto de línea al final de la respuesta

        context += f"\nUser: {user_input}\nAI: {chunk}"

if __name__ == "__main__":
    handle_conversation()

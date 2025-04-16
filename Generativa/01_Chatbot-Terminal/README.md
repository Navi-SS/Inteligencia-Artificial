
# Chatbot con LangChain y Ollama (Streaming)

Este es un ejemplo básico de un chatbot en consola que utiliza `LangChain` junto con `Ollama` para ofrecer respuestas generadas por modelos LLM. El chatbot mantiene un historial de conversación y utiliza streaming para mostrar las respuestas en tiempo real.

## Requisitos

- Python 3.9 o superior
- [Ollama](https://ollama.com/) instalado y corriendo con el modelo deseado
- Las siguientes bibliotecas de Python:

```bash
pip install langchain-core langchain-ollama
```

## Modelo usado

```python
model_name = "llama3.2:3b-instruct-q4_K_M"
```

> Puedes cambiarlo por otro modelo que tengas disponible localmente con Ollama.

## Prompt usado

```text
Responde la pregunta de abajo.

Aqui esta el historial de la conversacion: {context}

Pregunta: {question}

Respuesta:
```

## Cómo usar

1. Asegúrate de que `Ollama` esté corriendo y el modelo `llama3.2:3b-instruct-q4_K_M` esté instalado.
2. Ejecuta el script:

```bash
python main.py
```

3. Escribe tus preguntas en la consola.
4. Escribe `adios` para salir del chat.

---

¡Listo! Tu chatbot ya estará funcionando con respuestas fluidas gracias al streaming.

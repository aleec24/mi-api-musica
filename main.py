from fastapi import FastAPI
import openai
import requests

app = FastAPI()

# Clave de OpenAI para IA (Reemplaza con la tuya)
openai.api_key = "TU_CLAVE_OPENAI"

# Clave de Genius API para buscar letras (Reemplaza con la tuya)
GENIUS_API_KEY = "TU_CLAVE_GENIUS"

# Función para buscar letras en Genius
def buscar_letra(cancion):
    url = f"https://api.genius.com/search?q={cancion}"
    headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# Endpoint para responder preguntas sobre música
@app.get("/pregunta")
def responder_pregunta(query: str):
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return {"respuesta": respuesta["choices"][0]["message"]["content"]}

# Endpoint para obtener letras de canciones
@app.get("/letra")
def obtener_letra(cancion: str):
    return buscar_letra(cancion)

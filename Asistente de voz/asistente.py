import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Cliente para los "Oídos" (Whisper vía OpenAI)
client = OpenAI(api_key=os.getenv('NVIDIA_API_KEY'))

def escuchar(ruta_audio):
    """Fase 1: Convierte el MP3 a texto."""
    audio_file = open(ruta_audio, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription.text

def pensar(texto_usuario):
    """Fase 2: Mistral Large procesa el texto y responde."""
    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
    
    # Inyectamos tu llave de NVIDIA desde el .env
    headers = {
        "Authorization": f"Bearer {os.getenv('NVIDIA_API_KEY')}",
        "Accept": "application/json"
    }

    # Aquí le damos la personalidad al asistente (Ej: Modo Sarcástico)
    mensaje_sistema = "Eres un asistente robótico con una actitud sarcástica y algo agresiva. Tus respuestas deben ser cortas, directas y con humor negro."

    payload = {
        "model": "mistralai/mistral-large-3-675b-instruct-2512",
        "messages": [
            {"role": "system", "content": mensaje_sistema},
            {"role": "user", "content": texto_usuario} # Aquí entra lo que tú le dijiste
        ],
        "max_tokens": 150, # Limitamos a respuestas cortas para que hable rápido
        "temperature": 0.5,
        "stream": False # Lo apagamos para recibir la respuesta completa
    }

    # Hacemos la petición a NVIDIA
    response = requests.post(invoke_url, headers=headers, json=payload)
    respuesta_json = response.json()
    
    # Extraemos y devolvemos solo el texto de la IA
    return respuesta_json["choices"][0]["message"]["content"]

# --- Ejecución del Flujo ---
if __name__ == "__main__":
    print("Escuchando (procesando audio)...")
    texto_escuchado = escuchar("prueba.mp3")
    print(f"\nTú dijiste: {texto_escuchado}")

    print("\nPensando (Mistral vía NVIDIA)...")
    respuesta_ia = pensar(texto_escuchado)
    print(f"\nIA dice: {respuesta_ia}")
    
    # Fase 3 (Pendiente): Pasar 'respuesta_ia' a un motor de voz.
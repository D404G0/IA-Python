import requests
import json
from requests import Response
from datos import url, token

invoke_url = url
stream = False

headers = {
    "Authorization": "Bearer " + token,
}

# 1. Esta es tu lista viva en la memoria RAM
messages = [
    {
        "role": "system", 
        "content": "Eres un asistente que ayudaras a responder preguntas que te pidan, te limitaras estrictramente lo que te pidan sin agregar mas informacion"
    }
]

while True:

    user_input = input("Tu: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ("salir", "exit", "bye", "sayonara"):
        print("Chaoooo")
        break

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "google/gemma-3n-e4b-it",
        "messages": messages  
    }

    response = requests.post(invoke_url, headers = headers, json = payload)
    datos = response.json()

    if "choices" in datos:
        texto_ia = datos["choices"][0]["message"]["content"]
        
        messages.append({"role": "assistant", "content": texto_ia})

        print(f'IA: \n {texto_ia}')
        print("-" * 30) 

        with open("cache.json", "w", encoding = "utf-8") as archivo:
            json.dump(messages, archivo, indent = 4, ensure_ascii = False)

    else:
        print("Hubo un error en la petición. Respuesta del servidor:")
        print(datos)
        messages.pop()
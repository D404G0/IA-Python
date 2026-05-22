#---------------------Importar libreria---------------------#
import requests
import os
import json
from requests import Response
from datos import url, token

#---------------------Conexion con nvidia---------------------#
invoke_url = url
stream = False

headers = {
    "Authorization": "Bearer " + token,
}

#---------------------Memoria de IA---------------------#
messages = [
    {
        "role": "system", 
        "content": "Eres un asistente que ayudaras a responder preguntas que te pidan, te limitaras estritramente lo que te pidan sin agregar mas informacion"
    }
]

#---------------------Respuesta de modelo---------------------#
while True:

    #-------------Validacion de input-------------#
    user_input = input("Tu: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ("salir", "exit", "bye", "sayonara"):
        print("Chaoooo")
        break

    #-------------Agregar respuesta en memoria-------------#
    messages.append({"role": "user", "content": user_input})

    #-------------Conexion y respuesta de modelo de ia-------------#
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

    else:
        print("Hubo un error en la petición. Respuesta del servidor:")
        print(datos)
        messages.pop()
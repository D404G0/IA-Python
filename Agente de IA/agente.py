import requests
from requests import Response
from datos import url, token

invoke_url = url
stream = False

headers = {
    "Authorization": "Bearer " + token,
}

while True:

    user_input = input("Tu: ").strip()
    payload = {
        "model": "google/gemma-3n-e4b-it",
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post(invoke_url, headers = headers, json = payload)
    datos = response.json()

    if "choices" in datos:
        texto_ia = datos["choices"][0]["message"]["content"]
        print(f'IA: \n {texto_ia}')
    else:
        print("Hubo un error en la petición. Respuesta del servidor:")
        print(datos)


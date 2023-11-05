import os
from pathlib import Path
import openai
from pythonosc import dispatcher, osc_server, udp_client

# Configura tu clave de API de OpenAI
apikey='apikey.txt'
openai.api_key = f'C:/Users/obeyk/Desktop/UPF/Trimester 1/Advanced Interface Design/Challenges/Challenge #6/{apikey}'


# Función que llama a OpenAI y responde con el resultado
def handle_prompt(unused_addr, prompt_text):
    print(prompt_text)
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", 
                "content": prompt_text}
                ],
      max_tokens=400
    )
    print(response.choices[0]["message"]["content"])
    response_text = response.choices[0]["message"]["content"]
    osc_client.send_message("/response", response_text)

# Configura OSC
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/prompt", handle_prompt)

server = osc_server.ThreadingOSCUDPServer(("localhost", 12345), dispatcher)
print("Servidor OSC iniciado en {}".format(server.server_address))

# Definir osc_client para enviar respuestas
osc_client = udp_client.SimpleUDPClient("127.0.0.1", 12000)  # Assuming Processing is listening on this IP and port

server.serve_forever()



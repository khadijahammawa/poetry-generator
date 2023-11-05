import os
from pathlib import Path
import openai
from pytorch_poem_generator import *
from pythonosc import dispatcher, osc_server, udp_client

# Función que llama a OpenAI y responde con el resultado
def handle_prompt(unused_addr, prompt_text):
    print(prompt_text)

    response_text = generate_rhymed_poem(prompt_text)
    osc_client.send_message("/response", response_text)

# Configura OSC
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/prompt", handle_prompt)

server = osc_server.ThreadingOSCUDPServer(("localhost", 12345), dispatcher)
print("Servidor OSC iniciado en {}".format(server.server_address))

# Definir osc_client para enviar respuestas
osc_client = udp_client.SimpleUDPClient("127.0.0.1", 12000)  # Assuming Processing is listening on this IP and port

server.serve_forever()



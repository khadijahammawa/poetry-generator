from pythonosc import udp_client, dispatcher, osc_server

# Create an OSC server to listen for incoming messages from Processing
server = osc_server.ThreadingOSCUDPServer(('127.0.0.1', 12345), dispatcher)

# Define a function to handle incoming messages
def handle_user_input(unused_addr, user_input):
    # Process the user's input and generate poetry
    generated_poetry = generate_poetry(user_input)
    
    # Send the generated poetry back to the Processing sketch via OSC
    client = udp_client.SimpleUDPClient('127.0.0.1', 54321)
    client.send_message('/response', generated_poetry)

dispatcher.map('/prompt', handle_user_input)

# Start the OSC server
server.serve_forever()

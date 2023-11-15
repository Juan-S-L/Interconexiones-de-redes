import socket

# Configuración del servidor
host = '192.168.56.1'  # Cambia por la dirección IP del servidor
port = 5555  # Puerto de comunicación

# Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen(1)
print(f"Esperando conexión en el puerto {port}...")

# Aceptar la conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")

while True:
    # Recibir mensaje del cliente
    data = client_socket.recv(1024).decode()
    print(f"Cliente: {data}")

    # Enviar mensaje al cliente
    message = input("Escribe tu mensaje: ")
    client_socket.send(message.encode())

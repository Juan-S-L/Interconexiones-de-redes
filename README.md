# Proyecto de Interconexiones de redes
## Introducción
El presente documento ofrece una guía paso a paso destinada a facilitar la configuración y ejecución de un ejercicio práctico en el ámbito de las redes de computadoras. El ejercicio tiene como objetivo principal proporcionar una comprensión práctica de los fundamentos de la comunicación entre dispositivos en una red local, así como introducir conceptos básicos de seguridad en redes, destacando especialmente el funcionamiento conceptual del ataque conocido como Man-in-the-Middle (MitM).

La finalidad de esta guía es proporcionar a los participantes una descripción detallada y clara de los pasos necesarios para llevar a cabo el ejercicio, permitiendo que cualquier persona interesada en el tema pueda reproducirlo y comprender los procesos involucrados en la comunicación entre dispositivos en una red.

Es importante señalar que este ejercicio se debe realizar en un entorno controlado y ético, con el consentimiento explícito de todas las partes involucradas. Se enfatiza la necesidad de practicar la seguridad informática de manera responsable y respetuosa, evitando cualquier acción que viole la privacidad o la integridad de las redes y dispositivos sin la debida autorización.

El documento está estructurado en una serie de pasos secuenciales, desde la preparación del entorno hasta la ejecución del ejercicio, detallando cada fase para garantizar una comprensión completa y una implementación exitosa. Al seguir esta guía, se espera que los participantes adquieran un conocimiento práctico valioso en el ámbito de las redes de computadoras y la seguridad informática.

## Requisitos previos
Antes de proceder con la configuración y ejecución del ejercicio, es fundamental cumplir con ciertos requisitos que asegurarán el correcto desarrollo y comprensión del mismo. A continuación, se detallan los requisitos previos necesarios:

1. **Dos computadoras en una red local:** Es necesario contar con al menos dos computadoras conectadas a la misma red local para establecer la comunicación entre ellas. Estas computadoras deben ser capaces de comunicarse entre sí a través de la red.

2. **Conocimientos básicos de redes:** Se recomienda tener un entendimiento elemental de los conceptos básicos de redes informáticas, incluyendo direcciones IP, protocolos de comunicación, y la estructura de una red local.

3. **Permisos y configuraciones de red:** Asegúrate de contar con los permisos necesarios para realizar configuraciones en las computadoras y ajustar la configuración de la red, incluyendo la capacidad de modificar la configuración del firewall o de los programas de seguridad para permitir la comunicación entre las computadoras en el puerto especificado.

4. **Conocimientos de programación (opcional):** Para fines de desarrollo y ejecución del ejercicio, se pueden requerir conocimientos básicos de programación en el lenguaje seleccionado para la implementación del servidor y cliente, como Python, Java, C/C++, entre otros.

5. **Herramientas necesarias:** Dependiendo de la implementación específica del ejercicio, se pueden necesitar herramientas adicionales como un entorno de desarrollo integrado (IDE), acceso a la línea de comandos, o programas específicos relacionados con la configuración y prueba de redes.

Es esencial asegurarse de cumplir con estos requisitos previos para garantizar una ejecución exitosa del ejercicio y una comprensión completa de los conceptos tratados.

## Paso 1: Preparación del entorno
1. **Conexión de las computadoras en la red local:** Asegúrate de que las dos computadoras que se utilizarán en el ejercicio estén conectadas a la misma red local, ya sea a través de conexión cableada o inalámbrica. Verifica que ambas computadoras puedan comunicarse entre sí en la red.
2. **Verificación de la conectividad:** Para comprobar la conectividad entre las computadoras, utiliza el comando ping en la línea de comandos. Desde cada computadora, intenta hacer ping a la dirección IP de la otra computadora. Por ejemplo:
```cmd
ping dirección_IP_de_la_otra_computadora
```
Esto permitirá verificar que ambas computadoras puedan comunicarse correctamente.

3. **Ajustes de firewall y seguridad:** Verifica y ajusta las configuraciones del firewall o programas de seguridad en ambas computadoras para permitir la comunicación en el puerto que se utilizará para el ejercicio. Asegúrate de que no existan restricciones que puedan bloquear la comunicación entre las computadoras.

4. **Confirmación de permisos:** Asegúrate de tener los permisos necesarios para realizar configuraciones en las computadoras, así como acceso para modificar la configuración de red si es necesario. Si se requieren permisos adicionales, solicita el acceso correspondiente.

## Paso 2: Configuración del servidor
En este paso, se llevará a cabo la configuración del servidor en una de las computadoras, permitiendo la comunicación con el cliente en la red local. Sigue los siguientes pasos para configurar el servidor:


1. **Selección de la computadora para el servidor:** Elige una de las tres computadoras para actuar como servidor. Esta será la computadora a la que el cliente se conectará para enviar mensajes.

2. **Implementación del código del servidor:** Utiliza el lenguaje de programación seleccionado (por ejemplo, Python, Java, etc.) para implementar el código del servidor.
Asegúrate de que el servidor esté configurado para escuchar conexiones entrantes en un puerto específico. Por ejemplo, en Python con sockets TCP, se podría utilizar:
```python
import socket

# Configuración del servidor
host = 'tu_direccion_IP'  # Cambia por la dirección IP del servidor
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
```

3. **Ejecución del servidor:** Ejecuta el código del servidor en la computadora seleccionada para actuar como servidor. Asegúrate de que el servidor esté en ejecución y escuchando conexiones entrantes.

Al completar estos pasos, el servidor estará configurado y listo para aceptar conexiones entrantes desde el cliente en la red local.

## Paso 3: Configuración del cliente
En esta etapa, se configurará el cliente en una de las computadoras para establecer la comunicación con el servidor en la red local. Sigue los siguientes pasos para configurar el cliente:

1. **Elección de la computadora para el cliente:** Selecciona una de las tres computadoras para actuar como cliente. Esta será la computadora que se conectará al servidor para enviar y recibir mensajes.

2. **Implementación del código del cliente:** Utiliza el lenguaje de programación elegido para implementar el código del cliente. Asegúrate de que el cliente esté configurado para conectarse al servidor en la dirección IP y puerto específicos. Por ejemplo, en Python con sockets TCP:
```python
import socket

# Configuración del cliente
host = 'IP_del_servidor'  # Cambia por la dirección IP del servidor
port = 5555  # Puerto de comunicación

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Conexión establecida con el servidor")

while True:
    # Enviar mensaje al servidor
    message = input("Escribe tu mensaje: ")
    client_socket.send(message.encode())

    # Recibir mensaje del servidor
    data = client_socket.recv(1024).decode()
    print(f"Servidor: {data}")
```

3. **Ejecución del cliente:** Ejecuta el código del cliente en la computadora seleccionada para actuar como cliente. Asegúrate de que el cliente esté configurado para conectarse al servidor utilizando la dirección IP y el puerto correctos.

Al seguir estos pasos, el cliente estará configurado y listo para establecer una conexión con el servidor en la red local.

## Paso 4: Simulación del ataque Man-in-the-Middle (MitM)
En esta fase, se simulará un escenario de ataque Man-in-the-Middle (MitM) para ilustrar cómo un atacante podría interceptar y manipular la comunicación entre el servidor y el cliente. Este paso debe llevarse a cabo en un entorno controlado y con el consentimiento explícito de todas las partes involucradas.

**Nota:** Este ejercicio tiene propósitos educativos y éticos. No se debe realizar en un entorno no autorizado ni con intenciones maliciosas.
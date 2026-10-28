from socket import *
from math import *

puertoServidor = 12000

socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.bind(('', puertoServidor))

socketServidor.listen(1)
print('Servidor listo para recibir conexiones...')

while True:
    
    socketCliente, direccionCliente = socketServidor.accept()
    print('Conexion establecida con: ', direccionCliente)
    
    while True:
        try:
            
            mensaje = socketCliente.recv(1024).decode()
            
            if not mensaje:
                break
            
            resultado = eval(mensaje)
            socketCliente.send(str(resultado).encode())        
            
        except:
            socketCliente.send('Error en la expresion'.encode())     
        
    print("El cliente: ", direccionCliente, " se ha desconectado")
    socketCliente.close()

    
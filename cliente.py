import socket

def client(host = 'localhost', port = 12345):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        request = input("Digite a solicitação (Data, Hora ou Data e Hora): ")
        client_socket.send(request.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print("Resposta do servidor:", response)

        client_socket.close()
client()

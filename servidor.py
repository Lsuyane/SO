import socket
import threading
import datetime

def servidor(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    response = ""

    if request == "Data":
        response = datetime.datetime.now().strftime("%Y-%m-%d")
    elif request == "Hora":
        response = datetime.datetime.now().strftime("%H:%M:%S")
    elif request == "Data e Hora":
        response = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        response = "Opção inválida."

    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def main():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor escutando em {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão aceita de {addr[0]}:{addr[1]}")
        
        client_thread = threading.Thread(target=servidor, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()

import socket

# cria um objeto de soquete
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# associa o soquete a um endereço e porta
server_socket.bind(('localhost', 8080))

# exibe mensagem de confirmação
print("Servidor aguardando solicitações...")

# recebe o nome do arquivo solicitado pelo cliente
filename, client_address = server_socket.recvfrom(1024)
filename = filename.decode()

# abre o arquivo no modo de leitura binária
with open(filename, 'rb') as file:

    # lê o conteúdo do arquivo em blocos de 1024 bytes
    data = file.read(1024)

    # enquanto houver dados a serem lidos
    while data:

        # envia os dados ao cliente
        server_socket.sendto(data, client_address)

        # lê o próximo bloco de dados do arquivo
        data = file.read(1024)

# exibe mensagem de conclusão
print("Arquivo enviado para o cliente!")

# fecha o soquete do servidor
server_socket.close()

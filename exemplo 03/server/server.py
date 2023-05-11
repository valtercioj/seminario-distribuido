import socket

# cria um objeto de soquete UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# associa o soquete a um endereço e porta
server_socket.bind(('localhost', 8080))

# exibe mensagem de confirmação
print("Servidor aguardando conexão...")

# recebe o arquivo do cliente
data, client_address = server_socket.recvfrom(1024)

# nome do arquivo que será salvo no servidor
filename = "arquivo_servidor.txt"

# abre o arquivo no modo de escrita binária
with open(filename, 'wb') as file:

    # enquanto houver dados a serem recebidos
    while data:

        # escreve os dados recebidos no arquivo
        file.write(data)

        # recebe o próximo bloco de dados
        data, client_address = server_socket.recvfrom(1024)

# exibe mensagem de conclusão
print("Arquivo recebido com sucesso!")

# fecha o soquete do servidor
server_socket.close()

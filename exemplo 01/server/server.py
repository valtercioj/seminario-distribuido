import socket

# Cria um objeto de socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket a um endereço e porta
server_socket.bind(('localhost', 8080))

# Espera conexões do cliente
server_socket.listen(1)

# Exibe mensagem de confirmação
print("Servidor aguardando conexão...")

# Aceita uma conexão do cliente
connection, address = server_socket.accept()

# Recebe o nome do arquivo do cliente
filename = connection.recv(1024).decode()

# Abre o arquivo no modo de escrita binária
with open(filename, 'wb') as file:

    # Recebe os dados do arquivo em blocos de 1024 bytes
    data = connection.recv(1024)

    # Enquanto houver dados a serem recebidos
    while data:

        # Escreve os dados recebidos no arquivo
        file.write(data)

        # Recebe o próximo bloco de dados
        data = connection.recv(1024)

# Recebe os dados escritos do cliente em blocos de 1024 bytes
data_written = connection.recv(1024)

# Abre o arquivo no modo de escrita
with open("escrito.txt", "w") as file:

    # Enquanto houver dados a serem recebidos
    while data_written:

        # Escreve os dados recebidos no arquivo
        file.write(data_written.decode())

        # Recebe o próximo bloco de dados
        data_written = connection.recv(1024)

# Exibe mensagem de conclusão
print("Arquivo recebido e salvo com sucesso!")

# Fecha a conexão com o cliente
connection.close()

# Fecha o servidor
server_socket.close()

import socket

# Cria um objeto de socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
client_socket.connect(('localhost', 8080))

# Exibe mensagem de confirmação de conexão
print("Cliente conectado ao servidor!")

# Nome do arquivo que será enviado
filename = str(input("Digite o nome do arquivo a ser enviado: "))

# Envio do nome do arquivo ao servidor
client_socket.send(filename.encode())

# Abre o arquivo no modo de leitura binária
with open(filename, 'rb') as file:

    # Lê o conteúdo do arquivo em blocos de 1024 bytes
    data = file.read(1024)

    while data:

        # Envio dos dados ao servidor
        client_socket.send(data)

        # Lê o próximo bloco de dados do arquivo
        data = file.read(1024)

# Exibe mensagem de conclusão
print("Arquivo enviado com sucesso!")

# Fecha a conexão com o servidor
client_socket.close()

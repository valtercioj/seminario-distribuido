import socket
import os
# cria um objeto de soquete UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# exibe mensagem de confirmação de conexão
print("Cliente conectado ao servidor!")

# nome do arquivo que será enviado
filename = str(input("Digite o nome do arquivo a ser enviado: "))
if not os.path.exists(filename):
    print("\nArquivo não encontrado!")
    exit()

# abre o arquivo no modo de leitura binária
with open(filename, 'rb') as file:

    # lê o conteúdo do arquivo em blocos de 1024 bytes
    data = file.read(1024)

    # enquanto houver dados a serem lidos
    while data:

        # envia os dados ao servidor
        client_socket.sendto(data, ('localhost', 8080))

        # lê o próximo bloco de dados do arquivo
        data = file.read(1024)

# exibe mensagem de conclusão
print("Arquivo enviado com sucesso!")

# fecha o soquete do cliente
client_socket.close()

import socket

# cria um objeto de socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# define o endereço e porta do servidor
server_address = ('localhost', 8080)

# nome do arquivo que será solicitado
filename = str(input("Digite o nome do arquivo a ser enviado: "))

# verifica se o arquivo existe 
if not os.path.exists(filename):
    print("\nArquivo não encontrado!")
    exit()


# envia o nome do arquivo ao servidor
client_socket.sendto(filename.encode(), server_address)

# recebe o arquivo do servidor em blocos de 1024 bytes
data, server = client_socket.recvfrom(1024)

# abre o arquivo no modo de escrita binária
with open(filename, 'wb') as file:
    
    # escreve os dados recebidos no arquivo
    file.write(data)

# exibe mensagem de conclusão
print(f"Arquivo '{filename}' recebido com sucesso!")

# fecha a conexão com o servidor
client_socket.close()

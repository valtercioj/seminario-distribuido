import socket

# Cria um objeto socket com IPv4 e protocolo TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 



# Associa o servidor ao endereço IP e porta específicos
server.bind(('localhost', 8080)) 

# Coloca o servidor em modo escuta para conexões
server.listen(1) 

print("O servidor funcionando na porta 8080...")

# Aceita uma conexão de entrada e retorna uma nova tupla de objeto do socket
connection, address = server.accept() 

# Recebe o nome do arquivo a ser enviado pelo cliente
nameFile = connection.recv(1024).decode() 

with open(nameFile, 'rb') as file: # Abre o arquivo em modo de leitura binário

    for data in file: # Lê o arquivo em blocos de tamanho definido

        # Envia cada bloco do arquivo para o cliente
        connection.sendall(data) 

print("Arquivo enviado com sucesso!")

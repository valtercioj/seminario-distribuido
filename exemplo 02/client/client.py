import socket

# Cria um objeto de socket do tipo TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor que está em execução localmente na porta 8080
client.connect(('localhost', 8080))

# Imprime uma mensagem indicando que a conexão foi estabelecida com sucesso
print("O cliente está conectado ao servidor!")

# Solicita que o usuário informe o nome do arquivo que será enviado
filename = str(input("Digite o nome do arquivo a ser enviado: "))

# Envia o nome do arquivo codificado para o servidor
client.send(filename.encode())

# Abre o arquivo em modo de escrita binária
with open(filename, 'wb') as file:
    while 1:
        # Recebe os dados enviados pelo servidor
        data = client.recv(1000000)
        
        # Se não houver mais dados, encerra o loop
        if not data:
            break
        
        # Escreve os dados no arquivo
        file.write(data)

# Imprime uma mensagem indicando que o arquivo foi enviado com sucesso
print("Arquivo enviado com sucesso!")

# Encerra a conexão com o servidor
client.close()

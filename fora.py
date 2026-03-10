import os

cwd = os.getcwd()

lista_pasta = [i for i in os.listdir(cwd) if os.path.isdir(i)]

for pasta in lista_pasta:
    caminho = os.path.join(cwd, pasta)

    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        inicio = os.path.join(caminho, arquivo)
        destino = os.path.join(cwd, arquivo)

        os.replace(inicio, destino)
    os.rmdir(caminho)
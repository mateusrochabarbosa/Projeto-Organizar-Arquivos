import os

cwd = os.getcwd()

lista_total = os.listdir(cwd)

lista_arquivos = [i for i in lista_total if os.path.isfile(i) and '.py' not in i]

tipos = list(set([i.split('.')[1] for i in lista_arquivos]))

for tipo_arquivo in tipos:
    os.mkdir(tipo_arquivo)

for arquivo in lista_arquivos:
        inicio = os.path.join(cwd, arquivo)
        destino = os.path.join(cwd, arquivo.split('.')[-1], arquivo)

        os.replace(inicio, destino)
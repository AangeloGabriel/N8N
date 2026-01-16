import os 

def OrdenaLista(CaminhoArquivos):

    listaNomes = []
    for arquivos in CaminhoArquivos:    
        nome = os.path.basename(arquivos)
        if nome not in listaNomes:
            listaNomes.append(nome)

    listaorganizada = {}


    for datas in listaNomes:
        if datas not in listaorganizada:
            listaorganizada[datas] = []

        for caminho in CaminhoArquivos:
            if os.path.basename(caminho) == datas:
                listaorganizada[datas].append(caminho)

    return listaorganizada
import os 

def LeitorPastas():
    PATH = 'C:/n8n-data/arquivos/amazon_scraping'
    resultado = []

    for arquivo in os.listdir(PATH):
        if arquivo.startswith ("~$"):
            continue
        else:
            Caminhos = os.path.join(PATH, arquivo)
            resultado.append(Caminhos)

    arquivocaminho = []
    for caminhopastas in resultado:
        Lista_arquivos_totais = os.listdir(caminhopastas)
        for files in Lista_arquivos_totais:
            if files != "Offers":
                a = os.path.join(caminhopastas, files)
                arquivocaminho.append(a) 
    
    ListaFinal = []
    for i in arquivocaminho:
        a = i.replace("\\", "/")
        ListaFinal.append(a)       

    return ListaFinal
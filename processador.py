from organizador import OrdenaLista
import pandas as pd
import os

def Processa(ListaOrdenada):

    Tabela = pd.DataFrame()

    for data, lista_caminhos in ListaOrdenada.items():
            for caminhos in lista_caminhos:
                if data == os.path.basename(caminhos):
                    excel = pd.read_excel(caminhos)
                    excel.insert(0, "DataAnuncio", value=(os.path.splitext(data)[0]).replace("_", "/"), allow_duplicates=True)
                    Tabela = pd.concat([Tabela, excel], ignore_index=True)
                else:
                     continue
    return Tabela


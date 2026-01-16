import pandas as pd
import os

def Salva(Arquivo):
    
    PATH_SAVE = r"S:\S&OP e Produtos\Compartilhado\S&OP\N8N\Automacoes\amazon_scraping\Consolidado"
    FORMAT = "Amazon_Geral.xlsx"

    arquivo_final = os.path.join(PATH_SAVE, FORMAT)
    
    Tabela = pd.DataFrame(Arquivo)
    
    Tabela.to_excel(excel_writer=arquivo_final, sheet_name="Geral", index=False)
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

PATH_SAVE = os.getenv("PATH_SAVE")
FORMAT = "Amazon_Geral.xlsx"

def Salva(Arquivo):

    arquivo_final = os.path.join(PATH_SAVE, FORMAT)
    
    Tabela = pd.DataFrame(Arquivo)
    
    Tabela.to_excel(excel_writer=arquivo_final, sheet_name="Geral", index=False)
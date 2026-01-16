from leitor import LeitorPastas
from organizador import OrdenaLista
from processador import Processa
from salva import Salva

def main():
    Pastas = LeitorPastas()

    Organizado = OrdenaLista(Pastas)

    Processados = Processa(Organizado)
    
    Salva(Processados)
 
if __name__  == "__main__":
    main()
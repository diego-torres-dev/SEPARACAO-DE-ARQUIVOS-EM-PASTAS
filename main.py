# Importa o método Path
from pathlib import Path

# Importa a biblioteca shutil
import shutil

# Lista de estados
estados = ["AM", "GO", "MG", "RJ", "SP"]

# Lista de anos
anos = [2018, 2019, 2020]

# Lista de trimestres
trimestres = ["01", "02", "03", "04"]

# Caminho relativo da pasta com as bases de dados
pasta_arquivos = Path("Arquivos_Lojas")


def criar_pasta(nome_pasta):
    """Cria uma pasta com o nome especificado caso ela não exista.

    Parâmetro:
        nome_pasta (str): caminho relativo da pasta

    Retorna:
        Cria uma pasta no caminho relativo especificado caso ela não exista
    """

    if not Path(nome_pasta).exists():
        Path(nome_pasta).mkdir()


# Cria a pasta principal
criar_pasta("Estados")

# Cria as subpastas da pasta Estado
for estado in estados:
    criar_pasta(f"Estados/{estado}")
    for ano in anos:
        criar_pasta(f"Estados/{estado}/{ano}")
        for trimestre in trimestres:
            criar_pasta(f"Estados/{estado}/{ano}/{trimestre}")

# Nome da pasta de destino
pasta_destino = None

# Cria uma lista com os nomes dos arquivos da pasta atual
arquivos = pasta_arquivos.iterdir()

# Percorre a lista com os nomes dos arquivos
for arquivo in arquivos:
    # Obtém o nome do arquivo
    nome_arquivo = arquivo.name

    # Verifica se o arquivo é um CSV
    if nome_arquivo.endswith(".csv"):
        # Obtém o nome do estado a que o arquivo se refere
        estado = nome_arquivo[-6:-4]

        # Obtém o ano a que o arquivo se refere
        ano = nome_arquivo[0:4]

        # Obtém o trimestre a que o arquivo se refere
        trimestre = nome_arquivo[4:6]

        # Especifica a pasta de origem do arquivo
        pasta_origem = f"Arquivos_Lojas/{nome_arquivo}"

        # Especifica a pasta de destino do arquivo
        pasta_destino = f"Estados/{estado}/{ano}/{trimestre}"

        # Move o arquivo para a pasta especificada
        shutil.move(Path(pasta_origem), Path(pasta_destino))

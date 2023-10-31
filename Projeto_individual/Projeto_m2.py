# Importe a biblioteca pandas para lidar com dados em formato CSV
import pandas as pd

# Esta função permite ao usuário inserir o nome do arquivo CSV que deseja importar
def importar_csv():
    while True:
        arquivo = input("Digite o nome do arquivo CSV que deseja importar (sem a extensão .csv): ")
        try:
            candidatos = pd.read_csv(f'{arquivo}.csv')  # Tenta ler o arquivo CSV
            return candidatos
        except FileNotFoundError:
            print(f"Erro: O arquivo '{arquivo}.csv' não foi encontrado. Verifique o nome e a localização do arquivo.")
        except Exception as e:
            print(f"Erro ao importar o arquivo CSV: {e}")

# Esta função permite ao usuário inserir as notas mínimas para as áreas E, T, P e S
def notas_min():
    while True:
        try:
            nota_min_e = float(input('Digite a nota mínima para E: '))
            nota_min_t = float(input('Digite a nota mínima para T: '))
            nota_min_p = float(input('Digite a nota mínima para P: '))
            nota_min_s = float(input('Digite a nota mínima para S: '))
            return nota_min_e, nota_min_t, nota_min_p, nota_min_s
        except ValueError:
            print("Erro: Insira um valor numérico válido para as notas mínimas.")

# Esta função filtra os candidatos com base nas notas mínimas especificadas
def filtrar_candidatos(candidatos, nota_min_e, nota_min_t, nota_min_p, nota_min_s):
    candidatos_filtrados = candidatos[
        (candidatos['e'] >= nota_min_e) &
        (candidatos['t'] >= nota_min_t) &
        (candidatos['p'] >= nota_min_p) &
        (candidatos['s'] >= nota_min_s)
    ]
    return candidatos_filtrados

if __name__ == "__main__":
    candidatos = importar_csv()  # Importa o arquivo CSV especificado pelo usuário
    nota_min_e, nota_min_t, nota_min_p, nota_min_s = notas_min()  # Obtém as notas mínimas especificadas pelo usuário
    candidatos_filtrados = filtrar_candidatos(candidatos, nota_min_e, nota_min_t, nota_min_p, nota_min_s)  # Filtra os candidatos

    # Verifica se existem candidatos que atendem aos critérios e os salva em um novo arquivo CSV ou informa que nenhum candidato foi encontrado
    if not candidatos_filtrados.empty:
        arquivo_saida = input("Digite o nome do arquivo de saída para os candidatos filtrados (sem a extensão .csv): ")
        candidatos_filtrados.to_csv(f'{arquivo_saida}.csv', sep=';', index=False)
        print(f"Candidatos filtrados salvos no arquivo '{arquivo_saida}.csv'")
    else:
        print("Nenhum candidato atende aos critérios informados.")

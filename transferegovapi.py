import requests
import pandas as pd

def baixarDadosTed(offset=0, limite=1000):
    url = "https://api.transferegov.gestao.gov.br/ted/plano_acao"
    df = pd.DataFrame()

    while True:
        try:
            print(f"Solicitando dados com offset={offset}...")
            resposta = requests.get(f"{url}?offset={offset}")

            if resposta.status_code != 200:
                print(f"Erro ao acessar a API: Status {resposta.status_code}")
                break

            dados_json = resposta.json()

            if not dados_json:
                print("Dados baixados com sucesso.")
                break

            df = pd.concat([df, pd.DataFrame(dados_json)], ignore_index=True)

            if df.empty:
                print("Nenhum dado encontrado no DataFrame. Encerrando.")
                break

            offset += limite

            df.to_csv(f"plano_acao_{offset}.csv", index=False, sep=';')

        except Exception as erro:
            print(f"Ocorreu um erro durante a execução: {erro}")
            break

def main(offset=0, limite=1000):
    print("Iniciando o processo de extração dos dados de plano de ação...")
    baixarDadosTed(offset, limite)
    print("Processo finalizado.")

if __name__ == "__main__":
    import sys
    offset = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    limite = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    main(offset, limite)

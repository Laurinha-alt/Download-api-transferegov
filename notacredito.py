import requests
import pandas as pd

def baixar_varios_json():
    url_base = "https://api.transferegov.gestao.gov.br/ted/nota_credito"
    offset = 0
    limite = 1000
    contador_arquivo = 1

    while True:
        try:
            print(f"Solicitando dados com offset={offset}...")
            resposta = requests.get(f"{url_base}?offset={offset}")

            if resposta.status_code != 200:
                print(f"Erro ao acessar a API: Status {resposta.status_code}")
                break

            dados_json = resposta.json()

            if not dados_json:
                print("Todos os dados foram baixados com sucesso!")
                break

            df = pd.DataFrame(dados_json)

            if df.empty:
                print("Nenhum dado retornado no DataFrame. Encerrando.")
                break

            nome_arquivo = f"notacredito{contador_arquivo}.json"
            df.to_json(nome_arquivo, orient="records", force_ascii=False, indent=4)
            print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

            offset += limite
            contador_arquivo += 1

        except Exception as erro:
            print(f"Ocorreu um erro durante a execução: {erro}")
            break

def main():
    print("Iniciando o processo de extração dos dados do plano de ação...")
    baixar_varios_json()
    print("Processo finalizado.")

if __name__ == "__main__":
    main()
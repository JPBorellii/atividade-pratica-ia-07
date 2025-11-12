# 3_ler_csv.py
# Lê um arquivo CSV com colunas Nome, Idade, Cidade e exibe os dados na tela.

import csv

def ler_csv(caminho_arquivo):
    registros = []
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # tenta converter idade para int quando possível
                idade = row.get('Idade', '').strip()
                try:
                    idade = int(idade) if idade != '' else None
                except ValueError:
                    # mantém como string se não for inteiro
                    pass
                registros.append({
                    'Nome': row.get('Nome', '').strip(),
                    'Idade': idade,
                    'Cidade': row.get('Cidade', '').strip()
                })
    except FileNotFoundError:
        raise RuntimeError("Arquivo não encontrado: " + caminho_arquivo)
    except Exception as e:
        raise RuntimeError("Erro ao ler CSV: " + str(e))
    return registros

if __name__ == "__main__":
    caminho = input("Caminho do arquivo CSV a ler: ")
    try:
        dados = ler_csv(caminho)
        if not dados:
            print("Nenhum registro encontrado no arquivo.")
        else:
            print("Registros lidos:")
            for i, rec in enumerate(dados, start=1):
                print(f"{i}. Nome: {rec['Nome']}, Idade: {rec['Idade']}, Cidade: {rec['Cidade']}")
    except Exception as e:
        print("Erro:", e)
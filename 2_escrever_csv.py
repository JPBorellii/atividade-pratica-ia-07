# 2_escrever_csv.py
# Escreve informações pessoais em um arquivo CSV (Nome, Idade, Cidade).

import csv

def escrever_csv(caminho_arquivo, registros):
    """Registros: lista de dicionários com chaves 'Nome','Idade','Cidade'."""
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['Nome', 'Idade', 'Cidade']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rec in registros:
            writer.writerow(rec)

if __name__ == "__main__":
    caminho = input("Nome do arquivo CSV a criar (ex: pessoas.csv): ")
    print("Digite os dados das pessoas. Para encerrar, deixe o nome vazio e pressione Enter.")
    lista = []
    while True:
        nome = input("Nome: ").strip()
        if nome == "":
            break
        idade_text = input("Idade: ").strip()
        cidade = input("Cidade: ").strip()
        # valida idade simples
        try:
            idade = int(idade_text)
        except ValueError:
            print("Idade inválida, tente novamente.")
            continue
        lista.append({'Nome': nome, 'Idade': idade, 'Cidade': cidade})
    if lista:
        try:
            escrever_csv(caminho, lista)
            print("Arquivo salvo em:", caminho)
        except Exception as e:
            print("Erro ao salvar arquivo:", e)
    else:
        print("Nenhum registro para salvar.")
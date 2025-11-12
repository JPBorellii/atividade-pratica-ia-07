# 4_json_read_write.py
# Lê um arquivo JSON com informações de uma pessoa e permite gravar/atualizar outro JSON.

import json

def ler_json_pessoa(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dado = json.load(f)
    except FileNotFoundError:
        raise RuntimeError("Arquivo JSON não encontrado: " + caminho_arquivo)
    except json.JSONDecodeError:
        raise RuntimeError("Arquivo JSON inválido ou mal formatado.")
    # espera campos básicos; não é estrito
    nome = dado.get('nome')
    idade = dado.get('idade')
    cidade = dado.get('cidade')
    return {'nome': nome, 'idade': idade, 'cidade': cidade}

def escrever_json_pessoa(caminho_arquivo, pessoa_dict):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(pessoa_dict, f, ensure_ascii=False, indent=4)
    except Exception as e:
        raise RuntimeError("Erro ao escrever JSON: " + str(e))

if __name__ == "__main__":
    caminho = input("Caminho do arquivo JSON a ler (ex: pessoa.json): ")
    try:
        pessoa = ler_json_pessoa(caminho)
        print("Dados encontrados:")
        print("Nome :", pessoa.get('nome'))
        print("Idade:", pessoa.get('idade'))
        print("Cidade:", pessoa.get('cidade'))
    except Exception as e:
        print("Erro ao ler JSON:", e)
        pessoa = None

    if pessoa is None:
        # permite criar um novo
        resposta = input("Deseja criar um novo registro? (s/n): ").strip().lower()
        if resposta != 's':
            print("Encerrando sem gravar.")
            exit(0)
        nome = input("Nome: ").strip()
        idade_text = input("Idade: ").strip()
        cidade = input("Cidade: ").strip()
        try:
            idade = int(idade_text)
        except ValueError:
            idade = idade_text  # mantém texto se não for inteiro
        pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}

    # permite atualizar antes de salvar
    print("Se quiser alterar algum campo, digite o novo valor; Enter para manter.")
    novo_nome = input(f"Nome [{pessoa.get('nome')}]: ").strip()
    novo_idade = input(f"Idade [{pessoa.get('idade')}]: ").strip()
    nova_cidade = input(f"Cidade [{pessoa.get('cidade')}]: ").strip()
    if novo_nome:
        pessoa['nome'] = novo_nome
    if novo_idade:
        try:
            pessoa['idade'] = int(novo_idade)
        except ValueError:
            pessoa['idade'] = novo_idade
    if nova_cidade:
        pessoa['cidade'] = nova_cidade

    destino = input("Nome do arquivo JSON para salvar (ex: pessoa_out.json): ").strip()
    if not destino:
        destino = "pessoa_out.json"
    try:
        escrever_json_pessoa(destino, pessoa)
        print("Arquivo salvo em:", destino)
    except Exception as e:
        print("Erro ao salvar JSON:", e)
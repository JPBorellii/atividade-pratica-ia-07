# 1_estatisticas_log.py
# Lê um arquivo de log e calcula média e desvio padrão dos tempos encontrados.
# Aceita linhas com apenas um número (tempo em segundos) ou linhas de texto que contenham um número.

import math
import re

def extrair_tempos_de_linhas(linhas):
    """Extrai todos os números de ponto flutuante das linhas e retorna lista de floats."""
    tempos = []
    # regex para capturar floats com ou sem notação científica
    num_re = re.compile(r'[-+]?\d*\.\d+|\d+')
    for linha in linhas:
        for match in num_re.findall(linha):
            try:
                tempos.append(float(match))
            except ValueError:
                continue
    return tempos

def calcular_media(serie):
    return sum(serie) / len(serie) if serie else 0.0

def calcular_desvio_padrao(serie):
    n = len(serie)
    if n <= 1:
        return 0.0
    media = calcular_media(serie)
    variancia = sum((x - media) ** 2 for x in serie) / (n - 1)  # amostral
    return math.sqrt(variancia)

def processar_arquivo_log(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
    except FileNotFoundError:
        raise RuntimeError("Arquivo não encontrado: " + caminho_arquivo)
    except Exception as e:
        raise RuntimeError("Erro ao abrir o arquivo: " + str(e))

    tempos = extrair_tempos_de_linhas(linhas)
    if not tempos:
        raise RuntimeError("Nenhum tempo numérico encontrado no arquivo.")

    media = calcular_media(tempos)
    dp = calcular_desvio_padrao(tempos)
    return {
        "count": len(tempos),
        "media": media,
        "desvio_padrao": dp
    }

if __name__ == "__main__":
    caminho = input("Caminho do arquivo de log: ")
    try:
        res = processar_arquivo_log(caminho)
        print("Quantidade de tempos encontrados:", res["count"])
        print("Média dos tempos: {:.4f}".format(res["media"]))
        print("Desvio padrão (amostral): {:.4f}".format(res["desvio_padrao"]))
    except Exception as e:
        print("Erro:", e)
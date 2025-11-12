# Atividade Prática 07  
**Nome:** João Paulo Silva Borelli  
**Turma:** BRSAO-199  
**Data:** 12/11/2025

## Descrição  

Soluções em Python para manipulação de arquivos: logs, CSV e JSON.  
Cada script tem comentários curtos e tratamento básico de erros.

## Arquivos  

1_estatisticas_log.py - Lê arquivo de log, extrai números de tempo e calcula média e desvio padrão (amostral).  
2_escrever_csv.py - Interativo: recebe registros (Nome, Idade, Cidade) e grava em CSV.  
3_ler_csv.py - Lê CSV com colunas Nome, Idade, Cidade e exibe os registros na tela.  
4_json_read_write.py - Lê um JSON de pessoa (nome, idade, cidade), permite editar/criar e grava em JSON.

## Como usar  

- Execute cada script independentemente com `python nome_do_arquivo.py`.  
- Os scripts usam entrada via terminal (`input`) para facilitar testes manuais.  
- Para o script de estatísticas, passe o caminho de um arquivo de log que contenha números (um por linha ou em linhas de texto).

## Observações técnicas  

- O script de estatísticas usa regex para extrair números das linhas (floats e inteiros).  
- O CSV é escrito/ lido com `csv.DictWriter` e `csv.DictReader` usando `utf-8`.  
- O JSON é lido/escrito com `json` padrão e salvo com `indent=4` para legibilidade.

## O que aprendi  

- Ler e escrever arquivos texto, CSV e JSON em Python.  
- Extrair dados numéricos de texto bruto e calcular estatísticas básicas.  
- Tornar scripts tolerantes a erros de entrada e arquivos inexistentes.
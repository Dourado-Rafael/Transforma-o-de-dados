# Projeto de Extração e Processamento de Tabelas em PDF

Este projeto realiza a extração de tabelas de um arquivo PDF, processa os dados e os salva em formato CSV. Em seguida, o CSV gerado é compactado em um arquivo ZIP para fácil distribuição.

## Descrição

O código extrai todas as tabelas de um PDF (usando a biblioteca `tabula`), faz algumas substituições de texto nas colunas do DataFrame e salva os dados processados em um arquivo CSV. O CSV gerado é, então, compactado em um arquivo ZIP para facilitar o compartilhamento.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **Tabula-py**: Biblioteca para extrair tabelas de PDFs
- **Pandas**: Manipulação e análise de dados
- **Zipfile**: Compactação de arquivos em formato ZIP

## Requisitos

- Python 3.x
- Bibliotecas Python:
    - `tabula-py`
    - `pandas`
    - `zipfile` (inclusa no Python)
    - `os` (inclusa no Python)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Instale as dependências necessárias:

    ```bash
    pip install tabula-py pandas
    ```

3. Certifique-se de ter o Java instalado, pois o Tabula utiliza o Java para processar os PDFs.

## Uso

1. Coloque o arquivo PDF chamado `Anexo_1.pdf` na raiz do projeto ou altere o caminho no código.
2. Execute o script Python:

    ```bash
    python extrair_e_processar_tabelas.py
    ```

3. O script fará o seguinte:
   - Extrair todas as tabelas do PDF `Anexo_1.pdf`.
   - Concatenar todas as tabelas extraídas em um único DataFrame.
   - Renomear algumas colunas específicas para facilitar a leitura.
   - Salvar os dados processados em um arquivo CSV chamado `rol_procedimentos.csv`.
   - Compactar o arquivo CSV gerado em um arquivo ZIP chamado `Teste_Rafael.zip`.


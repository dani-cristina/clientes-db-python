# clientes-db-python

Script em Python para criação e gerenciamento de uma tabela de clientes utilizando banco de dados SQLite.

## Descrição

Este projeto contém um script que cria uma tabela chamada `cliente` em um banco de dados SQLite chamado `meu_banco.db`.  
A tabela armazena informações de clientes, como ID, nome, e-mail e data de nascimento.

## Como usar

1. Certifique-se de ter o Python instalado.
2. Execute o arquivo `banco_dados.py`:
   ```bash
   python banco_dados.py
   ```
3. O banco de dados `meu_banco.db` será criado na mesma pasta, contendo a tabela `cliente`.

## Estrutura da tabela

- **id**: inteiro, chave primária
- **nome**: texto
- **email**: texto
- **data_nascimento**: data

## Requisitos

- Python 3.x

## Autor

Daniela

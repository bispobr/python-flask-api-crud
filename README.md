# python-flask-api-crud

Este repositório contém um projeto CRUD simples construído usando flask. O objetivo deste repositório é praticar e construir todos os métodos CRUD usando python.

## Indice

- [Instalação](Instalação)
- [configuração](#configuração)
- [API Endpoints](#api-endpoints)
- [Banco-de-Dados](#Banco-de-Dados)

## Instalação

1. Clone o repositório:

```bash
git https://github.com/bispobr/python-flask-api-crud.git
```
2. instale o flask atraves do pip python
2. execute o arquivo app.py

## Como usar

1. A API está acessivem atraves do Link http://localhost:5000

## API Endpoints
A API contem os seguintes endpoints :

```markdown
GET /livro - Retorna uma Lista com todos os livros cadastrados.

POST /livro/id - Registra um novo livro.

PUT /livro/id - Altera Um informações de um livro.

DELETE /livro/id - Exclui Um livro.
```
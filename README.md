# API CRUD com Flask

API REST desenvolvida em Python utilizando Flask para praticar a implementação das operações fundamentais de um CRUD.

O projeto utiliza o conceito de gerenciamento de livros como domínio da aplicação.

## Funcionalidades

- Cadastro de livros
- Listagem de livros
- Atualização de livros
- Exclusão de livros
- API HTTP baseada em operações CRUD

## Tecnologias

- Python
- Flask

## Requisitos

- Python 3+
- Flask

## Instalação

Clone o repositório:

```bash
git clone https://github.com/bispobr/python-flask-api-crud.git
cd python-flask-api-crud
```

Instale o Flask:

```bash
pip install flask
```

## Executando o projeto

Execute o arquivo principal da aplicação:

```bash
python app.py
```

Por padrão, a API fica disponível em:

```text
http://localhost:5000
```

## API Endpoints

### Listar livros

```http
GET /livro
```

Retorna a lista de livros cadastrados.

### Criar livro

```http
POST /livro
```

Cadastra um novo livro.

> O README original indicava `POST /livro/id`, porém o identificador não é normalmente utilizado para a criação de um novo recurso. A rota documentada acima deve ser confirmada na implementação atual caso tenha sido definida de forma diferente.

### Atualizar livro

```http
PUT /livro/{id}
```

Atualiza as informações de um livro existente.

### Excluir livro

```http
DELETE /livro/{id}
```

Exclui um livro pelo identificador.

## Fluxo simplificado

```text
Cliente
   │
   ▼
API Flask
   │
   ▼
Rotas HTTP
   │
   ├── GET
   ├── POST
   ├── PUT
   └── DELETE
   │
   ▼
Gerenciamento de livros
```

## Estrutura

O ponto de entrada indicado na documentação do projeto é o arquivo `app.py`.

Os demais arquivos e detalhes da implementação devem ser consultados diretamente no código do projeto.

## Status

Projeto de estudos desenvolvido para praticar a construção de APIs CRUD utilizando Python e Flask.

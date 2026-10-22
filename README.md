# HelpDesk API

API REST para gerenciamento de chamados de suporte, desenvolvida em Python como parte de uma trilha prática de estudos em desenvolvimento backend.

## Tecnologias

- Python
- FastAPI
- Pydantic
- PostgreSQL
- Psycopg 3
- Uvicorn

## Funcionalidades

O projeto possui operações de persistência para:

- Criar chamados
- Listar chamados
- Buscar chamados por ID
- Atualizar chamados
- Excluir chamados

## Estrutura do projeto

- `main.py`: aplicação FastAPI
- `repositorios.py`: operações de acesso aos dados
- `banco.py`: conexão com PostgreSQL
- `chamados.sql`: estrutura e dados de exemplo do banco
- `chamados.py`: arquivo utilizado durante os estudos

## Banco de dados

O projeto utiliza o banco PostgreSQL `helpdesk`.

O arquivo `chamados.sql` contém a criação da tabela `chamados`, com os campos:

- `id`: identificador do chamado
- `titulo`: título do chamado
- `status`: situação do chamado
- `criado_em`: data e hora de criação

Os status permitidos são `aberto`, `em andamento` e `fechado`.

Para preparar um banco novo, após configurar o PostgreSQL:

```bash
createdb helpdesk
psql -d helpdesk -f chamados.sql
```

Esses comandos são destinados à configuração inicial. Não execute novamente o script em um banco que já tenha a tabela criada.

## Como executar

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/pstabelino/helpdesk-api.git
cd helpdesk-api
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Com o PostgreSQL configurado, inicie a API:

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

## Objetivo educacional

Praticar a construção de APIs REST, operações CRUD, integração com PostgreSQL e organização de código em camadas.

## Autor

Paulo Henrique

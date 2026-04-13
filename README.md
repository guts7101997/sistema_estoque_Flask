#  Sistema de Estoque com Flask

Sistema CRUD de estoque desenvolvido em Python com Flask e MySQL.

## Tecnologias
- Python + Flask
- MySQL
- HTML + CSS

## Funcionalidades
- Cadastrar, listar, atualizar e deletar produtos
- Alerta automático de estoque baixo (≤ 5 unidades)

## Como rodar

1. Instale as dependências: `pip install flask mysql-connector-python`
2. Crie o banco no MySQL:

```sql
CREATE DATABASE sistema_estoque;

USE sistema_estoque;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(100),
    quantidade INT,
    preco DECIMAL(10,2)
);
```

3. No `app.py`, substitua `SUA_SENHA_AQUI` pela sua senha do MySQL
4. Rode: `python app.py`
5. Acesse: `http://127.0.0.1:5000`

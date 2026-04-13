from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "chave_secreta_123"

#Conexão 
def get_conexao():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='mello0408',
        database='sistema_estoque'
    )


# Rotas 

@app.route('/')
def index():
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()

    itens_baixos = [p for p in produtos if int(p[3]) <= 5]

    return render_template('index.html', produtos=produtos, itens_baixos=itens_baixos)


@app.route('/inserir', methods=['POST'])
def inserir():
    nome       = request.form['nome']
    categoria  = request.form['categoria']
    quantidade = request.form['quantidade']
    preco      = request.form['preco']

    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, categoria, quantidade, preco) VALUES (%s, %s, %s, %s)",
            (nome, categoria, quantidade, preco)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash("Produto inserido com sucesso!", "sucesso")
    except Exception as e:
        flash(f"Erro ao inserir: {e}", "erro")

    return redirect(url_for('index'))


@app.route('/atualizar', methods=['POST'])
def atualizar():
    nome       = request.form['nome']
    categoria  = request.form['categoria']
    quantidade = request.form['quantidade']
    preco      = request.form['preco']

    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produtos SET categoria=%s, quantidade=%s, preco=%s WHERE nome=%s",
            (categoria, quantidade, preco, nome)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash(f"Produto '{nome}' atualizado!", "sucesso")
    except Exception as e:
        flash(f"Erro ao atualizar: {e}", "erro")

    return redirect(url_for('index'))


@app.route('/deletar', methods=['POST'])
def deletar():
    nome = request.form['nome']

    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE nome=%s", (nome,))
        conn.commit()
        cursor.close()
        conn.close()
        flash(f"Produto '{nome}' deletado!", "sucesso")
    except Exception as e:
        flash(f"Erro ao deletar: {e}", "erro")

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

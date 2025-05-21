from flask import Flask, request # importamos a biblioteca flask e suas ferramentas
import sqlite3 as sql # importamos o sqlite (banco de dados) e definimos o nome dele como sql para facilitar
app = Flask(__name__)

@app.route('/', methods=['GET','POST']) # rota do login
def index(): 
    retorno = request.json
    con = sql.connect('banco.sqlite3')
    cur = con.cursor()
    comando = f"""SELECT NOME, SENHA FROM usuarios WHERE NOME = '{retorno.get('nome')}' AND SENHA = '{retorno.get('senha')}' """
    cur.execute(comando)
    visualizar = cur.fetchone()
    if visualizar:
        return "Login feito."
    else:
        return "Login não feito."

@app.route('/cadastro', methods=['POST'])
def cadastro():
    retorno = request.json
    con = sql.connect('banco.sqlite3')
    cur = con.cursor()
    comando = f"""INSERT INTO usuarios (NOME,SENHA,EMAIL,TELEFONE) VALUES ('{retorno.get('nome')}','{retorno.get('senha')}','{retorno.get('email')}','{retorno.get('telefone')}')"""
    cur.execute(comando)
    con.commit()
    con.close()
    return "Cadastro feito."

@app.route('/ver', methods=['GET'])
def ver():
    con = sql.connect('banco.sqlite3')
    cur = con.cursor()
    comando = f"""SELECT * FROM usuarios"""
    cur.execute(comando)
    visualizar = cur.fetchall()
    con.close()
    return visualizar

if __name__ == '__main__':
    app.run(debug=True)
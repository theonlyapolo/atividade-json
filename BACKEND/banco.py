import sqlite3 as sql

con = sql.connect('banco.sqlite3')
cur = con.cursor()
cur.execute(f"DROP TABLE IF EXISTS usuarios")
comando = f""" CREATE TABLE usuarios (
        NOME VARCHAR(255) NOT NULL,
        SENHA VARCHAR(255) NOT NULL,
        EMAIL TEXT NOT NULL,
        TELEFONE CHAR(11) NOT NULL
        );"""
cur.execute(comando)
con.close()
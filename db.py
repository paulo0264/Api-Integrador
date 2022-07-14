import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = 'database.db'

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

############# CATEGORIAS ################

def insert_categorias(args=()):
    sql = ''' INSERT INTO categorias(nome_categoria,descricao)
              VALUES(?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def update_categorias(args=()):
    sql = ''' UPDATE categorias SET nome_categoria = ?, descricao = ? WHERE id = ? '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def delete_categorias(id):
    sql = ''' DELETE from categorias WHERE id = ?",     
                      (id,) '''
    cur = get_db().cursor()
    cur.execute(sql, id)
    get_db().commit()
    return cur.lastrowid

############# PRODUTOS ################

def insert_produtos(args=()):
    sql = ''' INSERT INTO produtos(id_produto,codigo_produto,nome_produto,valor_produto,quantidade)
              VALUES(?,?,?,?,?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def delete_produtos(id_produto):
    sql = ''' DELETE from produtos WHERE id_produto = ?",     
                      (id_produto,) '''
    cur = get_db().cursor()
    cur.execute(sql, id_produto)
    get_db().commit()
    return cur.lastrowid

############# USERS ################

def insert_users(args=()):
    sql = ''' INSERT INTO users (nome, email, telefone, endereco,       
                    cidade) VALUES (?, ?, ?, ?, ?) '''
    cur = get_db().cursor()
    cur.execute(sql, args)
    get_db().commit()
    return cur.lastrowid

def delete_user(user_id):
    sql = ''' DELETE from users WHERE user_id = ?",     
                      (user_id,) '''
    cur = get_db().cursor()
    cur.execute(sql, user_id)
    get_db().commit()
    return cur.lastrowid
    
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = [dict((cur.description[i][0], value) \
       for i, value in enumerate(row)) for row in cur.fetchall()]
   
    get_db().commit()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
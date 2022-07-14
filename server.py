from flask import Flask, request, jsonify, abort, make_response
import db
    
app = Flask(__name__)
app.config['DEBUG']=True

# @app.errorhandler(404)
# def not_found(error):
#    return make_response(jsonify({'Status': 404, 'Error': 'Resource not found'}), 404)

########  ROUTE LISTAR CATEGORIAS

@app.route("/solucoes/categorias",methods=['GET'])
def get_categorias():
    categorias = db.query_db('SELECT * FROM categorias')
    return jsonify(categorias),200


@app.route("/solucoes/categorias/<id>",methods=['GET'])
def get_categoria(id):
    categoria = db.query_db('SELECT * FROM categorias WHERE id_categoria = ?', (id,))
    return jsonify(categoria),200
    abort(404)

########  ROUTE LISTAR PRODUTOS

@app.route("/solucoes/produtos",methods=['GET'])
def get_produtos():
    produtos = db.query_db('SELECT * FROM produtos')
    return jsonify(produtos),200


@app.route("/solucoes/produtos<id>",methods=['GET'])
def get_produto(id):
    produto = db.query_db('SELECT * FROM produtos WHERE id = ?', (id,))
    return jsonify(produto),200
    abort(404)

########  ROUTE CADASTRAR CATEGORIAS

@app.route("/solucoes/categorias",methods=['POST'])
def add_categorias():
    if request.is_json:
        categorias = request.get_json()
        id = db.insert_categorias((categorias['nome_categoria'],categorias['descricao']))
        return {"Cadastrado com sucesso!":id}, 201
    return {"error": "Request must be JSON"}, 415

########  ROUTE CADASTRAR PRODUTOS

@app.route("/solucoes/produtos",methods=['POST'])
def add_produtos():
    if request.is_json:
        produtos = request.get_json()
        id = db.insert_produtos((produtos['id_categoria'],produtos['codigo_produto'],produtos['nome_produto'],produtos['valor_produto'],produtos['quantidade']))
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415


########  ROUTE EDITAR PRODUTOS

@app.route("/solucoes/categorias_edit/<int:id>",methods=['PUT'])
def update_categoria(id):
    categorias = request.get_json()
    db.query_db(f'UPDATE categorias SET nome_categoria = "{categorias["nome_categoria"]}", descricao = "{categorias["descricao"]}" WHERE id_categoria = {id}')
    return {"Categoria Editada com sucesso!":id}, 201 

@app.route("/solucoes/produtos_edit/<int:id_produto>",methods=['PUT'])
def update_produto(id_produto):
    produtos = request.get_json()
    db.query_db(f'UPDATE produtos SET codigo_produto = "{produtos["codigo_produto"]}", nome_produto = "{produtos["nome_produto"]}", valor_produto = "{produtos["valor_produto"]}", quantidade = "{produtos["quantidade"]}" WHERE id_produtos = {id_produto}')
    return {"error": "not founded"}, 404 


########  ROUTE DELETAR PRODUTOS

@app.route("/solucoes/categorias/delete/<int:id>",methods=['DELETE'])
def delete_categoria(id):
    db.query_db(f'DELETE FROM categorias WHERE id_categoria =  {id}')
    return {"Categoria Deletado com sucesso!":id}, 201  

@app.route("/solucoes/produtos/delete<int:id>",methods=['DELETE'])
def delete_produto(id):
    db.query_db(f'DELETE FROM produtos WHERE id_produto =  {id}')
    return {"Categoria Deletado com sucesso!":id}, 201 

if __name__ == '__main__':
    init_db = False
    
    db.init_app(app)
    
    if init_db:
        with app.app_context():
            db.init_db()
    
    app.run(debug=True,host="0.0.0.0", port=8090)
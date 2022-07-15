from pickle import TRUE
from trace import Trace
from flask import Flask, request, jsonify, abort, make_response
import db
    
app = Flask(__name__)
app.config['DEBUG']=True

# @app.errorhandler(404)
# def not_found(error):
#    return make_response(jsonify({'Status': 404, 'Error': 'Resource not found'}), 404)



############  ROUTE CATEGORIAS  ################3###

@app.route("/solucoes/categorias",methods=['GET'])
def get_categorias():
    categorias = db.query_db('SELECT * FROM categorias')
    return jsonify(categorias),200


@app.route("/solucoes/categorias/<id>",methods=['GET'])
def get_categoria(id):
    categoria = db.query_db('SELECT * FROM categorias WHERE id_categoria = ?', (id,))
    return jsonify(categoria),200
    abort(404)

@app.route("/solucoes/categorias",methods=['POST'])
def add_categorias():
    if request.is_json:
        categorias = request.get_json()
        id = db.insert_categorias((categorias['nome_categoria'],categorias['descricao']))
        return {"Cadastrado com sucesso!":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/solucoes/categorias_edit/<int:id>",methods=['PUT'])
def update_categoria(id):
    categorias = request.get_json()
    db.query_db(f'UPDATE categorias SET nome_categoria = "{categorias["nome_categoria"]}", descricao = "{categorias["descricao"]}" WHERE id_categoria = {id}')
    return {"Categoria Editada com sucesso!":id}, 201 

@app.route("/solucoes/categorias/delete/<int:id>",methods=['DELETE'])
def delete_categoria(id):
    db.query_db(f'DELETE FROM categorias WHERE id_categoria =  {id}')
    return {"Categoria Deletado com sucesso!":id}, 201


###############  ROUTE PRODUTOS  ######################

@app.route("/solucoes/produtos",methods=['GET'])
def get_produtos():
    produtos = db.query_db('SELECT * FROM produtos')
    return jsonify(produtos),200


@app.route("/solucoes/produtos/<id>",methods=['GET'])
def get_produto(id):
    produto = db.query_db('SELECT * FROM produtos WHERE id_produto = ?', (id,))
    return jsonify(produto),200
    abort(404)


@app.route("/solucoes/produtos",methods=['POST'])
def add_produtos():
    if request.is_json:
        produtos = request.get_json()
        id = db.insert_produtos((produtos['codigo_produto'],produtos['nome_produto'],produtos['valor_produto'],produtos['quantidade'],produtos['id_categoria']))
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415


@app.route("/solucoes/produtos_edit/<int:id_produto>",methods=['PUT'])
def update_produto(id_produto):
    produtos = request.get_json()
    db.query_db(f'UPDATE produtos SET codigo_produto = "{produtos["codigo_produto"]}", nome_produto = "{produtos["nome_produto"]}", valor_produto = "{produtos["valor_produto"]}", quantidade = "{produtos["quantidade"]}" WHERE id_produto = {id_produto}')
    return {"Produto atualizado": id_produto}, 201
   


@app.route("/solucoes/produtos/delete/<int:id>",methods=['DELETE'])
def delete_produto(id):
    db.query_db(f'DELETE FROM produtos WHERE id_produto =  {id}')
    return {"Produto deletado com sucesso!":id}, 201 

############# Route Pedido ################

@app.route("/solucoes/pedidos",methods=['GET'])
def get_pedidos():
    pedidos = db.query_db('SELECT * FROM pedidos')
    return jsonify(pedidos),200


@app.route("/solucoes/pedidos/<id>",methods=['GET'])
def get_pedido(id):
    pedido = db.query_db('SELECT * FROM pedidos WHERE id_pedidos = ?', (id,))
    return jsonify(pedido),200
    abort(404)


@app.route("/solucoes/pedidos",methods=['POST'])
def add_pedidos():
    if request.is_json:
        pedidos = request.get_json()
        id = db.insert_pedidos((pedidos['quant_pedido'],pedidos['valor_pedido'],pedidos['data_pedido']))
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415


@app.route("/solucoes/pedidos_edit/<int:id_pedidos>",methods=['PUT'])
def update_pedidosb(id_pedidos):
    pedidos = request.get_json()
    db.query_db(f'UPDATE pedidos SET quant_pedido = "{pedidos["quant_pedido"]}", valor_pedido = "{pedidos["valor_pedido"]}", data_pedido = "{pedidos["data_pedido"]}"WHERE id_pedidos = {id_pedidos}')
    return {"Pedido atualizado atualizado": id_pedidos}, 201
   
############# ROUTE PEDIDO/PRODUTO ##############

@app.route("/solucoes/ped_prod",methods=['POST'])
def add_ped_prod():
    if request.is_json:
        ped_prods = request.get_json()
        id = db.insert_pedido_produto((ped_prods['id_pedidos'], ped_prods['id_produto']))
        return {"Cadastrado com sucesso!":id}, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/solucoes/ped_prod",methods=['GET'])
def get_ped_prod():
    ped_prods = db.query_db('SELECT * FROM ped_prod')
    
    return jsonify(ped_prods),200


if __name__ == '__main__':
    init_db = False
    
    db.init_app(app)
    
    if init_db:
        with app.app_context():
            db.init_db()
    
    app.run(debug=True,host="0.0.0.0", port=8090)
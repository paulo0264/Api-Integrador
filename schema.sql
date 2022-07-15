DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS ped_prod;


CREATE TABLE categorias (
  id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_categoria TEXT NOT NULL,
  descricao TEXT NOT NULL
);

CREATE TABLE produtos (
  id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo_produto TEXT UNIQUE NOT NULL,
  nome_produto TEXT NOT NULL,
  valor_produto TEXT NOT NULL,
  quantidade INTEGER NOT NULL,
  id_categoria INTEGER,
  FOREIGN KEY(id_categoria) REFERENCES categorias(id)
);

CREATE TABLE pedidos (
id_pedidos INTEGER PRIMARY KEY AUTOINCREMENT,
quant_pedido INTEGER NOT NULL,
valor_pedido TEXT NOT NULL,
data_pedido TEXT NOT NULL
);

CREATE TABLE ped_prod(
id_ped_prod INTEGER PRIMARY KEY AUTOINCREMENT,
id_produto INTEGER,
id_pedidos INTEGER,
FOREIGN KEY(id_produto) REFERENCES produtos(id),
FOREIGN KEY(id_pedidos) REFERENCES pedidos(id)


)
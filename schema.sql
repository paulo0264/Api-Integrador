DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS produtos;

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
  FOREIGN KEY(id_categoria) REFERENCES categorias(id)
);
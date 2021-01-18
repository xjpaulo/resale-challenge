CREATE TABLE imoveis (
imovel_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome varchar(100) NOT NULL,
endereco varchar(150) NOT NULL,
descricao varchar(150) NOT NULL,
status varchar(7) NOT NULL,
caracteristicas varchar(200),
tipo varchar(11) NOT NULL,
finalidade varchar(11),
imobiliaria_id int NOT NULL,
FOREIGN KEY (imobiliaria_id) REFERENCES imobiliarias(imobiliaria_id)
ON DELETE CASCADE
);

CREATE TABLE imobiliarias (
imobiliaria_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome varchar(100) NOT NULL,
endereco varchar(150)
);
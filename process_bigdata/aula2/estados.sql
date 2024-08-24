DROP TABLE IF EXISTS municipio;
DROP TABLE IF EXISTS estado;

CREATE TABLE estado(
    uf TEXT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    id_regiao TEXT NOT NULL,
    FOREIGN KEY (id_regiao) REFERENCES regiao(id)
);

INSERT INTO estado (uf, nome, id_regiao) VALUES ('AC', 'Acre', 'N');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('AL', 'Alagoas', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('AP', 'Amapá', 'N');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('AM', 'Amazonas', 'N');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('BA', 'Bahia', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('CE', 'Ceará', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('DF', 'Distrito Federal', 'CO');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('ES', 'Espírito Santo', 'SE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('GO', 'Goiás', 'CO');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('MA', 'Maranhão', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('MT', 'Mato Grosso', 'CO');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('MS', 'Mato Grosso do Sul', 'CO');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('MG', 'Minas Gerais', 'SE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('PA', 'Pará', 'N');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('PB', 'Paraíba', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('PR', 'Paraná', 'S');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('PE', 'Pernambuco', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('PI', 'Piauí', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('RJ', 'Rio de Janeiro', 'SE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('RN', 'Rio Grande do Norte', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('RS', 'Rio Grande do Sul', 'S');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('RO', 'Rondônia', 'N');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('RR', 'Roraima', 'N');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('SC', 'Santa Catarina', 'S');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('SP', 'São Paulo', 'SE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('SE', 'Sergipe', 'NE');
INSERT INTO estado (uf, nome, id_regiao) VALUES ('TO', 'Tocantins', 'N');

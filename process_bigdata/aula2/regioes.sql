DROP TABLE IF EXISTS municipio;
DROP TABLE IF EXISTS estado;
DROP TABLE IF EXISTS regiao;

CREATE TABLE regiao(
    id TEXT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

INSERT INTO regiao (id, nome) VALUES ('N', 'Norte');
INSERT INTO regiao (id, nome) VALUES ('NE', 'Nordeste');
INSERT INTO regiao (id, nome) VALUES ('CO', 'Centro-Oeste');
INSERT INTO regiao (id, nome) VALUES ('SE', 'Sudeste');
INSERT INTO regiao (id, nome) VALUES ('S', 'Sul');
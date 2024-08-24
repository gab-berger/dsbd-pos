--a. Exiba todos os municípios em ordem alfabética, juntamente com seus estados e regiões. Use inner join.

SELECT
    municipio.nome,
    estado.nome,
    regiao.nome
FROM municipio
INNER JOIN estado ON municipio.uf = estado.uf
INNER JOIN regiao ON estado.id_regiao = regiao.id
ORDER BY municipio.nome
LIMIT 10;

--b. Exiba todos os municípios homônimos, onde os homônimos devem estar na mesma região.
SELECT
    m1.nome,
    e1.nome,
    r1.nome,
    m2.nome,
    e2.nome,
    r2.nome
FROM municipio m1
    INNER JOIN estado e1 ON m1.uf = e1.uf
    INNER JOIN regiao r1 ON e1.id_regiao = r1.id
    INNER JOIN municipio m2 ON m1.nome = m2.nome
    INNER JOIN estado e2 ON m2.uf = e2.uf
    INNER JOIN regiao r2 ON e2.id_regiao = r2.id
WHERE m1.nome = m2.nome AND r1.nome = r2.nome AND e1.nome < e2.nome
ORDER BY m1.nome
LIMIT 10;

--c. Exiba todas as combinações únicas entre nomes de município e região do Brasil.
SELECT
    municipio.nome,
    regiao.nome
FROM municipio
INNER JOIN estado ON municipio.uf = estado.uf
INNER JOIN regiao ON estado.id_regiao = regiao.id
ORDER BY municipio.nome
LIMIT 10;

--d. Conte quantos municípios existem na região SUL do Brasil.
SELECT
    count(municipio.nome)
FROM municipio
INNER JOIN estado ON municipio.uf = estado.uf
INNER JOIN regiao ON estado.id_regiao = regiao.id
WHERE regiao.id = 'S';

--e. Liste os municípios possuem ‘ão’ em algum lugar do nome, e que ficam no Nordeste.
SELECT
    municipio.nome
FROM municipio
INNER JOIN estado ON municipio.uf = estado.uf
INNER JOIN regiao ON estado.id_regiao = regiao.id
WHERE regiao.id = 'NE' AND municipio.nome LIKE '%ão%'
LIMIT 10;
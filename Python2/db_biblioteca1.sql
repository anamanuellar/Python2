CREATE DATABASE db_Biblioteca;
USE db_Biblioteca;
CREATE TABLE IF NOT EXISTS tbl_livro (
ID_Livro SMALLINT  AUTO_INCREMENT PRIMARY KEY,
Nome_Livro VARCHAR(70) NOT NULL,
ISBN13 CHAR(13),
ISBN10 CHAR(10),
ID_Categoria SMALLINT,
ID_Autor SMALLINT NOT NULL,
Data_Pub DATE NOT NULL,
Preco_Livro DECIMAL(6,2) NOT NULL
);
CREATE TABLE tbl_autores (
ID_Autor SMALLINT PRIMARY KEY,
Nome_Autor VARCHAR(50) NOT NULL,
Sobrenome_Autor VARCHAR(60) NOT NULL
);
CREATE TABLE tbl_categorias (
ID_Categoria SMALLINT PRIMARY KEY,
Categoria VARCHAR(30) NOT NULL
);
CREATE TABLE tbl_editoras (
ID_Editora SMALLINT PRIMARY KEY AUTO_INCREMENT,
Nome_Editora VARCHAR(50) NOT NULL
);
/*tabela de nome tbl_teste_incremento para estudar o uso do auto incremento em colunas*/
CREATE TABLE tbl_teste_incremento (
Codigo SMALLINT PRIMARY KEY AUTO_INCREMENT,
Nome VARCHAR(20) NOT NULL
) AUTO_INCREMENT = 15;

/*inserindo dados aleatórios na tabela para realizar o teste*/
INSERT INTO tbl_teste_incremento (Nome) VALUES ('Ana');
INSERT INTO tbl_teste_incremento (Nome) VALUES ('Maria');
INSERT INTO tbl_teste_incremento (Nome) VALUES ('Julia');
INSERT INTO tbl_teste_incremento (Nome) VALUES ('Joana');
/*INSERT INTO tbl_teste_incremento (Nome) VALUES ('Pedro'); exemplo de novo incremento para verificar se foi adicinado com código 90*/

/*verificando se o auto invremento funcionou executando uma consulta na tabela*/
SELECT * FROM tbl_teste_incremento;

/*verificar o valor de incremento mais atual armazenado em uma tabela*/
SELECT MAX(ID_Livro)
FROM tbl_livro;

/* alterar o valor de incremento do próximo registro a ser armazenado em uma tabela*/
ALTER TABLE tbl_teste_incremento
AUTO_INCREMENT = 90;

/*adicionar a coluna id_autor na tabela tbl_livro, com a constraint de chave estrangeira (a chave primária está na tabela tbl_autores)*/
ALTER TABLE tbl_livro
ADD  ID_Autor  SMALLINT NOT NULL;

/*adicionando a chave estrangeira*/
ALTER TABLE tbl_livro
ADD CONSTRAINT fk_ID_Autor
FOREIGN KEY (ID_Autor)
REFERENCES tbl_autores (ID_autor)
ON DELETE CASCADE
ON UPDATE CASCADE;

/*adicionar à tabela tbl_livro a coluna id_editora*/
ALTER TABLE tbl_livro
ADD  ID_editora  SMALLINT NOT NULL;

/*fazendo tbl_livro como chave estrangeira da tabela tbl_editoras*/
ALTER TABLE tbl_Livro
ADD CONSTRAINT fk_id_editora
FOREIGN KEY (ID_editora)
REFERENCES tbl_editoras (ID_editora)
ON DELETE CASCADE
ON UPDATE CASCADE;

/* criando o relacionamento entre a tabela de livros e a tabela de categorias*/
ALTER TABLE tbl_Livro
ADD CONSTRAINT fk_id_categoria
FOREIGN KEY (ID_Categoria)
REFERENCES tbl_categorias (ID_Categoria)
ON DELETE CASCADE
ON UPDATE CASCADE;

/* inserindo dados de editoras na tabela tbl_editoras*/
INSERT INTO tbl_editoras (Nome_Editora) VALUES ('Prentice Hall');
INSERT INTO tbl_editoras (Nome_Editora) VALUES ('O´Reilly');
INSERT INTO tbl_editoras (Nome_Editora) VALUES ('Microsoft Press');
INSERT INTO tbl_editoras (Nome_Editora) VALUES ('Wiley');
INSERT INTO tbl_editoras (Nome_Editora) VALUES ('McGraw-Hill Education');

/*No exemplo anterior executamos o comando INSERT INTO repetidas vezes. */
/*Mas é possível executá-lo apenas uma vez e inserir múltiplos registros, como mostra o código abaixo, que irá inserir 12 autores de uma vez na tabela tbl_autores*/
INSERT INTO tbl_autores
VALUES
(1, 'Daniel', 'Barret'),
(2, 'Gerald', 'Carter'),
(3, 'Mark', 'Sobell'),
(4, 'William', 'Stanek'),
(5, 'Richard', 'Blum'),
(6, 'Jostein', 'Gaarder'),
(7, 'Umberto', 'Eco'),
(8, 'Neil', 'De Grasse Tyson'),
(9, 'Stephen', 'Hawking'),
(10, 'Stephen', 'Jay Gould'),
(11, 'Charles', 'Darwin'),
(12, 'Alan', 'Turing'),
(13, 'Simon', 'Monk'),
(14, 'Paul', 'Scherz');

/*inserindo dados na tabela de categorias*/
INSERT INTO tbl_categorias
VALUES
(1, 'Tecnologia'),
(2, 'História'),
(3, 'Literatura'),
(4, 'Astronomia'),
(5, 'Botânica');

/*inserindo dados na tabela de livros*/
INSERT INTO tbl_Livro (Nome_Livro, ISBN13, ISBN10, Data_Pub, Preco_Livro, ID_Categoria, ID_Autor, ID_Editora)
VALUES
('Linux Command Line and Shell Scripting','9781118983843', '111898384X', '20150109', 68.35, 1, 5, 4),
('SSH, the Secure Shell','9780596008956', '0596008953', '20050517', 58.30, 1, 1, 2),
('Using Samba','9780596002565', '0596002564', '20031221', 61.45, 1, 2, 2),
('Fedora and Red Hat Linux', '9780133477436', '0133477436', '20140110', 62.24, 1, 3, 1),
('Windows Server 2012 Inside Out','9780735666313', '0735666318', '20130125', 66.80, 1, 4, 3),
('Microsoft Exchange Server 2010','9780735640610', '0735640610', '20101201', 45.30, 1, 4, 3),
('Practical Electronics for Inventors', '9781259587542', '1259587541', '20160324', 67.80, 1, 13, 5);
/*Neste último exemplo, uma das colunas não recebeu dados inseridos pelo comando (ID_livro é auto-incrementado), então especificamos as colunas que receberiam dados.*/

/*Testando a inserção de dados*/
SELECT * FROM tbl_autores;
SELECT * FROM tbl_editoras;
SELECT * FROM tbl_livro;

TRUNCATE TABLE tbl_teste_incremento;
/*ALIAS - retornando a coluna Nome_Livro com o nome de Livro apenas*/
SELECT Nome_Livro
AS Livro
FROM tbl_Livro;

/*aplicando ALIAS sem a necessidade de usar a plavras AS: basta inserir o alias desejado logo após o nome da coluna sem separação por vírgulas*/
SELECT Nome_Livro Livro, Preco_Livro 'Preço do Livro'
FROM tbl_Livro;

/*Funções de agregação*/
/* COUNT - retornando o número total de autores cadastrados na tabela de autores*/
SELECT COUNT(*) FROM tbl_autores;
/*COUNT DISTINCT - Contar o número de autores que possuem livros cadastrados na tabela de autores, sem repetições*/
SELECT COUNT(DISTINCT id_autor) FROM tbl_Livro;
/*MAX - Descobrir o preço mais alto dos livros*/
SELECT MAX(Preco_Livro) FROM tbl_Livro;
/*MIN - Descobrir a data de publicação do livro mais antigo*/
SELECT MIN(Data_Pub) FROM tbl_Livro;
/*AVG - Retornar o preço médio dos livros cadastrados no banco*/
SELECT AVG(Preco_Livro) FROM tbl_Livro;
/*SUM - Descobrir o valor total dos livros presentes na tabela de livros*/
SELECT SUM(Preco_Livro) FROM tbl_Livro;

/*retornar todos os livros da tabela tbl_livro cuja data de publicação esteja entre 17/05/2004 e 17/05/2011 (a data é fornecida no código: ano|mês|dia)*/
SELECT * FROM tbl_Livro
WHERE Data_Pub BETWEEN '20040517' AND '20110517';

/* retornar os nomes dos livros e seus respectivos preços, da tabela tbl_livros, porém somente os livros cujos preços estiverem entre R$ 40,00 e 60,00*/
SELECT Nome_Livro AS Livro, Preco_Livro AS Preço
FROM tbl_Livro
WHERE Preco_Livro BETWEEN 40.00 AND 60.00;

/*LIKE E NOT LIKE*/
/*Selecionar todos os registros da tabela tbl_livro cujo nome comece com a letra F*/
SELECT * FROM tbl_Livro
WHERE Nome_Livro LIKE 'F%'; 

/*Selecionar todos os registros da tabela tbl_livro cujo nome não começa com a letra S*/
SELECT * FROM tbl_Livro
WHERE Nome_Livro NOT LIKE 'S%'; 

/*Selecionar os nomes de livros da tabela tbl_livro cujo nome se inicie com uma letra qualquer e a segunda letra seja a letra i*/
SELECT Nome_Livro
FROM tbl_Livro
WHERE Nome_Livro LIKE '_i%';

/*Selecionar os nomes dos livros e seus respectivos preços, na tabela de livros, cujo nome não comece com a letra F e que custem mais de R$ 60,00*/
SELECT Nome_Livro AS Livro, Preco_Livro AS Valor
FROM tbl_livro
WHERE Nome_Livro NOT LIKE 'F%'
AND Preco_Livro > 60.00;

/* Aplicando Padrões: criar o padrão de sobrenome “da Silva” na coluna Sobrenome_autor da tabela tbl_autores quando não informado*/
ALTER TABLE tbl_autores
MODIFY COLUMN Sobrenome_Autor Varchar(60)
DEFAULT 'da Silva';

INSERT INTO tbl_autores (ID_Autor, Nome_autor)
VALUES (15, 'João');

SELECT * FROM tbl_autores;

/*Removendo o padrão no campo sobrenome criado no código acima quando não informado*/
ALTER TABLE tbl_autores
MODIFY COLUMN Sobrenome_Autor Varchar(60);
INSERT INTO tbl_autores (ID_Autor, Nome_autor)
VALUES (16, 'Joana');
SELECT * FROM tbl_autores;

/*criar uma view de nome vw_LivrosAutores que retorne ao ser consultada os nomes dos livros e seus respectivos autores*/
CREATE VIEW vw_LivrosAutores
AS SELECT tbl_Livro.Nome_Livro AS Livro, tbl_autores.Nome_Autor AS Autor
FROM tbl_Livro
INNER JOIN tbl_autores
ON tbl_Livro.ID_Autor = tbl_autores.ID_Autor;

/*alterar a view vw_LivrosAutores para incluir também os preços dos livros*/
ALTER  VIEW vw_LivrosAutores AS
SELECT tbl_Livro.Nome_Livro AS Livro, tbl_autores.Nome_Autor AS Autor, Preco_Livro AS Valor
FROM tbl_Livro
INNER JOIN tbl_autores
ON tbl_Livro.ID_Autor = tbl_autores.ID_Autor;


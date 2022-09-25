-- DDL: Criando banco de dados
create database if not exists Ferramentas;
use Ferramentas;
create table if not exists Produtos (
	-- Bytes: 4 Range: -2.147.483.647 a 2.147.483.647
    -- htpps://dev.mysql.com/doc/refman/8.0/en/storage-requirements.html
		#data-types-storage-reqs-numeric
	codigo int primary key auto_increment,
    nome varchar (255) not null,
    -- Storage: Bytes: 2 Range: -32.767 a 32.767
    ano_fab smallint,
    -- De: -99.999.999,99 a 99.999.999,99
    preco decimal (10,2) not null
    );
create table if not exists Pedidos (
	pedido int unsigned primary key,
    cod_cliente int unsigned,
    -- Situaçao: C = Completo, P = Pendente Pagto, E = Em processamento
    -- R = Rejeitado Pagamento
    situacao set('C', 'P', 'E', 'R') not null default 'E',
    data_pedido date not null,            
    -- data
    total decimal (10,2) null
    );
create table if not exists Itens (
	cod_pedido int unsigned not null,
    cod_produto int not null,
    -- Chave primaria composta cod pedido e produto
    quantidade decimal (5,3) not null,
    desconto decimal (4,2) default 0,
	primary key (cod_pedido, cod_produto), 
		-- chave primaria composta
	foreign key (cod_pedido) 
		-- chave estrangeiar para o relacionamento entre tabelas
        references Pedidos (pedido)
        -- Ao excluir ou atualizar as tabelas principais, a exclusao ou
        -- atualizacao ira se propagar para esta tabela
		on delete cascade on update cascade,
	foreign key (cod_produto) 
        references Produtos (codigo)
		on delete cascade on update cascade
);
-- DML: Manipulando dados
-- Alterando a tabela Pedidos (Adicionando um campo)
alter table Pedidos
	add data_entrega date null;

-- Alterando a tabela Pedidos 
alter table Pedidos
	drop column total;
    
-- Alterando a tabela Produtos (Renomeando um campo)
-- Renomeando com 'change' e obrigatorio informar a definicao
alter table Produtos
	change column nome nomes varchar(200);

-- Alterando a tabela Produtos (Modificando a definicao de um campo)
alter table Produtos
	modify column nomes char (200) default 'SEM NOME';

-- Inserindo dados no Banco:
insert into Produtos (nomes, ano_fab, preco) values
	('Furadeira', 2020, 360.00),
    ('Chave de Fenda Longa N.5',20201, 29.50),
    ('Lixadeira Orbital Eletrca', 2022, 480.00);
    
-- inserindo um registro usando o campo 'nome' como 'default'
insert into Produtos (ano_fab, preco) value (2022, 0.0);
insert into Pedidos (pedido, cod_cliente, data_pedido) values (1, 1, '2022-09-15');
insert into Itens (cod_pedido, cod_produto, quantidade) values
	(1, 1, 1),
    (1, 2, 5),
    (1, 3, 2);
    
-- Excluindo Registros utilizando 'and' quando houver duas chaves primarias
delete from Itens where cod_pedido=1 and cod_produto=3;

-- Atualizando o campo 'quantidade' em 'Itens'
update Itens
	set quantidade = 10
    where cod_pedido= 1 and cod_produto=2;
    
-- Gerando consultas como relatorios (querys)
select nomes, preco from Produtos;

-- consulta com condicao:
select * from produtos where (Produtos.preco < 400);

-- consulta com mais que uma tabela:
select Produtos.nomes, Produtos.preco, Itens.Quantidade, Pedidos.data_pedido
	from Produtos, Itens, Pedidos
    where Produtos.codigo=Itens.cod_produto and Pedidos.pedido = Itens.cod_pedido
    order by Produtos.nomes asc;

-- commit: quando uma transaction e executada por completo (se o teste der certo, o default e commit para gravar)
-- roolback: quando a transaction falha, todas as açoes sao desfeitas (similar o desfazer)
start transaction;
	delete from Produtos where codigo=3;
    insert into Produtos (nomes, ano_fab, preco) values
		('Arco de Serra', 2018, 17.60);
	select * from Produtos;
    rollback;
    select * from Produtos;

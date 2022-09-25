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

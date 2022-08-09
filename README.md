# Docker Catalisa

## Index

- [Docker com Banco de dados Mysql](https://github.com/GuillaumeFalourd/docker-catalisa/blob/main/README.md#-docker-com-banco-de-dados-mysql)
- [Docker com Backend Python](https://github.com/GuillaumeFalourd/docker-catalisa/blob/main/README.md#-docker-com-backend-python)
- [Docker Compose](https://github.com/GuillaumeFalourd/docker-catalisa/blob/main/README.md#-docker-compose)
- [Desafio](https://github.com/GuillaumeFalourd/docker-catalisa/blob/main/README.md#-desafio)


## 🗃 Docker com Banco de dados Mysql

### 1.1 Construir a imagem

Na pasta `mysql` do repositório:

```bash
docker build -t company-database .
```

Conferir que a imagem foi gerada:

```
docker images
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
company-database        latest    89b38d78dc16   20 seconds ago   431MB
```

### 1.2 Rodando o Container

```bash
docker run -d -p 3306:3306 --name company-database -e MYSQL_ROOT_PASSWORD=RootPassword company-database
```

Será possível consultar que o container está `up` usando o comando `docker ps`.

### 1.3 Acesso ao Banco

```bash
docker exec -it company-database bash

mysql -uroot -p
Enter password: (RootPassword)
```

_Nota: Você pode rodar o comando `exit` em qualquer momento para sair do mysql ou do container do Docker._

#### 1.3.1 Acessar database

```bash
mysql> show databases;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| Company            |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

#### 1.3.2 Acessar database company

```
mysql> use Company;

Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed
```

#### 1.3.3 Mostrar Tabelas

```
mysql> show tables;

+-------------------+
| Tables_in_company |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.00 sec)
```

#### 1.3.4 Mostrar colunas tabela employees

```
mysql> show columns from employees;

+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| first_name | varchar(25) | YES  |     | NULL    |       |
| last_name  | varchar(25) | YES  |     | NULL    |       |
| department | varchar(15) | YES  |     | NULL    |       |
| email      | varchar(50) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)
```

#### 1.3.5 Mostrar conteúdo tabela employees

```
mysql> select * from employees;
+------------+-----------+------------+-------------------+
| first_name | last_name | department | email             |
+------------+-----------+------------+-------------------+
| Lorenz     | Vanthillo | IT         | lvthillo@mail.com |
+------------+-----------+------------+-------------------+
1 row in set (0.01 sec)
```

### 1.4 Matar o container

Após ter saido do container (usando o comando `exit`), ele continuará `Up` até você parar-lo.

Confere usando o comando `docker ps` que aparece ainda um container usando a imagem e o nome `company-database`.

Para parar-lo, use o comando `docker kill <CONTAINER_ID>` (após selecionar o CONTAINER ID que deseje parar).

Através do comando `docker ps -a` agora, é possível conferir que o estado do container é `Exited`.

Para remover-lo definitivamente dessa lista e conseguir subir um novo container usando o mesmo nome, basta executar `docker rm <CONTAINER_ID>`.

Após isso, até a lista retornada pelo comando `docker ps -a` estará vazia.


## 🐍 Docker com Backend Python

### 1.1 Construir a imagem

Na pasta `backend` do repositório:

```bash
docker build -t company-backend .
```

Conferir que a imagem foi gerada:

```
docker images
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
company-backend        latest    89b38d78dc16   20 seconds ago   431MB
```

### 1.2 Rodando o Container

```bash
docker run -d -p 80:80 --name company-backend company-backend
```

Abrindo o navegador, daria para acessar a página inicial do app na URL [http://0.0.0.0/](http://0.0.0.0/) retornando `Hello World`.

Já, a URL [http://0.0.0.0/employees](http://0.0.0.0/employees) não funcionaria, como o banco de dados não está configurado.

### 1.3 Acessar o app

```bash
docker exec -it company-backend bash
```

Uma vez no container, você pode listar e ver os arquivos que foram inclusos la.

_Nota: Você pode rodar o comando `exit` em qualquer momento para sair do container._

### 1.4 Matar o container

Da mesma forma que com o container do database, após ter saido do container de backend (usando o comando `exit`), ele continuará `Up` até você parar-lo.

Confere usando o comando `docker ps` que aparece ainda um container usando a imagem e o nome `company-backend`.

Para parar-lo, use o comando `docker kill <CONTAINER_ID>` (após selecionar o CONTAINER ID que deseje parar).

Através do comando `docker ps -a` agora, é possível conferir que o estado do container é `Exited`.

Para remover-lo definitivamente dessa lista e conseguir subir um novo container usando o mesmo nome, basta executar `docker rm <CONTAINER_ID>`.

Após isso, até a lista retornada pelo comando `docker ps -a` estará vazia.


## 🐍🗃 Docker Compose

Quando trabalhamos com vários containers, gerenciar a execução deles pode ficar mais complexo. 
Para isso, temos algumas tecnologias que auxiliam, sendo uma delas o **Docker Compose**. 

### 1. Subir o docker-compose1

Na pasta `root` do repositório:

```bash
docker-compose up
```

_Obs: Caso algumas portas já estiverem sendo usadas, liste os containers ativos através do comando `docker ps`, e após selecionar o CONTAINER ID que deseje parar e execute o comando `docker kill <CONTAINER_ID>`_

Abrindo o navegador, daria para acessar a página inicial do app na URL [http://0.0.0.0/](http://0.0.0.0/) retornando `Hello World`.

Também daria agora para acessar a URL [http://0.0.0.0/employees](http://0.0.0.0/employees) com sucesso, que retornaria a lista de `employees` presentes no banco.

### 2. Derrubar o docker-compose

Para sair do prompt do docker-compose up, use as teclas `CTRL + C`.

Isso não vai remover os containers, será ainda possível ver que eles usando o comando `docker ps -a`.

Para remover os containers, use o seguinte comando:

```bash
docker-compose down
```

Executando o comando `docker ps -a` agora, os containers não deveriam mais aparecer.


## 🛠 Desafio

Agora que entendeu como o Docker e o Docker Compose funcionam, tentem adaptar o código presente nesse projeto usando agora um Backend em Java com JDBC.

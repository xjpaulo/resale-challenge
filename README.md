# resale-challenge

Uma API RESTful para controle de registros de imóveis e imobiliárias através de operações CRUD. Esta API foi desenvolvida em Python, utilizando Flask, uWSGI, MySQL e Docker.

## Introdução

Ao acessar os endpoints da API utilizando os métodos de requisição POST-GET-PUT-DELETE, também conhecidos como operações CRUD, é possível gerenciar e listar os registros de imobiliárias e imóveis no banco de dados. O retorno das requisições sempre será no formato JSON.

## Pré-requisitos

 - [docker](https://docs.docker.com/)
 - [docker-compose](https://docs.docker.com/compose/)

## Infraestrutura

 - Gateway - Foi utilizado o uWSGI para permitir e controlar processos simultâneos;
 - API - Aplicação construída em Python junto com o framework Flask para criação de endpoints;
 - Banco de dados - O registro de imobiliárias e imóveis é armazenado dentro de um banco MySQL;
 - Docker - Utiliza dois containers: um para o serviço em Python e outro para o banco de dados.

## Configuração
Para iniciar a aplicação, execute o docker-compose na pasta raiz após clonar o repositório:
```
$ sudo docker-compose up --detach --build
```
Os logs podem ser acompanhados pelo comando:  
```
$ sudo docker-compose logs --follow
```
## Funcionamento

Após a instalação, leve em conta alguns segundos para o serviço do MySQL subir e aceitar conexões. A API ficará disponível através da URL abaixo:

`http://localhost:8080/`

### **Endpoints:**

 - **Listar imobiliárias**
 
```
GET localhost:8080/imobiliarias/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `nome` | opcional | string | Nome de imobiliária para filtrar na lista   |
|  `pagina` | opcional  |  int | Número da página que deseja visualizar  |
| `itens` | opcional | int | Número de itens para serem exibidos por página

 - **Listar única imobiliária**
 
```
GET localhost:8080/imobiliarias/<imobiliaria_id>/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `nome` | opcional | string | Nome de imobiliária para filtrar na lista   |
|  `pagina` | opcional  |  int | Número da página que deseja visualizar  |
| `itens` | opcional | int | Número de itens para serem exibidos por página

 - **Adicionar imobiliária**
 
``` 
POST localhost:8080/imobiliarias/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `nome` | obrigatório | string | Nome da imobiliária   |
|  `endereco` | opcional  |  string | Endereço da imobiliária  |

 - **Alterar imobiliária**
 
``` 
PUT localhost:8080/imobiliarias/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `imobiliaria_id` | obrigatório | int | ID da imobiliária que será alterada  |
|  `nome` | obrigatório | string | Nome da imobiliária   |
|  `endereco` | opcional | string | Endereço da imobiliária   |

 - **Remover imobiliária**
 
``` 
DELETE localhost:8080/imobiliarias/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `imobiliaria_id` | obrigatório | int | ID da imobiliária   |

>  Ao remover uma imobiliária, todos os imóveis vinculados à mesma também serão apagados.  

 - **Listar todos os imóveis**
 
```
GET localhost:8080/imobiliarias/imoveis/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `nome` | opcional | string | Nome de imóvel para filtrar na lista   |
|  `pagina` | opcional  |  int | Número da página que deseja visualizar  |
| `itens` | opcional | int | Número de itens para serem exibidos por página

 - **Listar imóveis por imobiliária**
 
```
GET localhost:8080/imobiliarias/<imobiliaria_id>/imoveis/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `nome` | opcional | string | Nome de imóvel para filtrar na lista   |
|  `pagina` | opcional  |  int | Número da página que deseja visualizar  |
| `itens` | opcional | int | Número de itens para serem exibidos por página

 - **Listar único imóvel**
 
```
GET localhost:8080/imobiliarias/<imobiliaria_id>/imoveis/<imovel_id>/
```

 - **Adicionar imóvel**
 
``` 
POST localhost:8080/imobiliarias/imoveis/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `nome` | obrigatório | string | Nome do imóvel  |
|  `endereco` | obrigatório  |  string | Endereço do imóvel  |
|  `descricao` | obrigatório  |  string | Descrição do imóvel  |
|  `imobiliaria_id` | obrigatório  |  int | ID da imobiliária do imóvel (Precisa existir na tabela imobiliarias) |
|  `status` | obrigatório  |  string | Status (Ativo ou Inativo) |
|  `tipo` | obrigatório  |  string | Tipo (Apartamento ou Casa) |
|  `finalidade` | opcional  |  string | Finalidade (Residencial ou Escritorio) |
|  `caracteristicas` | opcional  |  string | Características do imóvel (Quartos, salas, banheiros, vagas de garagem, ...) |

 - **Alterar imóvel**
 
``` 
PUT localhost:8080/imobiliarias/imoveis/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `imovel_id` | obrigatório | int | ID do imóvel que será alterado |
|  `nome` | obrigatório | string | Nome do imóvel  |
|  `endereco` | obrigatório  |  string | Endereço do imóvel  |
|  `descricao` | obrigatório  |  string | Descrição do imóvel  |
|  `imobiliaria_id` | obrigatório  |  int | ID da imobiliária do imóvel (Precisa existir na tabela imobiliarias)  |
|  `status` | obrigatório  |  string | Status (Ativo ou Inativo) |
|  `tipo` | obrigatório  |  string | Tipo (Apartamento ou Casa) |
|  `finalidade` | opcional  |  string | Finalidade (Residencial ou Escritorio) |
|  `caracteristicas` | opcional  |  string | Características do imóvel (Quartos, salas, banheiros, vagas de garagem, ...) |

 - **Remover imóvel**
 
``` 
DELETE localhost:8080/imobiliarias/imoveis/
```

Parâmetros:

| Campo  | Requisição  | Tipo  | Descrição  |
| ------------ | :------------: | ------------ | ------------ |
|  `imovel_id` | obrigatório | int | ID do imóvel   |

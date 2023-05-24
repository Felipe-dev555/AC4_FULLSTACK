# AC4 Cadastrar Carros (GET & POST)

Criar uma estrutura no backend em Python onde exista pelo menos 2 rotas (Methods GET e POST) que possam se comunicar com uma estrutura de banco de dados e executando as ações de cada um dos Methods. Após finalizado armazenar o arquivo em um repositório (git) e enviar no campo abaixo.


# ⛏  Tech & Dependências

### Pré-requisitos

*   PYTHON 3.11.3
*   MySQL

## Clonando o serviço

```sh
git clone git@github.com:Felipe-dev555/AC4_FULLSTACK.git
 
```

# Executando o serviço

Na pasta raiz do projeto executar o comando:

```sh
  python app.py
```


# Criar MySQL


```sh
CREATE DATABASE db_Carros;

USE db_Carros;

CREATE TABLE carro (
  codigo int(4) AUTO_INCREMENT,
  marca varchar(30) NOT NULL,
  modelo varchar(50),
  data_carro date,
  PRIMARY KEY (codigo)
);
```

# Testar no Postman o método POST & GET


### POST
<br>
```sh
http://127.0.0.1:5000/cadastrarCarros
```
</br>

<br>
Minimun Payload in POST: 
```JSON
{
    "marca": "vw",
    "modelo": "gol"
}
```

</br>

Example:
```JSON
[
  [
    1, 
    "vw", 
    "gol", 
    null
  ]
]
```

### GET

```sh
http://127.0.0.1:5000/listarTodos
```
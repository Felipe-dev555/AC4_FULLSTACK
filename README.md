CREATE DATABASE db_Carros;

USE db_Carros;

CREATE TABLE carro (
  codigo int(4) AUTO_INCREMENT,
  marca varchar(30) NOT NULL,
  modelo varchar(50),
  data_carro date,
  PRIMARY KEY (codigo)
);
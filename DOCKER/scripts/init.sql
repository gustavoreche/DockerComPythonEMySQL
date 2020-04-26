CREATE DATABASE emailDocker;

USE emailDocker;

CREATE TABLE emails ( 
    id INT NOT NULL AUTO_INCREMENT,  
    data_email DATETIME NOT NULL,  
    assunto VARCHAR(100) NOT NULL,  
    mensagem VARCHAR(500) NOT NULL,  
    PRIMARY KEY (id));



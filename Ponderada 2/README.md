# Atividade 2: Criação de uma aplicação protegida com CRUD

# Enunciado 

Esta atividade tem por objetivo desenvolver um projeto web que possibilite os usuários registrarem dados em um banco de dados. O deploy do banco, da API do backend e do frontend deve acontecer utilizando uma aplicação com múltiplos containers. A aplicação não precisa utilizar frameworks, pode ser realizada utilizando os primitivos presentes na linguagem de programação escolhida.

### **Divisão do projeto em containers:**

**Para os projetos que vão trabalhar com 2 containers:**

 - Container da aplicação (interface e backend);
 -  Container do banco de dados.

**Para os projetos que vão trabalhar com 3 containers:**

 - Container da interface com o usuário (frontend da aplicação);
 - Container do sistema de API (backend da aplicação); 
 - Container do banco de dados. 

A escolha de uma das estratégias está totalmente vinculada a experiência que o estudante deseja praticar. De qualquer forma, será necessário justificar a escolha da arquitetura utilizada para a solução.

Espera-se encontrar na entrega do projeto:

 - Arquitetura da solução utilizada (no arquivo README do projeto) e a
   justificativa de sua escolha; 
 - Um arquivo docker-compose para o lançamento da aplicação; 
 -  Instruções para lançar a aplicação; Instruções para utilizar a aplicação; - Uma descrição da estrutura de dados utilizada para armazenar os dados no banco de dados;  
 - Uma tela de login para entrar no sistema; 
 - Uma tela para ver os dados cadastrados;  
 - Uma tela para cadastrar novas entradas de dados.

O projeto consiste em um TODO List, onde o usuário deve se cadastrar no sistema (considerar o usuário  **teste**, com a senha  **teste123**) para ter acesso a suas notas e adicionar novas notas.  _**NÃO É NECESSÁRIO REALIZAR A IMPLEMENTAÇÃO DE CADASTRO DE USUÁRIOS OU TELA/FUNCIONALIDADE DE RECUPERAÇÃO DE SENHA.**_

A imagem do banco de dados que será utilizada pode ser de qualquer banco de dados RELACIONAL. A aplicação pode ser desenvolvida em Python ou em JavaScript.


# Tecnologias utilizadas

 - HTML5;
 - Flask;
 - Docker;
 - PostgreSQL; 
 - pandas.

## Descrição do projeto

Este projeto é uma aplicação web para gerenciar notas. Está hospedado em um servidor Flask e contêinerizado com Docker. A aplicação permite que os usuários visualizem, adicionem e excluam notas. O servidor Flask conecta-se a um banco de dados PostgreSQL para armazenar as notas. 

**A imagem do docker do front-end** está disponível em: [Repositório Docker](https://hub.docker.com/repository/docker/patriciahonorato/front-notas/general) 

A do **banco** está em: [Repositório do Banco](https://hub.docker.com/repository/docker/patriciahonorato/dbnotes/general)

## Funcionalides

 -  **HTML5**: Utilizado para estruturar o conteúdo do currículo.
-   **CSS3**: Usado para estilizar o currículo.
-   **Flask**: Framework usado para criar o servidor que hospeda o currículo online.
-   **Docker**: Usado para contêinerizar o projeto, facilitando a implantação e portabilidade.
-   **PostgreSQL**: Banco de dados relacional.

## Estrutura de pastas do projeto 

Ponderada 2/
│
├── db/
│   ├── CreateDatabase.sql
│   └── Dockerfile (do db)
│
├── templates/
│   ├── index.html
│   └── notas.html
│
├── conectar_tabela.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── server.py

## Instruções de utilização

 **1. Clonar o repositório do GitHub que contém o arquivo `docker-compose.yml`:**

    ipatriciahonorato\modulo-7\Ponderada 2
    
**2. Executar o docker compose:**

    docker-compose up
    
**4. Acessar a aplicação pelo adminer:**
http://localhost:8080

**Log In:**

**1) Sistema:** Selecione "PostgreSQL".

**2) Servidor:** Digite "db" 

**3) Usuário:** Digite "postgres" 

**4) Senha:** Digite "senha"

**5) Base de dados:** Você pode deixar isso em branco ou digitar "notasdb" para se conectar diretamente ao banco de dados  especificado.

**Clique em "Login".**

**5. Para acessar a interface:**

    http://localhost
    
username: patriciahonorato
senha: #123!

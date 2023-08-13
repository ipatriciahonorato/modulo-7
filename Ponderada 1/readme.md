# Atividade 1: Criando o ambiente para a execução de uma aplicação containerizada (former: Criando uma conta em uma núvem comercial)

# Enunciado 

Este autoestudo tem por objetivo verificar se o estudante consegue criar uma aplicação e um container para executá-la. Espera-se que os estudantes possam criar suas imagens e descrever o que foi necessário para realizar seu desenvolvimento. Espera-se ainda que os estudantes possam buscar as informações complementares para o desenvolvimento da aplicação.

Os estudantes devem criar uma aplicação em Python utilizam algum framework Web (sugesre-se o Flask ou o Fastapi), para apresentar uma página HTML com o currículo do estudante. 

A aplicação deve ser containerizada e deve ser possível executá-la em um container Docker. O estudante deve descrever o que foi necessário para realizar o desenvolvimento da aplicação e containerização. O estudante deve ainda descrever como executar a aplicação em um container Docker.

O dockerfile deve conter as seguintes informações:

-   A imagem base deve ser a imagem oficial do Python (a escolha do estudante)
-   A imagem deve instalar o framework web escolhido
-   A imagem deve copiar o código fonte da aplicação para o container
-   A imagem deve expor a porta 80
-   A imagem deve executar o comando para iniciar a aplicação
-   A imagem deve estar publicada no Dockerhub


# Tecnologias utilizadas

 - HTML5;
-   CSS3;
-   Flask;
-   Docker.

## Descrição do projeto

Esse projeto é um currículo online interativo, hospedado em um servidor Flask e contêinerizado com Docker. O currículo está disponível na porta 80 e apresenta seções distintas para mostrar informações profissionais, educacionais, habilidades técnicas e prêmios e honras. Também apresenta um botão para download do arquivo no formato pdf. A imagem do docker está disponível em: [Repositório docker](https://hub.docker.com/r/patriciahonorato/resume-flask)

## Funcionalides

 -  **HTML5**: Utilizado para estruturar o conteúdo do currículo.
-   **CSS3**: Usado para estilizar o currículo.
-   **Flask**: Framework usado para criar o servidor que hospeda o currículo online.
-   **Docker**: Usado para contêinerizar o projeto, facilitando a implantação e portabilidade.

## Instruções de utilização

 **1. Baixar a imagem docker**

    docker pull patriciahonorato/resume-flask
**2. Iniciar o container:**

    docker run -d -p 80:80 patriciahonorato/resume-flask

**4. Acessar a aplicação:**
http://localhost:80

**5. Para parar o projeto:**

    docker stop [CONTAINER_ID]

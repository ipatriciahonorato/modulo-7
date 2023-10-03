# Atividade 4: Construção de Dashboard para Visualização de Dados

## Enunciado

Esta atividade tem por objetivo realizar a integração das demais atividades desenvolvidas. Ela será o frontend de visualização de dados do modelo disponibilizado. Esta interface deverá consumir os dados disponibilizados da atividade ponderada 3. O acesso a este dashboard deverá acontecer mediante ao login do usuário, conforme desenvolvido na atividade ponderada 2.

> _**IMPORTANTE 1:**_  Para está entrega, o estudante deve utilizar o framework de frontend de sua preferência. O framework deve ser justificado pelo estudante. Uma sugestão deframework para a criação do Dashboard é o Streamlit. A interface de login do usuário pode ser implementada com o próprio framework de frontend em conjunto com o FastAPI.

> _**IMPORTANTE 2:**_  Para está entrega, gravar a aplicação funcionando na infraestrutura provisionada na AWS para sua execução. Descrever qual infraestrutura foi utilizada e como ela foi provisionada.

## Padrão de qualidade

Os pontos que serão avaliados na entrega do projeto:

1.  _**(Até 2.0 ponto)**_  Publicação das Imagens para os sistemas: o sistema foi publicada corretamente na cloud (API, Modelo, Backend e Frontend);
2.  _**(Até 1.0 ponto)**_  Documentação do ambiente de de produção: documentar o ambiente de produção que foi implementado;
3.  _**(Até 3.0 ponto)**_  Construção do Dashboard: o dashboard foi construído e consome os dados da API;
4.  _**(Até 2.0 ponto)**_  Construção do Frontend: o frontend foi construído e consome os dados da API e faz o login do usuário;
5.  _**(Até 2.0 ponto)**_  As instruções no arquivo README foram suficientes para executar a aplicação: as instruções no arquivo README foram suficientes para executar a aplicação APENAS SEGUINDO OS PASSOS CONTIDOS NO DOCUMENTO;

## Visão Geral

Este projeto consiste na implementação de um Dashboard de Visualização de Dados, desenvolvido para integrar as atividades anteriores e prover uma interface de usuário interativa e segura para acesso aos dados do modelo de Machine Learning previamente desenvolvido e deployado. O front end foi construído utilizando Streamlit e é acessado mediante autenticação de login implementada via FastAPI no back end.

### Endereço do Dashboard:

[http://ec2-35-171-20-219.compute-1.amazonaws.com:8501/](http://ec2-35-171-20-219.compute-1.amazonaws.com:8501/)

### Imagens Docker:

-   FastAPI Backend: `patriciahonorato/fastapi-ponderada-4:tagname`
-   Streamlit Frontend: `patriciahonorato/streamlit-ponderada-4:tagname`

## Tecnologias Utilizadas

-   **Streamlit**
    
-   **FastAPI**
    
-   **Docker**
    
-   **AWS EC2**
    
-   **AWS S3**
    

## Arquitetura do Projeto

1.  **Frontend (Streamlit)**: Apresenta os dados e visualizações, interage com o usuário para autenticação e consulta ao modelo.
    
2.  **Backend (FastAPI)**: Gerencia a autenticação do usuário, comunica-se com o front end e provê acesso seguro ao modelo e aos dados.
    
3.  **AWS S3 Bucket**: Armazena o modelo de Machine Learning que é acessado pelo back end.
    
4.  **Docker**: Contêineres que encapsulam o front e o back end, facilitando o deploy na instância EC2 da AWS.
    

## Funcionalidades

### Frontend (Streamlit)

-   **Visualização de Dados**: Exibe visualizações interativas e informações pertinentes derivadas do modelo de ML.
    
-   **Comunicação com a API**: Envia requisições ao back end para autenticação e para recuperação de dados.
    

### Backend (FastAPI)

-   **Autenticação**: Valida as credenciais do usuário e permite/denega o acesso ao dashboard.
    
-   **API para Consumo de Dados**: Disponibiliza endpoints para recuperação de dados e interação com o modelo de ML.
    

### AWS S3

-   **Armazenamento de Modelo**: Hospeda o modelo de Machine Learning para ser acessado pelo back end quando necessário.

## Execução e Deploy

### Imagens Docker

As imagens do Docker para o frontend e backend estão disponíveis no Docker Hub:

-   [Frontend](https://hub.docker.com/r/patriciahonorato/streamlit-ponderada-4)
-   [Backend](https://hub.docker.com/r/patriciahonorato/fastapi-ponderada-4)


## Deploy na AWS
**1. Instanciação do EC2:**
- Inicie uma instância EC2 via AWS Console.
- Selecione a AMI e o tipo de instância.
- Configure detalhes e adicione regras de segurança.
- Gere e baixe a chave de acesso.
**2. Acesso e Configuração da Instância:**
- Acesse via SSH.
- Instale e inicie o Docker e Docker-Compose (se necessário).
**3. Configuração dos Contêineres Docker:**
- Realize o pull das imagens Docker desejadas.
`docker pull patriciahonorato/fastapi-ponderada-4:tagname`
`docker pull patriciahonorato/streamlit-ponderada-4:tagname`
- Utilize um arquivo docker-compose.yml para orquestrar os contêineres.
`version: '3'`
`services:`
 ` fastapi-app:`
   ` image: patriciahonorato/fastapi-ponderada-4:tagname`
    `ports:`
     ` - "8000:8000"`
  `streamlit-app:`
    `image: patriciahonorato/streamlit-ponderada-4:tagname
    ports:`
      `- "8501:8501"`
- Inicie os contêineres com docker-compose up -d.
**4. Configuração do Bucket S3:**

-   No serviço S3 no console da AWS é criado um novo bucket.
-   Nele é feito o upload do modelo treinado para o bucket criado (`heart_predict.pkl`).
-   É necessário garantir que o modelo pode ser acessado pela instância EC2 configurando as políticas de IAM e as permissões do bucket conforme necessário.

**5. Validação:**
Verifique o acesso e funcionalidade da aplicação.

## Vídeo Demonstrativo

Nesse vídeo é mostrado uma demonstração prática do funcionamento da aplicação com o modelo na instância EC2 [(link)](https://drive.google.com/file/d/1emg5a_9jbywq6z-MVN4Bv4MrnuuJJvb2/view?usp=drive_link).


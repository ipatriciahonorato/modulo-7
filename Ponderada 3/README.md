# Atividade 3: Deploy de modelo de Machine Learning na Nuvem

## Enunciado

Construção e deploy de um modelo de predição ou classificação criados pelos alunos. Este modelo deve ser deployado em uma nuvem comercial e uma API de acesso a ele deve ser desenvolvida.

> _**IMPORTANTE 1:**_  Para está entrega, não é necessário construir uma interface de usuário para o modelo, como um frontend. Apenas a API de acesso ao modelo deve ser desenvolvida.

_**IMPORTANTE 2:**_  Para está entrega, dois pontos são obrigatórios:

1.  A utilização do Python com o FastAPI para realizar a construção da API;
2.  O deploy com o imagens de containers no DockerHub.

O estudante deve escolher um conjunto de dados dentre os relacionados abaixo. Qualquer conjunto diferente destes deve ser aprovado pelo professor. Toda a manipulação realizada com os dados deve ser descrita na documentação do projeto.

O conjunto de dados escolhido deve ser utilizado para a construção de um modelo de predição ou classificação. O modelo deve ser construído utilizando o Python e o framework de Machine Learning de preferência do estudante. A escolha do modelo deve ser justificada pelo estudante.

O ambiente de desenvolvimento deve ser documentado, assim como o ambiente de produção. Um video deve ser gravado apresentado o processo de utilização do modelo em produção.

> _**IMPORTANTE:**_  Depois de gravado o comportamento do projeto em produção, o estudante deve remover os recursos alocados na nuvem comercial. Apenas o vídeo será utilizado para a avaliação do projeto, em conjunto com os códigos fontes desenvolvidos.

## [](https://github.com/Murilo-ZC/Questoes-Trabalho-Inteli-M7/tree/main/ponderada3#padr%C3%A3o-de-qualidade)Padrão de qualidade

Os pontos que serão avaliados na entrega do projeto:

1.  _**(Até 1.0 ponto)**_  Construção do dockerfile: o arquivo contem todas as informações necessárias para a construção da imagem dos containers para produção;
2.  _**(Até 1.0 ponto)**_  Publicação das Imagens para a API: a API foi publicada corretamente na cloud;
3.  _**(Até 1.0 ponto)**_  Documentação do ambiente de desenvolvimento: documentar o ambiente de desenvolvimento (não precisa estar dockerizado), seus requisitos e como executar o projeto. Exportar os notebooks temporários que foram utilizados em seu desenvolvimento;
4.  _**(Até 1.0 ponto)**_  Documentação da API e seu funcionamento;
5.  _**(Até 1.0 ponto)**_  Descrever qual modelo de Machine Learning foi escolhido e justificar sua escolha: essa justificativa pode vir da comparação entre diversos modelos que foram previamente aplicados;
6.  _**(Até 1.0 ponto)**_  As instruções no arquivo README foram suficientes para executar a aplicação: as instruções no arquivo README foram suficientes para executar a aplicação APENAS SEGUINDO OS PASSOS CONTIDOS NO DOCUMENTO;
7.  _**(Até 2.0 pontos)**_  Treinamento do modelo;
8.  _**(Até 2.0 pontos)**_  Pré-processamento dos dados;

## Descrição do projeto

Este projeto utiliza um modelo de Machine Learning para prever a condição do tratamento de doenças cardíacas. Ele foi desenvolvido no Google Colab e posteriormente transferido para um ambiente virtual em Python no formato pkl. O modelo foi escolhido após um processo de seleção com a biblioteca Pycaret e deployado usando FastAPI. A API está contêinerizada com Docker e hospedada em uma instância EC2 da AWS.

A imagem do docker do projeto está disponível em: [Repositório Docker](https://hub.docker.com/repository/docker/patriciahonorato/deploy-modelo-heart-predict/general)

### Tecnologias utilizadas

-   Python;
-   FastAPI;
-   Pycaret;
-   Docker;
-   AWS EC2.
### Funcionalidades

-   **Python**: Linguagem de programação principal.
-   **FastAPI**: Framework web utilizado para desenvolver a API.
-   **Pycaret**: Biblioteca de Machine Learning usada para treinar, testar e selecionar o modelo.
-   **Docker**: Usado para contêinerizar o projeto.
-   **AWS EC2**: Serviço de cloud utilizado para hospedar a API.

## Descrição e Justificativa do Modelo de Machine Learning
O modelo de Machine Learning escolhido para este projeto foi o Logistic Regression. A escolha deste modelo foi baseada em vários fatores:

**- Comparação entre Modelos:** Durante a fase inicial do projeto, vários modelos foram testados usando a biblioteca Pycaret. Esta biblioteca testa diversos modelos e compara suas métricas. O modelo de regressão logística destacou-se com uma acurácia de 0.8362 e AUC de 0.8914.

**- Interpretabilidade:** O modelo de regressão logística oferece uma interpretação clara dos pesos associados a cada recurso, o que pode ser útil para entender a importância relativa das características no contexto de doenças cardíacas.

**- Velocidade:** Em comparação com modelos mais complexos, como redes neurais ou ensembles avançados, a regressão logística tende a ser mais rápida e exige menos recursos computacionais, tornando-a adequada para deployment.

### Pré-processamento dos Dados
No contexto deste projeto, os seguintes passos para pré processamento dos dados foram realizados:

**- Tratamento de Valores Faltantes:** Antes de qualquer processamento adicional, o conjunto de dados foi examinado para valores faltantes usando df.isnull().sum(). Essa etapa é fundamental para garantir que não estamos alimentando valores ausentes no modelo, o que pode levar a resultados imprecisos.

**- Conversão de Variáveis Categóricas:** As colunas categóricas, como 'sex', 'cp', entre outras, foram convertidas para o tipo 'category'. Isso facilita a codificação destas colunas mais tarde e também melhora a eficiência do modelo, pois ele não terá que lidar com valores de texto.

**- Escalonamento de Variáveis Numéricas:** Para garantir que todas as características numéricas estejam na mesma escala e para melhorar a convergência do modelo, as variáveis numéricas foram padronizadas usando o StandardScaler do scikit-learn. Isso significa que cada recurso terá uma média de 0 e um desvio padrão de 1.

## Estrutura de pastas do projeto

    Ponderada 3/
    ├── app/
    │   └── models/
    │       └── modelo.pkl
    │   └── main.py
    ├── Dockerfile
    ├── dockerignore
    ├── requirements.txt
    └── logs.log

## Instruções de utilização

**1.  Clonar o repositório do GitHub que contém o arquivo Dockerfile e demais componentes:**

    `git clone ipatriciahonorato/modulo7/tree/main/Ponderada%203`
   

**2.  Puxar a imagem Docker Hub:**

   `docker pull patriciahonorato/deploy-modelo-heart-predict`

**3.  Acessar a API pelo link:**

[http://ec2-184-73-91-169.compute-1.amazonaws.com/docs](http://ec2-184-73-91-169.compute-1.amazonaws.com/docs)

(**Observação:** o deploy da API foi feita nesse link mas conforme as instruções da atividade, após a gravação do vídeo a API foi excluída da nuvem.)

## Vídeo de demonstração de funcionamento do projeto

[Link do video no Google Drive](https://drive.google.com/file/d/1FUuOb9ZGqrjV-6_IHeKmp3zZMEbWdDt8/view?usp=sharing)

### Referências

[Dataset do Kaggle de Heart Disease Cleveland UCI](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)

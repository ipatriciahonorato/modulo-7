# Use a versão oficial do PostgreSQL como base
FROM postgres:13

# Defina variáveis de ambiente para a senha do usuário 'postgres' e o nome do banco de dados
# Estas são variáveis padrão reconhecidas pelo container do PostgreSQL
ENV POSTGRES_PASSWORD=senha
ENV POSTGRES_DB=notasdb

# Copie o script SQL para a pasta de inicialização do container
COPY CreateDatabase.sql /docker-entrypoint-initdb.d/

# O ponto de entrada e o comando são herdados da imagem base do PostgreSQL,
# então não precisamos especificá-los. Eles cuidarão da inicialização do banco de dados e da execução do script.

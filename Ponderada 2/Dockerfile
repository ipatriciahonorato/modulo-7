# Use uma imagem base do Python 3.8
FROM python:3.8-slim

# Instale dependências necessárias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Defina uma pasta de trabalho
WORKDIR /app

# Copie os requisitos do aplicativo para o contêiner
COPY requirements.txt .

# Instale os requisitos do aplicativo
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código e templates para o contêiner
COPY . .

# Defina a porta em que o aplicativo será executado
EXPOSE 5000

# Comando para iniciar o aplicativo
CMD ["python", "server.py"]

-- CreateDatabase.sql

-- Cria a tabela 'notas'
CREATE TABLE notas (
    id SERIAL PRIMARY KEY,       -- ID automático e chave primária
    titulo VARCHAR(255) NOT NULL,     -- Título da nota
    descricao TEXT NOT NULL           -- Descrição ou corpo da nota
);

-- Inserir dados iniciais (opcional)
INSERT INTO notas (titulo, descricao) VALUES ('Exemplo Nota 1', 'Esta é a descrição da nota 1.');
INSERT INTO notas (titulo, descricao) VALUES ('Exemplo Nota 2', 'Esta é a descrição da nota 2.');

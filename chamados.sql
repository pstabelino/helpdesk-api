CREATE TABLE chamados (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    status VARCHAR(50) NOT NULL
        CHECK (status IN ('aberto', 'em andamento', 'fechado')),
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO chamados (titulo, status)
VALUES
    ('Erro na integração', 'aberto'),
    ('Dashboard não atualiza', 'em andamento');
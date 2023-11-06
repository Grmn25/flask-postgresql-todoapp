instructions = [
    "SET CONSTRAINTS ALL DEFERRED;",
    "DROP TABLE IF EXISTS todo;",
    "DROP TABLE IF EXISTS usuario;",
    "SET CONSTRAINTS ALL IMMEDIATE;",
    """
        CREATE TABLE usuario(
            usuario_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(250) NOT NULL
        );
    """,
    """
        CREATE TABLE todo(
            todo_id SERIAL PRIMARY KEY,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            created_by INT REFERENCES usuario(usuario_id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
]

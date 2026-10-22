from banco import conectar
from typing import Literal



def listar_chamados_repo(status: Literal["aberto", "em andamento", "fechado"] | None = None):
    with conectar() as conexao:
        with conexao.cursor() as cursor:

            if status is not None:
                cursor.execute(
                    """
                    SELECT id, titulo, status
                    FROM chamados
                    WHERE status = %s
                    """,
                    (status,)
                )
            else:
                cursor.execute("""
                    SELECT id, titulo, status
                    FROM chamados
                """)

            chamados = cursor.fetchall()

    return chamados


def buscar_chamado_repo(chamado_id: int):
    with conectar() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute("""
                SELECT id, titulo, status
                FROM chamados
                WHERE id = %s;
                """,
                (chamado_id,)
            )

            chamado = cursor.fetchone()

    return chamado


def criar_chamado_repo(titulo: str, status: str):
    with conectar() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute("""
                INSERT INTO chamados (titulo, status)
                VALUES (%s, %s)
                RETURNING id, titulo, status, criado_em;
                """,
                (titulo, status)
            )

            chamado = cursor.fetchone()

    return chamado


def atualizar_chamado_repo(chamado_id: int, titulo: str | None, status: str | None):
    with conectar() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute("""
                UPDATE chamados
                SET
                    titulo = COALESCE(%s, titulo),
                    status = COALESCE(%s, status)
                WHERE id = %s
                RETURNING id, titulo, status, criado_em;
                """,
                (titulo, status, chamado_id)
            )

            chamado = cursor.fetchone()

    return chamado


def excluir_chamado_repo(chamado_id: int):
    with conectar() as conexao:
        with conexao.cursor() as cursor:

            cursor.execute(
                """
                DELETE FROM chamados
                WHERE id = %s
                RETURNING id, titulo, status;
                """,
                (chamado_id,)
            )

            chamado = cursor.fetchone()

    return chamado
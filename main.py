from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
from repositorios import listar_chamados_repo, criar_chamado_repo, buscar_chamado_repo, atualizar_chamado_repo, excluir_chamado_repo


app = FastAPI()


class ChamadoCriacao(BaseModel):
    titulo: str
    status: Literal["aberto", "em andamento", "fechado"]


class ChamadoAtualizacao(BaseModel):
    titulo: str | None = None
    status: Literal["aberto", "em andamento", "fechado"] | None = None


@app.get("/")
def inicio():
    return {
        "mensagem": "HelpDesk API funcionando"
    }


@app.get("/chamados")
def listar_chamados(status: Literal["aberto", "em andamento", "fechado"] | None = None):
    
    chamados = listar_chamados_repo(status)
    
    return chamados


@app.get("/chamados/{chamado_id}")
def buscar_chamado(chamado_id: int):
    
    chamado = buscar_chamado_repo(chamado_id)

    if chamado is None:

        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )
    
    return chamado


@app.post("/chamados", status_code=201)
def criar_chamado(novo_chamado: ChamadoCriacao):

    chamado = criar_chamado_repo(novo_chamado.titulo, novo_chamado.status)

    return chamado


@app.patch("/chamados/{chamado_id}")
def atualizar_chamado(chamado_id: int, dados: ChamadoAtualizacao):
    
    chamado = atualizar_chamado_repo(chamado_id, dados.titulo, dados.status)

    if chamado is None:
    
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    return chamado


@app.delete("/chamados/{chamado_id}")
def excluir_chamado(chamado_id: int):

    chamado = excluir_chamado_repo(chamado_id)

    if chamado is None:

        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )
            
    return {"mensagem": "Chamado excluído com sucesso"}
    
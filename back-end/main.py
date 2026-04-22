from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
usuarios = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

@app.post("/criar-usuario")
def criar_usuario(novo_usuario: Usuario):
    for usuario in usuarios:
        if novo_usuario.id == usuario.id:
            return {"erro": f"Já existe usuário com ID {novo_usuario.id}."}
        elif novo_usuario.email == usuario.email:
            return {"erro": f"Já existe usuário com Email {novo_usuario.email}"}

    usuarios.append(novo_usuario)
    return {"mensagem": f"Usuário {novo_usuario.id} adicionado com sucesso."}

@app.get("/resgatar-usuario/{id}")
def resgatar_usuario(id: int):
    for usuario in usuarios:
        if id == usuario.id:
            return usuario
    return {"erro": f"Usuário de ID {id} não encontrado."}
        
@app.get("/resgatar-todos-usuarios")
def resgatar_todos_usuario():
    return usuarios

@app.put("/editar-usuario/{id}")
def editar_usuario(id: int, usuario_editado: Usuario):
    for i, usuario in enumerate(usuarios):
        if id == usuario.id:
            if usuario_editado.id != usuario.id:
                return {"erro": f"ID não pode ser alterado"}
            for usuario in usuarios:
                if usuario_editado.email == usuario.email:
                    return {"erro": "Esse email já está sendo utilizado."}
            usuarios[i] = usuario_editado
            return {"mensagem": f"Usuário {usuario_editado.id} editado com sucesso."}
    return {"erro": f"Usuário não encontrado"}

@app.delete("/deletar-usuario/{id}")
def deletar_usuario(id: int):
    for usuario in usuarios:
        if id == usuario.id:
            usuarios.remove(usuario)
            return {"mensagem": f"Usuário deletado com sucesso"}
    return {"erro": f"Usuário de ID {id} não encontrado"}

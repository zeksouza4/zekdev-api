from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# === CONFIGURAÇÃO DO CORS ===
origins = ["*"]  # "*" libera para qualquer frontend. Para mais segurança, coloca a URL do seu site.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ============================

# Suas rotas
@app.post("/cadastro")
def cadastro(email: str, senha: str):
    # lógica de cadastro
    return {"msg": "Usuário cadastrado com sucesso"}

@app.post("/login")
def login(email: str, senha: str):
    # lógica de login
    return {"access_token": "token_exemplo"}
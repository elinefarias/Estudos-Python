from fastapi import FastAPI

app = FastAPI()

vendas = {
  1: {"item":"lata", "preco-unitario":4, "quantidade":5},
  2: {"item":"garrafa 2L", "preco-unitario":15, "quantidade":5},
  3: {"item":"garrafa 750mL", "preco-unitario":10, "quantidade":5},
  4: {"item":"lata mini", "preco-unitario":2, "quantidade":5},
}

@app.get("/")
def home():
    #return "Hello World!!"
    #return len(vendas)
    return {"vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_vendas(id_venda: int):
  if id_venda in vendas:
      return vendas[id_venda]
  else:
      return {"erro": "venda não encontrada"}
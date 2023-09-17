from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dataclasses import asdict
import sqlite3

app = FastAPI()

# Classe para representar a consulta de pesquisa
class SearchQuery(BaseModel):
    query: str


# Classe para representar a lista de consultas
class SearchQueryList(BaseModel):
    queries: list[SearchQuery]


# Rota para pesquisa genérica
@app.post("/api/search")
async def search(query: SearchQuery):
    # Realize a pesquisa no banco de dados SQLite com base na consulta
    # Substitua esta parte com sua lógica de pesquisa real
    results = []  # Armazene os resultados da pesquisa aqui
    return {"consult": query.query, "statusCode": 200, "content": results}

# Rota para pesquisa específica (filme, série, etc.)
@app.post("/api/search/{media_type}")
async def search_media_type(media_type: str, query: SearchQuery):
    # Realize a pesquisa no banco de dados SQLite com base no tipo de mídia e consulta
    # Substitua esta parte com sua lógica de pesquisa real
    results = []  # Armazene os resultados da pesquisa aqui
    return {"consult": query.query, "statusCode": 200, "content": results}

# Rota para pesquisa e adição de dados
@app.post("/api/sync_database")
async def search_and_add(queries: SearchQueryList):
    results = []
    
    # Realize a pesquisa para cada consulta na lista
    for query in queries.queries:
        # Substitua esta parte com sua lógica de pesquisa real
        # Aqui, estamos apenas simulando resultados fictícios
        results.append({"query": query.query, "results": []})
    
    # Insira os resultados no banco de dados SQLite
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    for result in results:
        for item in result["results"]:
            # Converta o objeto (por exemplo, Movie) para um dicionário antes de inserir no banco de dados
            item_dict = asdict(item)
            
            # Insira os dados no banco de dados SQLite
            # Substitua esta parte com sua lógica de inserção real
            cursor.execute("INSERT INTO movies (...) VALUES (...)")  # Exemplo para filmes
            
    conn.commit()
    conn.close()
    
    return {"message": "Search and add completed successfully", "results": results}


# Rota para adicionar dados ao banco de dados
@app.post("/api/add_data")
async def add_data(data: Movie):
    # Converta o objeto Movie para um dicionário antes de inserir no banco de dados
    data_dict = asdict(data)
    
    # Insira os dados no banco de dados SQLite
    # Substitua esta parte com sua lógica de inserção real
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (...) VALUES (...)")
    conn.commit()
    conn.close()
    
    return {"message": "Data added successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

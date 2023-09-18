from nicegui import app
from dataclasses import asdict
import sqlite3


from pytrarr.utils.dataclass import (
    MediaContent,
    ApiResponse,
    SearchQuery,
    SearchQueryList,
    MediaType,
)

from pytrarr.models.models import (
    add_content_in_database
)


# Rota para pesquisa genérica
@app.post(
    "/api/search"
)
async def search(
        query: SearchQuery,
        media_type: MediaType,
    ):
    results = []  # Armazene os resultados da pesquisa aqui
    return ApiResponse(query=query.query, statusCode=200, content=results)


# Rota para pesquisa e adição de dados
@app.post(
    "/api/sync_database"
)
async def search_and_add(
    queries: SearchQueryList
    ):
    results = []
    # Realize a pesquisa para cada consulta na lista
    for query in queries.queries:
        ...

    # Insira os resultados no banco de dados SQLite
    # add_content_in_database()
    
    return ApiResponse(message="Search and add completed successfully", statusCode=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

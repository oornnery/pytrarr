from httpx import AsyncClient
from rich.console import Console

console = Console()

class SearchTorrent:
    ...

class TMDB():
    API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2NzQwY2NjMjRlYjlkMzQ5NjJmNWQyMjM0MTBmZDEzYyIsInN1YiI6IjY1MTVhZGZhMDQ5OWYyMDBlMWM2N2U1ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VaPVndSOWt8LtDjJBp_QteXTVowBuklQCpNgjGJ3KZY'
    URL_BASE = "https://api.themoviedb.org/3"

    def __init__(self, 
            language: str = "pt-BR", # pt-BR, en-US
            include_adult: bool = False,
        ) -> None:
        self.language = language
        self.include_adult = include_adult

        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self.API_KEY
        }

        self.client = AsyncClient(
            headers=self.headers,
            base_url=self.URL_BASE
        )

    async def authentication(self):
        r = await self.client.get(
            url='/authentication',
        )
        console.log(r.json())
        return r.json()

    async def search(self, 
        query: str,
        page: int = 1,
        ) -> dict:
        path = '/search/multi'
        params = {
            'query': query,
            'language': self.language,
            'page': page,
            'include_adult': self.include_adult
        }
        r = await self.client.get(url=path, params=params)
        console.log(f'[yellow1]Request:[/yellow1] {r.url} - [yellow1]Status Code:[/yellow1] {r.status_code}')
        return r.json()

    async def search_movie(self, 
        query: str,
        region: str = '',
        primary_release_year: str = '',
        year: str = '',
        page: int = 1,
        ) -> dict:
        path = '/search/multi'
        params = {
            'query': query,
            'language': self.language,
            'region': region,
            'primary_release_year': primary_release_year,
            'year': year,
            'page': page,
            'include_adult': self.include_adult
        }
        r = await self.client.get(url=path, params=params)
        console.log(f'[yellow1]Request:[/yellow1] {r.url} - [yellow1]Status Code:[/yellow1] {r.status_code}')
        return r.json()

    async def search_tv(self, 
        query: str,
        first_air_date_year: str = '',
        year: str = '',
        page: int = 1,
        ) -> dict:
        path = '/search/multi'
        params = {
            'query': query,
            'language': self.language,
            'first_air_date_year': first_air_date_year,
            'year': year,
            'page': page,
            'include_adult': self.include_adult
        }
        r = await self.client.get(url=path, params=params)
        console.log(f'[yellow1]Request:[/yellow1] {r.url} - [yellow1]Status Code:[/yellow1] {r.status_code}')
        return r.json()

    def banner(self,
            path: str,
            size: str = 'w500'
        ):
        return f'https://image.tmdb.org/t/p/{size}/{path}'


if '__main__' == __name__:
    import asyncio
    async def tests():
        c = TMDB()
        await c.authentication()
        q = await c.search('Matrix')
        console.print(q)
        

    asyncio.run(tests())
    
    

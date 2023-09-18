from dataclasses import dataclass, field
from email import message
from pydantic import BaseModel
from typing import List

@dataclass
class SearchTorrent:
    title: str
    original_title: str
    year: str
    genres: list[str]
    language: list[str]
    subtitles: list[str]
    video_format: str
    video_quality: str
    video_size: str
    duration: str
    torrent: str

@dataclass
class Torrent:
    languages: List[str] = field(default_factory=list)
    subtitles: List[str] = field(default_factory=list)
    size: str = field(default_factory=str)
    video_format: str = field(default_factory=str)
    quality: str = field(default_factory=str)
    quality_video: str = field(default_factory=str)
    quality_audio: str = field(default_factory=str)
    info_hash: str = field(default_factory=str)
    file_content: str = field(default_factory=str)


@dataclass
class Episode:
    title: str = field(default_factory=str)
    season_number: str = field(default_factory=str)
    episode_number: str = field(default_factory=str)
    duration: str = field(default_factory=str)
    size: str = field(default_factory=str)
    links: List[Torrent] = field(default_factory=list)


@dataclass
class Season:
    season_number: str = field(default_factory=str)
    episodes: List[Episode] = field(default_factory=list)


@dataclass
class MediaContent:
    title: str = ""
    genres: List[str] = field(default_factory=list)
    poster: List[str] = field(default_factory=list)
    uploaded: str = field(default_factory=str)
    release_date: str = field(default_factory=str)
    duration: str = field(default_factory=str)
    size: str = field(default_factory=str)
    imdb: str = field(default_factory=str)
    last_update: str = field(default_factory=str)
    seasons: List[Season] = field(default_factory=list)
    links: List[Torrent] = field(default_factory=list)


@dataclass
class ApiResponse:
    query: str = field(default_factory=str)
    statusCode: int = field(default_factory=int)
    statusName: str = field(default_factory=str)
    message: str = field(default_factory=str)
    content: List[MediaContent] = field(default_factory=list[MediaContent])

# Classe para representar a consulta de pesquisa
class SearchQuery(BaseModel):
    query: str


# Classe para representar a lista de consultas
class SearchQueryList(BaseModel):
    queries: List[SearchQuery]

class MediaType(BaseModel):
    media_type: list[str]


from rich.console import Console

console = Console()

console.print(MediaContent())
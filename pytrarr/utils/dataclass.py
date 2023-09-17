from dataclasses import dataclass
from typing import List

@dataclass
class Movie:
    title: str
    poster: List[str]
    release_date: str
    uploaded: str
    genres: List[str]
    languages: List[str]
    duration: str
    quality: List[str]
    audio: str
    video: str
    format: List[str]
    size: str
    subtitles: List[str]
    imdb: str
    last_update: str
    links: List['Tracker']

@dataclass
class Series:
    title: str
    poster: List[str]
    release_date: str
    uploaded: str
    genres: List[str]
    languages: List[str]
    duration: str
    quality: List[str]
    seasons: List['Season']
    audio: str
    video: str
    format: List[str]
    size: str
    subtitles: List[str]
    imdb: str
    last_update: str
    links: List['Tracker']

@dataclass
class Tracker:
    size: str
    info_hash: str
    file_content: str

@dataclass
class Season:
    season_number: str
    episodes: List['Episode']

@dataclass
class Episode:
    episode_number: str
    title: str
    duration: str

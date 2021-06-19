import aiohttp


# defining config objects

class Config:
    DEBUG = None
    SESSION = None
    KITSU_URLS  = {
        "TRENDING_ANIME" : "https://kitsu.io/api/edge/trending/anime",
        "TRENDING_MANGA" : "https://kitsu.io/api/edge/trending/manga",
        "BASE_ANIME" : "https://kitsu.io/api/edge/anime/{}",
        "BASE_MANGA" : "https://kitsu.io/api/edge/manga/{}"
    }


class Development(Config):
    DEBUG = True



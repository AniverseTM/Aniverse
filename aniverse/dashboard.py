from quart import Blueprint, current_app, render_template
from aiohttp import ClientSession # type hinting type: ignore
bp = Blueprint("dashboard", __name__)

@bp.route("/dashboard")
async def dashboard():
    session = current_app.client_session
    urls = current_app.config["KITSU_URLS"]
    async with session.get(urls["TRENDING_ANIME"]) as anime_resp:
        anime_json = await anime_resp.json()
    async with session.get(urls["TRENDING_MANGA"]) as manga_resp:
        manga_json = await manga_resp.json()
    print(anime_json)
    print(manga_json)
    trending_anime = anime_json.get("data")
    trending_manga = manga_json.get("data")
    pta = []
    ptm = []
    for anime in trending_anime:
        _id = anime.get("id")
        attrs = anime.get("attributes")
        title = attrs.get("canonicalTitle")
        image = attrs.get("posterImage").get("large")
        episode_count = attrs.get("episodeCount") or "Unlisted"
        aobj_url = anime.get("links").get("self")
        data = {
            "title" : title,
            "image" : image,
            "episodeCount" : episode_count,
            "url" : "https://kitsu.io" + aobj_url,
            "id" : _id
        }
        pta.append(data)

    for manga in trending_manga:
        _id = manga.get("id")
        attrs = manga.get("attributes")
        title = attrs.get("canonicalTitle")
        image = attrs.get("posterImage").get("large")
        episode_count = attrs.get("chapterCount") or "Unlisted"
        mobj_url = manga.get("links").get("self")
        data = {
            "title" : title,
            "image" : image,
            "chapterCount" : episode_count,
            "url" : "https://kitsu.io" + mobj_url,
            "id" : _id
        }
        ptm.append(data)

    ctx = {
        "trendingAnime" : pta[:6],
        "trendingManga" : ptm[:6]
    }
    return await render_template("dashboard.html", **ctx)
from quart import Blueprint, current_app, render_template
from aiohttp import ClientSession # type hinting
from . import utils
bp = Blueprint("subpoints", __name__)

@bp.route("/anime/<anime_id>")
async def anime_dash(anime_id: int):
    session: ClientSession = current_app.client_session
    urls = current_app.config["KITSU_URLS"]
    url = urls["BASE_ANIME"].format(str(anime_id))
    async with session.get(url) as resp:
        data = await resp.json()
    data = data.get("data")
    attrs = data.get("attributes")
    description = attrs.get("description")
    title = attrs.get("canonicalTitle")
    cover_image = attrs.get("coverImage").get("large")
    poster_image = attrs.get("posterImage").get("large")
    trailer_link = attrs.get("youtubeVideoId")
    favourites = attrs.get("favoritesCount")
    rank = attrs.get("ratingRank")
    rating = attrs.get("averageRating")
    context = {
        "name" : utils.strip_to_len(title, 25),
        "cover_image" : cover_image,
        "description" : description,
        "poster_image" : poster_image,
        "trailer_link" : trailer_link,
        "favourites" : favourites,
        "rank" : rank,
        "rating" : rating
    }
    return await render_template("anime.view.html", **context)

@bp.route("/manga/<manga_id>")
async def manga_dash(manga_id: int):
    session: ClientSession = current_app.client_session
    urls = current_app.config["KITSU_URLS"]
    url = urls["BASE_MANGA"].format(str(manga_id))
    async with session.get(url) as resp:
        data = await resp.json()
    data = data.get("data")
    attrs = data.get("attributes")
    description = attrs.get("description")
    title = attrs.get("canonicalTitle")
    cover_image = attrs.get("coverImage").get("large")
    poster_image = attrs.get("posterImage").get("large")
    trailer_link = attrs.get("youtubeVideoId")
    favourites = attrs.get("favoritesCount")
    rank = attrs.get("ratingRank")
    rating = attrs.get("averageRating")
    context = {
        "name" : utils.strip_to_len(title, 25),
        "cover_image" : cover_image,
        "description" : description,
        "poster_image" : poster_image,
        "trailer_link" : trailer_link,
        "favourites" : favourites,
        "rank" : rank,
        "rating" : rating
    }
    return await render_template("manga.view.html", **context)
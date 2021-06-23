from quart import Blueprint, current_app, render_template, request
from . import utils

bp = Blueprint("searchpoints", __name__)

@bp.route("/anime", methods = ["GET", "PATCH"])
async def sp_anime():
    session = current_app.client_session
    if request.args.get("query") is None:
        urls = current_app.config["KITSU_URLS"]
        async with session.get(urls["TRENDING_ANIME"] + "?limit=12") as resp:
            print(resp.real_url)
            anime_json = await resp.json()
        pta = []
        trending_anime = anime_json.get("data")
        for anime in trending_anime:
            _id = anime.get("id")
            attrs = anime.get("attributes")
            title = attrs.get("canonicalTitle")
            image = attrs.get("posterImage").get("large")
            episode_count = attrs.get("episodeCount") or "Unlisted"
            aobj_url = anime.get("links").get("self")
            data = {
                "title" : utils.strip_to_len(title, 25),
                "image" : image,
                "episodeCount" : episode_count,
                "url" : "https://kitsu.io" + aobj_url,
                "id" : _id
            }
            pta.append(data)

        context = {
            "givenData": pta
        }
        return await render_template("anime.search.html", **context)
    else:
        query = request.args.get("query")
        query = query.replace("+", "%20")
        query = query.replace(" ", "%20")
        session = current_app.client_session
        urls = current_app.config["KITSU_URLS"]
        base_url = urls["BASE_ANIME"][:-3]
        async with session.get(base_url+ f"?filter[text]={query}&page[limit]=12") as resp:
            print(resp.real_url)
            anime_json = await resp.json()
            print(anime_json)
        pta = []
        trending_anime = anime_json.get("data")
        for anime in trending_anime:
            _id = anime.get("id")
            attrs = anime.get("attributes")
            title = attrs.get("canonicalTitle")
            image = attrs.get("posterImage").get("large")
            episode_count = attrs.get("episodeCount") or "Unlisted"
            aobj_url = anime.get("links").get("self")
            data = {
                "title" : utils.strip_to_len(title, 25),
                "image" : image,
                "episodeCount" : episode_count,
                "url" : "https://kitsu.io" + aobj_url,
                "id" : _id
            }
            pta.append(data)

        context = {
            "givenData": pta
        }
        return await render_template("anime.search.html", **context)


@bp.route("/manga", methods = ["GET", "PATCH"])
async def sp_manga():
    session = current_app.client_session
    if request.args.get("query") is None:
        urls = current_app.config["KITSU_URLS"]
        async with session.get(urls["TRENDING_MANGA"] + "?limit=12") as resp:
            print(resp.real_url)
            anime_json = await resp.json()
        pta = []
        trending_anime = anime_json.get("data")
        for anime in trending_anime:
            _id = anime.get("id")
            attrs = anime.get("attributes")
            title = attrs.get("canonicalTitle")
            image = attrs.get("posterImage").get("large")
            episode_count = attrs.get("episodeCount") or "Unlisted"
            aobj_url = anime.get("links").get("self")
            data = {
                "title" : utils.strip_to_len(title, 25),
                "image" : image,
                "episodeCount" : episode_count,
                "url" : "https://kitsu.io" + aobj_url,
                "id" : _id
            }
            pta.append(data)

        context = {
            "givenData": pta
        }
        return await render_template("anime.search.html", **context)
    else:
        query = request.args.get("query")
        query = query.replace("+", "%20")
        query = query.replace(" ", "%20")
        session = current_app.client_session
        urls = current_app.config["KITSU_URLS"]
        base_url = urls["BASE_MANGA"][:-3]
        async with session.get(base_url+ f"?filter[text]={query}&page[limit]=12") as resp:
            print(resp.real_url)
            anime_json = await resp.json()
            print(anime_json)
        pta = []
        trending_anime = anime_json.get("data")
        for anime in trending_anime:
            _id = anime.get("id")
            attrs = anime.get("attributes")
            title = attrs.get("canonicalTitle")
            image = attrs.get("posterImage").get("large")
            episode_count = attrs.get("episodeCount") or "Unlisted"
            aobj_url = anime.get("links").get("self")
            data = {
                "title" : utils.strip_to_len(title, 25),
                "image" : image,
                "episodeCount" : episode_count,
                "url" : "https://kitsu.io" + aobj_url,
                "id" : _id
            }
            pta.append(data)

        context = {
            "givenData": pta
        }
        return await render_template("manga.search.html", **context)
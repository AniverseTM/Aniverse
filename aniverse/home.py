from quart import Blueprint, render_template

bp = Blueprint("home", __name__)


@bp.route("/")
async def home():
    return await render_template("home.html")
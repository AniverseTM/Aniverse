from quart import Quart
from .config import Development
from . import home, dashboard, subpoints, searchpoints



BLUEPRINTS = [
    home.bp,
    dashboard.bp, 
    subpoints.bp,
    searchpoints.bp
]

def create_app(mode = Development) -> Quart:
    app = Quart(__name__)
    app.config.from_object(mode)
    for bp in BLUEPRINTS:
        app.register_blueprint(bp)
    return app











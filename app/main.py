from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar import Litestar

from app.config.alchemy import alchemy_config
from app.controllers.user import UserController
from app.middleware.exceptions import exception_handlers

app = Litestar(
    route_handlers=[UserController],
    plugins=[SQLAlchemyPlugin(config=alchemy_config)],
    exception_handlers=exception_handlers,
    debug=False,
)

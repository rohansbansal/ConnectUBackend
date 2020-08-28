from flask import request
from app.dao.connections_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *


class GetConnectionsController(ConnectUController):
    def get_path(self):
        return "/"

    def get_methods(self):
        return ["GET"]

    def content(self, **kwargs):
        try:
            user_id = request.args["user_id"]
        except Exception:
            raise HTTPException(msg="No user id supplied.", response_code=400)
        connections = get_connections_by_id(user_id)
        if not connections:
            raise HTTPException(msg="No connections with that id.", response_code=400)
        return connections
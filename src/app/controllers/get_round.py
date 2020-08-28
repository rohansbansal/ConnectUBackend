from flask import request
from app.dao.round_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *

class GetRoundController(ConnectUController):
    def get_path(self):
        return "/"
    def get_methods(self):
        return ["GET"]
    def content(self, **kwargs):
        try:
            user_id = request.args["user_id"]
        except Exception:
            raise HTTPException(msg="No user id supplied.", response_code=400)
        rounds = find_round_by_id(user_id)
        if not rounds:
            raise HTTPException(msg="No rounds with that id.", response_code=400)
        return rounds
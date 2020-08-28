from flask import Blueprint, request, session
from app.dao.round_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *

class GetRoundPairingController(ConnectUController):
    def get_path(self):
        return "/pairing/"
    def get_methods(self):
        return ["GET"]
    def get_successful_response_code(self):
        return 201
    def content(self, **kwargs):
        try:
            user_id = request.args["user_id"]
        except Exception:
            raise HTTPException(msg="No user id supplied.", response_code=400)
        round_pairings = find_round_pairing_by_id(user_id)
        if not round_pairings:
            raise HTTPException(msg="No round pairings with that id.", response_code=400)
        return round_pairings
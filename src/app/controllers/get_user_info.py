from flask import request
from app.dao.users_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *
import app.utils.google_auth as google_auth


class GetUserInfoController(ConnectUController):
    def get_path(self):
        return "/info/"

    def get_methods(self):
        return ["GET"]

    def content(self, **kwargs):
        try:
            user_id = request.args["user_id"]
        except Exception:
            raise HTTPException(msg="No user id supplied.", response_code=400)
        user = find_user_by_id(user_id)
        if not user:
            raise HTTPException(msg="No user account with that id.", response_code=400)
        return user

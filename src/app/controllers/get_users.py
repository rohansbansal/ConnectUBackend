from flask import request
from app.dao.users_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *
import app.utils.google_auth as google_auth


class GetUsersController(ConnectUController):
    def get_path(self):
        return "/users/"

    def get_methods(self):
        return ["GET"]

    def content(self, **kwargs):
        try:
            users = get_all_users()
        except Exception:
            raise HTTPException(msg="No merchants", response_code=400)
        return users

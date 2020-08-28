from flask import Blueprint, request, session
from app.dao.preferences_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *

class CreatePreferencesController(ConnectUController):
    def get_path(self):
        return "/"
    def get_methods(self):
        return ["POST"]
    def get_successful_response_code(self):
        return 201
    def content(self, **kwargs):
        try:
            user_id = request.args["user_id"]
        except Exception:
            raise HTTPException(msg="No user id supplied.", response_code=400)
        post_body = request.get_json()
        try:
            general = post_body["general"]
            clubs = post_body["clubs"]
            sports = post_body["sports"]
            entertainment = post_body["entertainment"]
            music = post_body["music"]
            movies = post_body["movies"]
        except Exception as e:
            InvalidRequestBodyException(msg=str(e))
        (insert_result, user_id) = create_preference(user_id, general, clubs, sports, entertainment, music, movies)
        if not insert_result.acknowledged:
            raise InternalErrorException("Couldn't add preferences to database.")

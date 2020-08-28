from flask import Blueprint, request, session
from app.dao.round_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *

class CreateRoundController(ConnectUController):
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
            opted = post_body["opted"],
            meet_type = post_body["meet_type"],
            first_time = post_body["first_time"]
        except Exception as e:
            InvalidRequestBodyException(msg=str(e))
        if find_round_by_id(uid=user_id):
            raise HTTPException("User already exists", response_code=400)
        (insert_result, user_id) = create_round(user_id, opted, meet_type, first_time)
        if not insert_result.acknowledged:
            raise InternalErrorException("Couldn't add round to database.")
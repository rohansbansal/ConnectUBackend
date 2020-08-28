from flask import Blueprint, request, session
from app.dao.round_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *
from app.utils.db_instance import mongo

class CreateRoundPairingController(ConnectUController):
    def get_path(self):
        return "/pairing/"
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
            emails = post_body["emails"]
        except Exception as e:
            InvalidRequestBodyException(msg=str(e))
        if find_round_pairing_by_id(uid=user_id):
            query = {"_id": user_id}
            mongo.db.round_pairing.remove(query)
        (insert_result, user_id) = create_round_pairing(user_id, emails)
        if not insert_result.acknowledged:
            raise InternalErrorException("Couldn't add round pairing to database.")
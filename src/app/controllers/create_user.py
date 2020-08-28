from flask import Blueprint, request, session
from app.dao.users_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *
import app.utils.google_auth as google_auth


class CreateUserController(ConnectUController):
    def get_path(self):
        return "/"

    def get_methods(self):
        return ["POST"]

    def get_successful_response_code(self):
        return 201

    def content(self, **kwargs):
        post_body = request.get_json()
        email = google_auth.get_user_info()["email"]
        try:
            name = post_body["name"]
            major = post_body["major"]
            school = post_body["school"]
            class_year = post_body["class_year"]
        except Exception as e:
            InvalidRequestBodyException(msg=str(e))

        if find_user_by_attributes(email=email):
            raise HTTPException("User already exists", response_code=400)
        (insert_result, user_id) = create_user(name, email, major, school, class_year)

        if not insert_result.acknowledged:
            raise InternalErrorException("Couldn't add user to database.")

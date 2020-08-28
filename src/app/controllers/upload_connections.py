from flask import request
from app.dao.connections_dao import *
from app.utils.connectu_controller import ConnectUController
from app.utils.exceptions import *


class UploadConnectionsController(ConnectUController):
    def get_path(self):
        return "/"

    def get_methods(self):
        return ["POST"]

    def get_successful_response_code(self):
        return 201

    def content(self, **kwargs):
        """
        Request body:
        {connections : {
            people:
            [{_id: "string", name: "string", email: "string", feedback: "string"}]
        }}
        """
        try:
            user_id = request.args["user_id"]
        except Exception:
            raise HTTPException(msg="No user id supplied.", response_code=400)
        post_body = request.get_json()
        try:
            connections = post_body["connections"]
        except Exception as e:
            InvalidRequestBodyException(msg=str(e))

        try:
            return (upload_connections(user_id, connections), str(user_id))

        except ValueError as e:
            raise HTTPException(msg=str(e), response_code=400)
        except Exception as e:
            raise HTTPException(msg=str(e), response_code=500)

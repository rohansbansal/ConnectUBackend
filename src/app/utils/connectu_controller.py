from app.utils.base_controller import abc, BaseController
from app.utils.exceptions import HTTPException
from app.utils.mongo_json_encoder import MongoEncoder
import json


class ConnectUController(BaseController, metaclass=abc.ABCMeta):
    """
    A REST-API controller that implements foundational functionality for
    handling requests.
    """

    @abc.abstractmethod
    def content(self, **kwargs):
        return dict()

    def get_name(self):
        return self.get_methods()[0] + "-" + self.get_path().replace("/", "-")

    def get_successful_response_code(self):
        return 200  # default successful response code of 200

    def response(self, **kwargs):
        try:
            content = self.content(**kwargs)
            if content or content == []:
                return (
                    json.dumps({"success": True, "data": content}, cls=MongoEncoder),
                    self.get_successful_response_code(),
                )
            return json.dumps({"success": True}), self.get_successful_response_code()
        except HTTPException as e:
            return (
                json.dumps({"success": False, "data": {"error": str(e)}}),
                e.response_code,
            )
        except Exception as e:
            return (
                json.dumps(
                    {"success": False, "data": {"error": "Internal error: " + str(e)}}
                ),
                500,
            )

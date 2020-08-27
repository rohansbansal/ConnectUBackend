class HTTPException(Exception):
    def __init__(self, msg, response_code):
        self.value = msg
        self.response_code = response_code

    def __str__(self):
        return self.value


class InvalidRequestBodyException(HTTPException):
    def __init__(self, msg=None):
        self.value = (
            "Invalid request body" if not msg else "Invalid request body: " + msg
        )
        self.response_code = 400


class InternalErrorException(HTTPException):
    def __init__(self, msg=None):
        self.value = "Internal error" if not msg else "Internal error: " + msg
        self.response_code = 500

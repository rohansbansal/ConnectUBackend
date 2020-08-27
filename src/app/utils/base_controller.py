import abc


class BaseController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_methods(self):
        """List of different HTTP methods supported."""

    @abc.abstractmethod
    def get_path(self):
        """URI-path that begins and ends with a '/'."""

    @abc.abstractmethod
    def get_successful_response_code(self):
        """Response code for the successful processing of a request."""

    @abc.abstractmethod
    def response(self, **kwargs):
        """The controller's response."""

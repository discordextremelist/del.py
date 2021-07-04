class DELpy(Exception):
    """
    Raise this so people could easily catch the exception
    """
    pass


class HTTPException(DELpy):
    """
    Raised when accessing the API fails
    """
    def __init__(self, *args, **kwargs):
        self.raised_error = kwargs.get('raised_error', None)
        if isinstance(self.raised_error, dict):
            self.status = self.raised_error.get('status', 0)
            self.message = self.raised_error.get('message', '')
        else:
            self.message = self.raised_error
            self.status = kwargs.get('status', None)

        err = f"Status code: {self.status} --> {self.message}"
        super().__init__(err)


class Unauthorized(DELpy):
    """
    Raised when no or invalid token is provided
    """
    pass


class InvalidTime(DELpy):
    """
    Raised when the time specified is too short.
    """
    pass

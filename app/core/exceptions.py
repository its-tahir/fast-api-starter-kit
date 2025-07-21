class BusinessLogicError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class AuthError(Exception):
    def __init__(self, message: str = "Authentication failed", status_code: int = 401):
        self.message = message
        self.status_code = status_code
        super().__init__(message) 
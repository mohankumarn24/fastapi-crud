# custom_exceptions.py

class ResourceNotFoundException(Exception):

    def __init__(self, message: str):
        self.message = message
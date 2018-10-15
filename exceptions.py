class MozzilaNotFound(Exception):
    def __init__(self, message, errors):

        super().__init__(message)

        self.error = "Mozzila directory could not be found. Is mozzila installed??"
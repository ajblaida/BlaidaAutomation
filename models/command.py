class Command:
    def __init__(self, arguments):
        self.zone = arguments[0]
        self.arguments = arguments[1:]
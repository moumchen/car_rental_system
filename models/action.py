
class Action:
    def __init__(self, message, handler):
        self.message = message
        self.handler = handler

    def execute(self, *args, **kwargs):
        return self.handler(*args, **kwargs)

from abc import ABC


class Chart(ABC):

    def __init__(self, config=None):
        if config is None:
            config = {}

        self.config = config

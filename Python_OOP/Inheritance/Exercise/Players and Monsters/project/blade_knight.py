from project.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return super(BladeKnight, self).__repr__()

from project.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return super(DarkKnight, self).__repr__()

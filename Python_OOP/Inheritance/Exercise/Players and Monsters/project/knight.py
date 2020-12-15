from project.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return super(Knight, self).__repr__()

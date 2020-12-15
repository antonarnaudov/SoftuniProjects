from project.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return super(Wizard, self).__repr__()

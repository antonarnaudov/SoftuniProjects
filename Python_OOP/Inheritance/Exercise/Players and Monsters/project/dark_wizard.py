from project.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return super(DarkWizard, self).__repr__()

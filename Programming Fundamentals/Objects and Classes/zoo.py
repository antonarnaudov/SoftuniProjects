class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            pass
        elif species == 'bird':
            pass

    def get_info(self, species):
        if species == 'mammal':
            animals = self.mammals
            species
        elif species == 'fish':
            pass
        elif species == 'bird':
            pass
        return f''
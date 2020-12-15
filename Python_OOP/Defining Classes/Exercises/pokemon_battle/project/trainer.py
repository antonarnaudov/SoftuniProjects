# from pokemon_battle.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon.name in [x.name for x in self.pokemon]:
            return "This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if pokemons:
            self.pokemon.remove(pokemons[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n'
        for p in self.pokemon:
            result += f'- {p.pokemon_details()}\n'
        return result


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
#
#
# trainer = Trainer("Stamat")
# pokemon = Pokemon("Pesho", 90)
# print(trainer.add_pokemon(pokemon))

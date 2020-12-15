# from project.lion import Lion
# from project.tiger import Tiger
# from project.cheetah import Cheetah
# from project.caretaker import Caretaker
# from project.vet import Vet
# from project.keeper import Keeper


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price > 0 \
                and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget - price < 0:
            return 'Not enough budget'
        return f'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        if self.workers:
            worker = [worker for worker in self.workers if worker.name == worker_name][0]
            if worker:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        expenses = sum([worker.salary for worker in self.workers])
        # for worker in self.workers:
        #     expenses += worker.salary
        if self.__budget - expenses > 0:
            self.__budget -= expenses
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        expenses = 0
        for animal in self.animals:
            expenses += animal.get_needs()

        if self.__budget - expenses > 0:
            self.__budget -= expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(lions) + '\n'
        result += f"----- {len(tigers)} Tigers:\n"
        result += '\n'.join(tigers) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(cheetahs) + '\n'
        return result
    # for l in lions:
    #     result += f'{l.__repr__()}\n'
    # result += f'----- {len(tigers)} Tigers:\n'
    # for t in tigers:
    #     result += f'{t.__repr__()}\n'
    # result += f'----- {len(cheetahs)} Cheetahs:\n'
    # for c in cheetahs:
    #     result += f'{c.__repr__()}\n'
    # return result.rstrip()


def workers_status(self):
    keepers = [keeper for keeper in self.workers if keeper.__class__.__name__ == 'Keeper']
    caretakers = [caretaker for caretaker in self.workers if caretaker.__class__.__name__ == 'Caretaker']
    vets = [vet for vet in self.workers if vet.__class__.__name__ == 'Vet']

    result = f'You have {len(self.workers)} workers\n' \
             f'----- {len(keepers)} Keepers:\n'
    for k in keepers:
        result += f'{k.__repr__()}\n'

    result += f'----- {len(caretakers)} Caretakers:\n'
    for c in caretakers:
        result += f'{c.__repr__()}\n'

    result += f'----- {len(vets)} Vets:\n'
    for v in vets:
        result += f'{v.__repr__()}\n'

    return result.rstrip()


#
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())

# test zoo workers_status

# test zoo add_animal success
from project.zoo import Zoo
from project.lion import Lion
import unittest


class Tests(unittest.TestCase):
    def test(self):
        z = Zoo("My Zoo", 1500, 6, 10)
        res = z.add_animal(Lion("Neo", "Male", 2), 1000)
        self.assertEqual(res, "Neo the Lion added to the zoo")
        self.assertEqual(len(z.animals), 1)
        self.assertEqual(z._Zoo__budget, 500)


if __name__ == "__main__":
    unittest.main()

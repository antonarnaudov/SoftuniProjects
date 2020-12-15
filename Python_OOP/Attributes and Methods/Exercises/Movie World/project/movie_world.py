class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < 10:
            return self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < 15:
            return self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        rented_by_customer = [r_d for r_d in customer.rented_dvds if r_d.id == dvd_id]

        if rented_by_customer:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return 'DVD is already rented'
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least " \
                   f"{dvd.age_restriction} to rent this movie"

        self.dvds[self.dvds.index(dvd)].is_rented = True
        i = self.customers.index(customer)
        self.customers[i].rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        rented_by_customer = [r_d for r_d in customer.rented_dvds if r_d.id == dvd_id]
        if rented_by_customer:
            i = self.customers.index(customer)
            self.customers[i].rented_dvds.remove(dvd)
            self.dvds[self.dvds.index(dvd)].is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in self.customers:
            result += f'{c.__repr__()}\n'
        for d in self.dvds:
            result += f'{d.__repr__()}\n'
        return result

#
# from project.customer import Customer
# from project.dvd import DVD
#
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
# print(movie_world)

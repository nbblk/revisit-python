class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('moves along....')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.moves()
my_car.get_make_model()

your_car = Vehicle('Ford', 'Mustang')
your_car.moves()
your_car.get_make_model()


class Airplane(Vehicle):
    def __init__(self, fea_id, make, model):
        self.fea_id = fea_id
        super().__init__(make, model)
        print('flies along...')


class Truck(Vehicle):
    def __init__(self):
        print('drives along...')



class GolfCart(Vehicle):
    pass


airplane = Airplane('Cesna', 'Skyhawk', 'n12345')
truck = Truck('Cesna2', 'Skyhawk')
golf = GolfCart('Cesna4', 'Skyhawk')

airplane.moves()
truck.moves()
golf.moves()
airplane.get_make_model()
truck.get_make_model()
golf.get_make_model()


print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
    
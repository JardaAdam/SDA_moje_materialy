import pickle

data = {
class Vehicles:

    def __init__(self, brand, model, color, n_of_wheels, max_speed, seat_capacity):
        self.brand = brand
        self.model = model
        self.color = color
        self.n_of_wheels = n_of_wheels
        self.max_speed = max_speed
        self.seat_capacity = seat_capacity
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
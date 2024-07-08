import pickle

with open('data.pickle', 'wb') as f:
   data = pickle.load(f)
print(data)
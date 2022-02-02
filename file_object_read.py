import pickle

file = open("sample.txt", "rb")
data = pickle.load(file)
print(data)
file.close()
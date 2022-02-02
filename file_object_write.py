import pickle
data = {
    "target": ["alpha", "bravo", "charly"]
}
file = open("sample.txt", "wb")
pickle.dump(data, file)
file.close()
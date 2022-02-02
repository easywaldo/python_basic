import pickle

file = open("sample.txt", "rb")
data = pickle.load(file)
print(data)
file.close()


with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(f'data : {data}')
    file.close()
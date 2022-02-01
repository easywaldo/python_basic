class Monster:
    def say(self):
        print('I am monster')

goblin: Monster = Monster()
goblin.say()

print(type(1))
print(type("string"))
print(type(True))
print(type(goblin))

print("string".__dir__())
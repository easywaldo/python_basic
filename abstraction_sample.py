class Robot:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def say_hi(self):
        print(f'greetings, my master call me {self.name}.')
    def cal_add(self, a, b):
        return a + b
    def die(self):
        print(f"{self.name} is being destroyed!")
    def __str__(self):
        return f"{self.name} and {self.code}!!"
    
siri = Robot("siri", 124823923)
javis = Robot("javis", 2943848)
bixby = Robot("bixby", 98723912)

print(siri.name)
print(javis.name)
print(siri)

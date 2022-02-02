import pay_module
from pay_module import Pay


pay:Pay = Pay(1, 20000, '2022-02-14')

print(pay.getPayInfo())
print(pay_module.version)
print(pay_module.printAuthor())

print(pay_module.__name__)
import random




numero = random.randrange(100)
for x in range(1, 6):
    numero = round(random.random() * 100)
    print("numero atual: {}".format(numero))

print("-------------------------")

for x in range(1, 6):
    numero = random.randrange(1, 101)
    print("numero atual: {}".format(numero))

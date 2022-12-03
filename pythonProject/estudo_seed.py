#seed é o que vai determinar o numero "aleatorio" que é gerado pelo ramdom
#caso a seed seja a mesma, o mesmo numero "aleatorio" sera gerado
import random


random.seed(100)
for x in range(1, 10):
    print(random.randrange(1, 101))

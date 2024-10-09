import random

numbers: list[int] = [i for i in range(95, 106)]
numbers1: list[int] = [i for i in range(10, 22, 2)]
list_random: list[bool] = [random.choice(True, False) for _ in range(5)]
list_random1: list[int] = [random.randint(1, 100) for _ in range(10)]
list_random2: list[int] = [random.randint for random.randint in list_random1 if random.randint > 50]
# list_random3: list[int] = [random.randint for _ in range(10)random.randint for random.randint in list_random if random.randint > 50]
list_random4: list[int] = [random.randint(10, 100) for _ in range(10)]
print(list_random4)
new_list: list[int] = [random.randint % 10 for random.randint in list_random4]

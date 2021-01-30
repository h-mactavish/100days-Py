import random

test_seed = int(input("Enter a seed number: "))

random.seed(test_seed)

random_num = random.randint(0, 100)
if(random_num < 50):
    print("Heads")
else:
    print("Tails")

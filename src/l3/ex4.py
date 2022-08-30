import random
random_list = [random.randint(0,100) for i in range (50)]

double_list = [x*x for x in random_list]
print(random_list)
print(double_list)
import random
# import my_module
#
#
# random_integer = random.randint(1, 10) #inclusive of 1 and 10
# print(random_integer)
#
# print(my_module.my_fav_num)
#
# random_number_0_to_1 = random.random() #it gives random int from 0 to 1
# # 0 inclusive to 1 not inclusive
# print(random_number_0_to_1)
#
# random_float = random.uniform(1, 10) #inclusive of 1 and 10

heads_or_tails = random.randint(0,1)  # we will get 0 or 1
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
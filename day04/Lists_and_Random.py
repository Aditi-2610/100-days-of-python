import random
from random import choice

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friends_index = random.randint(0,4)
print(friends[random_friends_index])
 #or

print(random.choice(friends)) #choice function is used to choose an item form a sequence
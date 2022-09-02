import random
import string


def generate_random_dict(length):
    random_dict = {}
    for _ in range(length):
        rand_key = "".join(random.sample(string.ascii_letters + string.digits, k=5))
        rand_value = "".join(
            random.sample(
                string.ascii_letters + string.digits, k=random.randint(a=3, b=9)
            )
        )
        random_dict[rand_key] = rand_value
    return random_dict


dictionary = generate_random_dict(3)
print(dictionary)

import random
from string import ascii_letters


def generate_random_word(min, max):
    random_string = "".join(
        random.choice(ascii_letters) for _ in range(random.randint(min, max))
    )
    # random_string = ''.join(random.sample(ascii_letters, k=random.randint(min,max)))        ### Second attempt
    return random_string


word = generate_random_word(2, 6)
print(word)

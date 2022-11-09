import random

noun = {0: 'dog', 1: 'cat', 2: 'boy', 3: 'girl', 4: 'teacher', 5: "hamster"}
adjectives = {0: 'red', 1: 'happi', 2: 'sad', 3: 'blue', 4: 'fast', 5: 'first'}
verb = {0: 'run', 1: 'sleep', 2: 'read', 3: 'look', 4: 'hear', 5: 'sit'}



def wheel_rotation_random():
    random_word = []
    n = random.randint(0, 5)
    adj = random.randint(0, 5)
    ve = random.randint(0, 5)

    random_word.append(noun.get(n))
    random_word.append(adjectives.get(adj))
    random_word.append(verb.get(ve))
    random_word.append(n)
    random_word.append(adj)
    random_word.append(ve)

    return random_word


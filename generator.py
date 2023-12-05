import random

def generate_array(n, lb, ub, seed, is_write):
    random.seed(seed)

    arr = [random.randint(lb, ub) for _ in range(n)]

    # write to file
    if is_write:
        with open(f'{n}_seed{seed}.txt', 'w', encoding='utf-8') as f:
            for num in arr:
                f.write(f'{num}\n')

    return arr
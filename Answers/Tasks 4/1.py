import itertools

def generate_combinations(word):
    permutations = itertools.permutations(word)
    combinations = [''.join(p) for p in permutations]
    unique_combinations = set(combinations)
    
    return unique_combinations

# Пример
word = "слово"
combinations = generate_combinations(word)
print("Все возможные комбинации букв в слове:")
for combo in combinations:
    print(combo)

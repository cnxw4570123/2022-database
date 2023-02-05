def key_method(pkms):
    print(f"pokemons = {pkms}")
    return pkms[1]


pokemons = [["라이츄", 200], ["피카츄", 100], ["파이리", 80], ["야도란", 50], ["잉어킹", 10]]
sorted_list = sorted(pokemons, key=key_method)
print(f"sorted = {sorted_list}")

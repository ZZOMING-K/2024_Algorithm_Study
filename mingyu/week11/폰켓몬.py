def solution(nums):
    answer = 0
    pokemon = {}
    for i, num in enumerate(nums):
        pokemon[num] = pokemon.get(num, 0) + 1
    print(pokemon)
    return answer

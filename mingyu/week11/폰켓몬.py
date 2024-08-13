def solution(nums):
    answer = 0
    pokemon = {}
    for i, num in enumerate(nums):
        pokemon[num] = pokemon.get(num, 0) + 1
    if len(pokemon) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(pokemon)
    return answer

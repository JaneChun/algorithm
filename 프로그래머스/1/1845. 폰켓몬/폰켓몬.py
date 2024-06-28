def solution(nums):
    typeOfPokemon = len(set(nums))
    pokemonSelectable = len(nums) / 2
    
    return min(typeOfPokemon, pokemonSelectable)
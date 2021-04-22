"""While such functions technically return something, that return value is not useful.
 You should add type hints saying as much by using None also as the return type:"""

print('----FUNCTION WITHOUT RETURN VALUE------')


def play(player_name: str) -> None:
    print(f"{player_name} plays")


shit_play = play('Adis')
print(shit_play)

print('----FUNCTIONS WITH RETURN VALUE------')


def play_1(player_name: str) -> str:
    return f"{player_name} plays"


shitplay_1 = play_1('Jacob')
print(shitplay_1)

"""Note that being explicit about a function not returning anything is different from not adding a type hint about 
the return value: """

print('-------FUNCTION WITH NO RETURN ANNOTATIONS-----')


def play_2(player_name: str):
    return f"{player_name} plays"


shitplay2 = play_2('Adit')

print(shitplay2)

"""As a more exotic case, note that you can also annotate functions that are never expected to return normally. This 
is done using NoReturn: """

from typing import NoReturn


def black_hole(player_name: str) -> NoReturn:
    raise Exception('There is no going back')


"""Since black_hole() always raises an exception, it will never return properly."""

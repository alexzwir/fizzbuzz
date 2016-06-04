"""
Regras do jogo:
1-) Se for múiltiplo de três, imprime Buzz.
2-) Se for múltiplo de cinco, imprime Fizz.
3-) Se for múltiplo de três e cinco, imprime Buzzfizz.
4-) Para todas as outras, imprime o número.
"""

from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)

def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'Fizzbuzz'
    elif multiple_of_5(pos):
        say = 'Buzz'
    elif multiple_of_3(pos):
        say = 'Fizz'

    return say

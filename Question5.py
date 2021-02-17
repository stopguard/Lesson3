"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого)
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
from random import choices
from random import sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
uniq_func = {True: choices, False: sample}


def get_jokes(n=1, uniq=False):
    answ = []
    if n > min([len(nouns), len(adverbs), len(adjectives)]):
        return 'Много шуток тоже вредно!'
    _nouns = uniq_func[uniq](nouns, n)
    _adverbs = uniq_func[uniq](adverbs, n)
    _adjectives = uniq_func[uniq](adjectives, n)
    for noun, adverb, adjective in zip(_nouns, _adverbs, _adjectives):
        answ.append(' '.join(noun, adverb, adjective))
    return answ


num_of_jokes = input('Введите желаемое количество шуток: ')

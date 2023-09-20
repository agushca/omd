def step2_no_umbrella():
    print('Пошел очень сильный дождик, и уточку унесло потоком воды в неизвестном направлении')
    bird = 'Со смертью этого персонажа нить вашей судьбы обрывается. \nЗагрузите предыдущую функцию дабы восстановить течение судьбы, или живите дальше в проклятом мире, который сами и создали \n{}'
    print(bird.format('(P.S. Ну зачем жалеть зонтик для уточки?) '))

def step2_umbrella():
    happy = 'Уточка успешно дошла до бара, откуда навеселе вернулась домой, где ее ждали утята. Вот они, слева направо: '
    for i in range(len(dir(int))):
        print(dir(int)[i], end=' ')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()

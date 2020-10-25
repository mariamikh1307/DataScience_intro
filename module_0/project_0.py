import numpy as np     

def game_core_v2(number):
    '''Применим бинарный метод поиска, то есть будем поэтапно делить диапазон загаданного числа пополам.

    Сначала устанавливаем число для первой попытки в середине заданного диапазона, то есть 50.
    Сравниваем число с загаданным и в зависимости от того, больше оно или меньше, выбираем следующий диапазон для деления пополам.

    Поэтапно функция принимает загаданное число и возвращает число попыток'''

    count = 1
    low = 1 #нижний порог диапазона отгадывания числа
    high = 100 #верхний порог диапазона отгадывания числа
    predict = 50
    while number != predict:
        count+=1
        if number > predict:  
            low = predict + 1 
            predict = (low+high) // 2
        elif number < predict: 
            high = predict 
            predict = (low+high) // 2
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core_v2)
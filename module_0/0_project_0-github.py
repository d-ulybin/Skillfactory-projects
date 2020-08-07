#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np # импорт модуля numpy

def game_core(number): #функция с игровой механикой
    
    count = 0 #задаем счетчик попыток
    predict = 0 #задаем переменную для предполагаемого числа
    upper_limit = 100
    lower_limit = 1  
    #выставляем предельные значения для predict
        
    while number != predict: #цикл будет работать до момента "угадывания"
    
        predict = int((lower_limit+upper_limit) / 2) #predict - int от среднего арифметического двух лимитов
        count += 1 #плюуем счетчик
                
        if number > predict:
            lower_limit = predict + 1 #если загаданное число больше, то изменяем нижний лимит                
        elif number < predict:
            upper_limit = predict - 1 #если загаданное число меньше, то изменяем верхний лимит 
            
    return(count) #функция возвращает количество попыток


def score_game(game_core): #функция, которая автоматизирует игру программы "сама с собой" 1000 раз

    count_ls = [] # создаем пустой список для наполнения данными о количестве оппыток
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size=(1000)) #массив случайных целых чисел из интервала  1-101 в кол-ве 1000
    
    for number in random_array: #запускаем цикл, где загаданное число будет браться из массива
        count_ls.append(game_core(number)) #запускаем движок игры с определенным выше загаданным числом
    
    score = int(np.mean(count_ls)) #подсчитываем среднее целое значение кол-ва попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток") 
    
    return(score)


score_game (game_core) #Вызываем сразу две функции: на отыгрыш 100 игр и механику игры


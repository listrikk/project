import time
import battle
import training
import npc


def your_home(robot) -> None:
    print('Вы в доме.. Одна комната это немного, но зато это всё твоё.')
    print(
        'Оглядываясь по сторонам ты видишь станцию подзарядки, стул, стол, цветочек на подоконнике и картину на стене. Можно подзаредиться и пополнить свою энергию или сесть на стул и задуматься о своих характеристиках, а может даже повысить их. Выбери, что сделать из команд приведённых ниже.'
    )
    print('1. Лечь спать. 2. Посмотреть характеристики. 3. Уйти.')
    print('Что ты хочешь сейчас сделать?')
    your_choice = input().lower()
    if your_choice == 'лечь спать' or your_choice == '1':
        if robot.energy <= 90:
            print('Ты поспал, энергия восстановлена.')
            robot.energy += 100 - robot.energy
        else:
            print('Ты не очень хочешь спать...')

        your_home(robot)
    elif your_choice == 'посмотреть характеристики' or your_choice == '2':
        print(
            f'Здоровье: {robot.health}, Сила: {robot.power}, Энергия: {robot.energy}, Очки: {robot.point}, Красота: {robot.beautiful}'
        )
        while robot.point >= 1:
            print('Пора улучшить навыки. Что ты хочешь улучшить? Сила/красота?')
            answer5 = input().lower()
            if answer5 == 'сила':
                robot.power += 1
                robot.point -= 1
            elif answer5 == 'красота':
                robot.beautiful += 1
                robot.point -= 1
            else:
                print('Такое улучшить нельзя..')
        your_home(robot)
    elif your_choice == 'уйти' or your_choice == '3':
        None
    elif your_choice == 'взять':
        if npc.flowers == False:
            print('Вы взяли цветок, можно идти к медсестре!')
            npc.flowers = True
        else:
            print('Вам тут нечего брать..')
    else:
        print(
            'К сожалению робот не умеет делать такие вещи, или не может понять, что за мысль появилась у него в голове. Попробуй снова..'
        )
        your_home(robot)
    downtown(robot)
    return None


def downtown(robot) -> None:
    print('Вы в городе. Тут людно. Точнее людей нету, зато роботов много. Что вы хотите сделать?')
    print('1. Посмотреть доску заданий. 2. Посмотреть карту. 3. Уйти в другую локацию.')
    answer = input().lower()
    if answer == 'Посмотреть доску заданий' or answer == '1':
        print('Вы подошли к доске заданий, вдруг вас отвлёк робот стоящий рядом.')
        npc.give_job()
        downtown(robot)
    elif answer == 'Посмотреть карту' or answer == '2':
        print(
            'Вы подходите к огромной карте прямо по среди города.. В самом центре вы видите точку, обозначающую вас. Снизу жилая зона, справа медпункт, слева зона обучения бойцов, а сверху большим пятном отмеченна неизвестная зона.'
        )
        print('Список локаций: Медпункт, зона обучения бойцов, дом, неизвестная зона..')
        print('Осмотрев карту робот уходит обратно')
        downtown(robot)
    elif answer == 'Уйти в другую локацию' or answer == '3':
        print(
            'В какую локацию идём? Посмотреть их можно на карте. Если вы этого не сделали напишите "Не знаю"'
        )
        answer2 = input().lower()
        if answer2 == 'медпункт':
            medical_center(robot)
        elif answer2 == 'зона обучения бойцов':
            combat_zone(robot)
        elif answer2 == 'дом':
            your_home(robot)
        elif answer2 == 'неизвестная зона':
            if npc.certificate == True:
                outside_city(robot)
            else:
                print('Вам сюда рано.')
                downtown(robot)
        elif answer2 == 'не знаю':
            downtown(robot)
        else:
            print(
                'Вы уехали искать это место, но увы, даже спустя много времени не нашли его.. Может была какая-то ошибка?'
            )
            downtown(robot)
    else:
        print(
            'Вдруг программа робота выдала знак ошибки. Он начал с огромной скоростью ездить по всему городу. Не сразу получилось вернуть управление, но спустя несколько минут роботу снова пришлось ехать к городу. Лучше не делать действий, которые программа не знает.'
        )
        downtown(robot)
    return None


def medical_center(robot) -> None:
    print(
        'Вы в больнице. В очереди стоят несколько роботов. Некоторые из них сильно поломаны, другие же выглядят целыми.. '
    )
    print('1. Взять талончик и встать в очередь. 2. Уйти.')
    answer = input().lower()
    if answer == 'взять талончик и встать в очередь' or answer == '1':
        print('Вы встаёте в очередь.. Роботов в очереди: 3')
        time.sleep(3)
        print('Роботов в очереди: 2')
        time.sleep(2)
        print('Роботов в очереди: 1')
        time.sleep(5)
        print('Ваша очередь! Вы заезжаете в кабинет. Вас встречает робот механик.')
        print(f"-Привет! Садись на стульчик, сейчас найдём тебе новые детали.")
        print('Врач выключает вашу систему и начинает менять детали.')
        time.sleep(3)
        print('Вы просыпаетесь, целый и новый. Доктор улыбается вам, вы вежливо прощаетесь и уходите.')
        robot.health += 100 - robot.health
        medical_center(robot)
    elif answer == 'уйти' or answer == '2':
        downtown(robot)
    elif answer == 'пройтись по коридорам':
        npc.nurse()
        downtown(robot)
    else:
        print(
            'Странные мысли пробегают у вас в голове.. Что вы хотели сделать? Непонятно..'
        )
    return None


def combat_zone(robot):
    print('Вы в зоне обучения боям. Как только вы оказываетесь у ворот, к вам подьёзжает большой робот генерал.')
    print('-Привет, мелкий. Как ты сюда попал?')
    print('1. Я хочу стать сильным воином. 2. Я случайно забрёл. 3.Заплакать от страха.')
    answer = input().lower()
    if answer == 'я хочу стать сильным воином.' or answer == '1':
        print('-Ты только в качестве гранаты подойдёшь, хотя ладно. Проходи прямо. Можешь там тренироваться.')
        print('Вы проходите вглубь базы. Впереди вы видите новичков. К вам сзади подъезжает робот.')
        print(
            '-Привет! Я инструктор. Суть боёв заключается в твоём выборе между действиями. Нужно предугадать что выберет противник. Остальное нужно познать уже в самом бою. Перед началом боя нужно выбрать сложность тренировочного робота. Выбери легкая/средняя/сложная.'
        )
        answer2 = input().lower()
        if answer2 == 'легкая':
            battle.battle(10, 50, robot)
            print('Вы провели бой. Очки опыта получены')
            robot.point += 1
            combat_zone(robot)
        if answer2 == 'средняя':
            battle.battle(15, 70, robot)
            print('Вы провели бой. Очки опыта получены')
            robot.point += 1
            combat_zone(robot)
        if answer2 == 'сложная':
            battle.battle(25, 100, robot)
            print('Вы провели бой. Очки опыта получены')
            robot.point += 1
            combat_zone(robot)
        else:
            print('Не получив внятного ответа инструктор ушёл, попробуй ещё раз.')
            combat_zone(robot)

    elif answer == 'я случайно забрёл' or answer == '2':
        print('-Тогда тебе ровно назад, удачи.')
        print('Вы уезжаете и возвращаетесь в центр города.')
        downtown(robot)
    elif answer == 'заплакать от страха' or answer == '3':
        print(
            'Вы стоите и пытаетесь заплакать, но роботы так не умеют. Поэтому генерал быстро меняется в настроении и выпинывает вас из зоны, вы укатываетесь в центр города.'
        )
        downtown(robot)
    elif answer == 'я к капитану':
        print('-Так бы сразу и сказал, его кабинет находится в корпусе слева.')
        print('Робот направился туда.')
        npc.captain()
        downtown(robot)
    else:
        print(
            'Робот не понял, что хочет сделать, поэтому просто стоял и не двигался. Генерал спустя пару минут перетащил вас за ворота зоны, а сам уехал.'
        )
        combat_zone(robot)
    return None


def outside_city(robot) -> None:
    robot.beautiful = 45
    file = open('end.txt', 'a')
    print(
        'Вы вышли за город.. Тут ужасно. Одна разруха.. Вместе с парочкой роботов, за которыми вы увязались вы идёте в эпицентр боя.. Пора защитить свой город. Показать, что ты это можешь.'
    )
    if robot.name == 'воин':
        print(
            'Спустя пару минут вы случайно отделяетесь от своей группы.. После долгих скитаний в округе вы ноходите их! Вражеских роботов. Сразу два. Синий и зелёный... Но почему они не атакакуют друг друга, разве они не враги? Плевать.. Нужно показать кто тут сильный.'
        )
        if robot.beautiful >= 42:
            print('Только ты вышел на поле они сразу застыли разглядывая тебя... ')
            print('Синий робот: ты..')
            print(
                'Ты: Что? Я страшный и пугающий, бойтесь меня!!! Я вас всех побью!!!'
            )
            print(
                'Не успел ты договорить как оба робота рухнули замертво.. Кажется их ослепило твоё сияние'
            )
            print('Концовка: Красота сильнее действий')
            file.write('\nКрасота сильнее действий')

        else:
            print('Ты вышел к ним, они готовы к бою. Не проиграй.')
            itog1 = battle.battle(25, 150, robot)
            if itog1 == 1:
                print('Первый враг повержен. Вы почувствовали прилив сил!')
                robot.energy += 100
                itog2 = battle.battle(32, 120, robot)
                if itog2 == 1:
                    print(
                        'Вы победили их, сразу после к вам выбежала группа роботов, увидев, что вы смогли их победить вас назначили в постоянную армию города. Теперь вы настоящий воин!'
                    )
                    print('Концовка: ты смог!')
                    file.write('\nТы смог!')
                else:
                    print('Вы не смогли отстоять честь вашего города.. Это конец.')
                    print('Концовка: Ты теперь один')
                    file.write('\nТы теперь один')
            else:
                print('Вы не смогли отстоять честь вашего города.. Это конец.')
                print('Концовка: Ты теперь один')
                file.write('\nТы теперь один')
    elif robot.name == 'умник':
        print(
            'Спустя пару минут вы случайно отделяетесь от своей группы.. После долгих скитаний в округе вы ноходите их! Вражеский робот.. Сейчас он узнает кто тут настоящая сила..'
        )
        if robot.beautiful >= 42:
            print('Только ты вышел на поле он посмотрел на тебя... ')
            print('Синий робот: ты..')
            print('Ты: Что? Готовься к своей кончине!')
            print(
                'Но противник не двигался, быстро поняв в чём дело, противник был ослеплён, ты подбежал к нему и стукнул по голове.'
            )
            print('Концовка: Это ведь победа, да?')
            file.write('\nЭто ведь победа, да?')
        else:
            print('Ты вышел к нему, он готов атаковать. Не проиграй.')
            itog1 = battle.battle(37, 160, robot)
            if itog1 == 1:
                print(
                    'Вы победили его! Обернувшись назад вы увидели своего инструктора. Поздравляю, тебя признали. Теперь у тебя есть настоящий дом!'
                )
                print('Концовка: Ты самый умный.. и сильный)')
                file.write('\nТы самый умный.. и сильный)')
            else:
                print(
                    'Ты стоишь и просто смотришь вниз.. Как.. как ты мог? Нету смысла возвращаться домой. Ты проиграл всё что мог.'
                )
                print('Концовка: Жаль его..')
                file.write('\nЖаль его..')

    else:
        print(
            'Спустя пару минут вы случайно отделяетесь от своей группы.. После долгих скитаний в округе вы ноходите их! Вражеский робот.. Сейчас он узнает кто тут настоящая сила..'
        )
        if robot.beautiful >= 42:
            print('Только ты вышел на поле он посмотрел на тебя... ')
            print('Синий робот: ты..')
            print('Ты: Что я?')
            print('Сини1 робот: я хочу уйти в ваш город..')
            print('Концовка: новый друг?..')
            file.write('\nНовый друг?')
        else:
            print('Ты вышел к нему, он готов атаковать. Не проиграй.')
            itog1 = battle.battle(35, 140, robot)
            if itog1 == 1:
                print(
                    'Вы победили его.. Программа робота еле слышно издала пиканье.. Посмотрев на него пару минут вы начали его тащить к себе в город. Спустя пару дней ему сменили детали. Когда он проснулся, то признал вашу силу и перешёл на вашу сторону.'
                )
                print('Концовка: Новый житель города.')
                file.write('\nНовый житель города')
            else:
                print(
                    'Ты стоишь и просто смотришь вниз.. Как.. как ты мог? Нету смысла возвращаться домой. Ты проиграл всё что мог.'
                )
                print('Концовка: Мне его жалко..')
                file.write('\nМне его жалко...')
                file.close()
    print('Что бы посмотреть концовки, при запуске игры напишите "концовки".')
    npc.new()
    

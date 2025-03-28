import random

actions = ['атака', 'защита']


def battle(his_power: int, his_health: int, robot) -> int:
    print('Вы вступаете в бой. Продолжать драться можно пока ваше здоровье больше 10.')
    while True:
        print('Что вы сделаете сейчас?')
        print('1. Нанести удар. 2. Защититься. 3. Сделать усиленный удар.')
        bot_action = random.choice(actions)
        user_action = input().lower()
        if user_action == 'нанести удар' or user_action == '1':
            if bot_action == 'атака':
                print('Вы смогли ударить первым, а бот не защитился.')
                his_health -= robot.power
            else:
                print('Бот защитился и атаковал вас.')
                robot.health -= his_power
            robot.energy -= 7
        elif user_action == 'защититься' or user_action == '2':
            if bot_action == 'атака':
                print('Вы защитились и атаковали бота')
                his_health -= robot.power
            else:
                print('Вы и враг защитились. Ничего не произошло.')
            robot.energy -= 5
        elif user_action == 'сделать усиленный удар' or user_action == '3':
            if bot_action == 'атака':
                print('Вам повезло, вы атаковали первыми! Вы снесли в два раза больше урона.')
                his_health -= robot.power * 2
            else:
                print('Вам не повезло, враг продумал этот ход. Вы потеряли в два раза больше здоровья.')
                robot.health -= his_power * 2
            robot.energy -= 10
        else:
            print('Вы сделали что-то непонятное, враг просто атаковал вас.')
            robot.health -= his_power
        print(
            f'Ваше здоровье:{robot.health}. Ваша энергия:{robot.energy}. Здоровье врага:{his_health}'
        )
        if his_health <= 1:
            print('Вы победили! Враг повержен.')
            return 1
        if robot.health <= 11:
            print(
                'Вы поняли, что вот-вот сломаетесь и начали убегать с боя. Это поражение.'
            )
            return 0
        if robot.energy <= 11:
            print(
                'Вы поняли, что вот-вот разрядитесь и начали убегать с боя. Это поражение.'
            )
            return 0


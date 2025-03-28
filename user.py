import battle
import history
import location
import training
import time
import npc

file = open('end.txt', 'r')
if file.read() == '':
    file.close
    file = open('end.txt', 'a')
    file.write('Твои концовки:')
    file.close
else:
    file.close
while True:
    print('Вы готовы начать игру? Да/нет')
    answer_game = input().lower()
    if answer_game == 'да':
        # history.video()
        # time.sleep(3)
        training.training()
    elif answer_game == 'концовки':
        file = open('end.txt', 'r')
        data = file.read()
        print(''.join(data))
        file.close()
    else:
        print('Вы ответили нет или ввели не то. Пока.')
        quit()


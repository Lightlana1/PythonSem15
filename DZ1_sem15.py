# Дорабатываем задачу из 13-го семинара
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.
# Добавим логирование ошибок

import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='task_DZ1.log',
                    encoding='utf-8',
                    level=logging.ERROR,
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)



def ask_user_input():
    while True:
        user_input = input('Введите число: ')
        try:
            result = int(user_input)
            break
        except ValueError as e:
            logger.error(f'{user_input} не получилось привести к целому числу')
            try:
                result = float(user_input)
                break
            except ValueError as e:
                logger.error(f'{user_input}не получилось привести к целому числу')

    return result


if __name__ == '__main__':
    print(ask_user_input())
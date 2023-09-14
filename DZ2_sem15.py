# Функция получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# Сделаем логирование информации с возможностью запуска из терминала

import logging
import argparse
from typing import Callable


FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='task_DZ2.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)

def parse():
    parser = argparse.ArgumentParser(prog='check_data',
                                     description='Проверка даты на валидность',
                                     epilog='check_date("20.06.1993")')

    parser.add_argument('-d', '--day', help='Какой день месяца')
    parser.add_argument('-m', '--month', help='Какой месяц')
    parser.add_argument('-y', '--year', help='Какой год')
    args = parser.parse_args()
    return check_date(f'{args.day} {args.month} {args.year}')

def add_to_log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_data = {'дата': args, **kwargs, 'валидность': result}
        logger.info(log_data)

        return result
    return wrapper

def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


@add_to_log
def check_date(data: str) -> bool:
    day, mon, yaer = map(int, data.split('.'))
    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= yaer <= 9999):
        return False

    if mon in (4, 6, 9, 11) and day > 30:
        return False

    if mon == 2 and day > 29:
        return False

    if mon == 2 and if_leap(yaer) and day > 29:
        return False

    if mon == 2 and not if_leap(yaer) and day > 28:
        return False

    return True

if __name__ == '__main__':
    print(parse())
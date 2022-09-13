# В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
# Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина

import os
from victory import birthday_month_year
from file_manager import author, show_files


def test_birthday_month_year():
    assert birthday_month_year(5, 6, 1899) == 'пятого июня 1899 года'
    assert birthday_month_year(7, 12, 2019) == 'седьмого декабря 2019 года'


# тест для грязной функции
def test_author():
    assert author() == 'Пушкин Александр Сергеевич'



def test_show_files():
    if os.listdir():
        assert len(show_files()) != 0
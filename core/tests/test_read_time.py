from core.read_time import read_time
from random import random, choice


def test_calculate_read_time():
    one_minute_text = ['word'] * 265

    one_minute = read_time(one_minute_text)
    two_minutes = read_time(one_minute_text * 2)
    three_minutes = read_time(one_minute_text * 3)

    assert one_minute == 1
    assert two_minutes == 2
    assert three_minutes == 3


def test_calculate_generic_text_integer_read_time():
    one_minute_text = ['word'] * 265

    generic_read_time = choice(range(50))
    whole_text = one_minute_text * generic_read_time

    time = read_time(whole_text)

    assert time == generic_read_time

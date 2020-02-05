from core.read_time import read_time
from random import random, choice


def test_calculate_read_time():
    one_minute_text = ['word'] * 265
    two_and_a_half_minutes_text = ['word'] * int(265 * 2.5)

    one_minute = read_time(one_minute_text)
    two_minutes = read_time(one_minute_text * 2)
    three_minutes = read_time(one_minute_text * 3)

    two_and_a_half_minutes_rounds_to_two_minutes = read_time(two_and_a_half_minutes_text)

    assert one_minute == 1
    assert two_minutes == 2
    assert three_minutes == 3
    assert two_and_a_half_minutes_rounds_to_two_minutes == 2


def test_calculate_generic_text_integer_read_time():
    """
    read_time should calculate the read time for a text whose length can
    be split in equal parts of 265 words
    """
    one_minute_text = ['word'] * 265
    generic_read_time = choice(range(50))
    whole_text = one_minute_text * generic_read_time

    time = read_time(whole_text)

    assert time == generic_read_time


def test_read_time_should_round_decimal_read_time():
    """
    Given a random text length, the function should return the read time in rounded values
    """
    random_decimal_multiplier = round(random(), 2)
    generic_read_time = choice(range(50)) * random_decimal_multiplier
    whole_text = ['word'] * int(265 * generic_read_time)

    time = read_time(whole_text)

    assert time == round(generic_read_time)

def read_time(words):
    """
    Medium.com reading time formula: 265 words per minute

    :param words: list of strings
    :return: read time for a given text
    :rtype: int
    """
    number_of_words = len(words)
    words_per_minute = 265

    reading_time = number_of_words / words_per_minute

    return round(reading_time)

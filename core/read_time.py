def read_time(words):
    """
    Medium.com reading time formula: 265 words per minute
    """

    number_of_words = len(words)
    words_per_minute = 265

    reading_time = number_of_words / words_per_minute

    return round(reading_time)

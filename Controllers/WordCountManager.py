import re

class WordCountManager:

  def __init__(self):
    ## leaving this empty for the time being
    pass

  def get_word_count(self, words):
    word_count = len(re.findall(r'\w+', words))
    return word_count



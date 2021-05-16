"""
Sentence class:

- accepts only strings, otherwise raises a TypeError
- accepts only complete sentences, otherwise - ValueError

- example of work:

    __repr__()
    > <Sentence (words = 13, other_chars = 7)>

- the Sentence()._words method must return a lazy iterator. The point here
  is that we do not want to store a list of words in the object, because
  sentences can be very large and take up a lot of memory, so we will generate
  it as needed and give it to the user

- example of work:

    Sentence('Hello word!')._words()
    > <generator object Sentence._words at 0x7f4e8cb065f0>'
    next(Sentence('Hello word!')._words())
    > 'Hello'

- has a Sentence().words property that returns a list of all words
  in a sentence (* remind you that we don't want to store all these words
  in our object)
- has a Sentence().other_chars property that returns a list of all non-words
  in a sentence
- can give a word by index

- example of work:

    Sentence('Hello world!')[0]
    > 'Hello'

- can give a slice by words

- example of work:

    Sentence('Hello world!')[:]
    > 'Hello world'

- can be used in a for loop

- example of work:

    for word in Sentence('Hello world!'):
        print(word)
    > 'Hello'
    > 'world'

- when passed as an argument to the iter() function,
  it returns SentenceIterator


SentenceIterator class:

- implements the Iterator Protocol
- when passed as an argument to the next() function, in turn,
  returns the words from the Sentence object that generates it

"""
from string import punctuation
from re import finditer

from settings import SENTENCE_END_SYMBOLS, SENTENCE


class SentenceIterator:
    """
    SentenceIterator class:

    - implements the Iterator Protocol
    - when passed as an argument to the next() function, in turn,
      returns the words from the Sentence object that generates it

    """

    def __init__(self, words):
        self._words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self._words):
            raise StopIteration
        result = self._words[self.index]
        self.index += 1
        return result

    @property
    def words(self):
        """
        the words list
        :return: list
        """
        return self._words


class Sentence:
    """
    Sentence class
    """

    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError('this should be the string')
        if not string.strip().endswith(SENTENCE_END_SYMBOLS):
            raise ValueError('this should be a completed proposal with '
                             '".", "?", or "!" at the end')
        self.string = string

    @staticmethod
    def get_clear_string(string: str) -> str:
        """
        filtering all punctuation chars
        :param string: str
        :return: str
        """
        return ''.join(filter(lambda _: _ not in punctuation, string)).strip()

    @staticmethod
    def get_other_chars(string: str) -> str:
        """
        getting all punctuation chars
        :param string: str
        :return: str
        """
        return ''.join(filter(lambda _: _ in punctuation, string)).strip()

    @property
    def clean_string(self) -> str:
        """
        string without punctuation
        :return: str
        """
        return self.get_clear_string(self.string)

    @property
    def other_chars(self):
        """
        string with only punctuation
        :return:
        """
        return list(self.get_other_chars(self.string))

    @property
    def other_chars_count(self) -> int:
        """
        Count of punctuation chars
        :return: int
        """
        return len(self.other_chars)

    def _words(self):
        """
        Words generator.
        :return:
        """
        for item in finditer(r'\w+', self.clean_string):
            yield item.group(0)

    @property
    def words(self):
        """
        list of words
        :return: list
        """
        return list(self._words())

    @property
    def words_count(self) -> int:
        """
        count of words
        :return: int
        """
        return len(self.words)

    def __repr__(self):
        return f"<Sentence(words={self.words_count}," \
               f" other_chars={self.other_chars_count})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def __getitem__(self, key):
        return self.words[key]


if __name__ == "__main__":
    sentence = Sentence(SENTENCE)
    sentence_iterator = SentenceIterator(sentence.words)

    print(sentence)
    print(sentence.words)
    print(sentence.other_chars)
    print(sentence[2:16])
    print(sentence[-3])
    for word in sentence[100:110]:
        print(word, end=" ")
    for word in sentence_iterator:
        print(word)

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


class SentenceIterator:
    """
    SentenceIterator class:

    - implements the Iterator Protocol
    - when passed as an argument to the next() function, in turn,
      returns the words from the Sentence object that generates it

    """
    pass


class Sentence:
    """
    Sentence class
    """
    def __init__(self, text: str):
        pass

    def __repr__(self):
        return f"<Sentence(words={?}, other_chars={?})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def _words(self):
        """
        method return a lazy iterator. The point here is that we do not
        want to store a list of words in the object, because sentences can
        be very large and take up a lot of memory, so we will generate
        it as needed and give it to the user
        :return:
        """
        return < lazy iterator >

    @property
    def words(self):
        """
        property that returns a list of all words in a sentence
        :return: list
        """
        return words in text

    @property
    def other_chars(self):
        """
        property that returns a list of all non-words in a sentence
        :return: list
        """
        return not words

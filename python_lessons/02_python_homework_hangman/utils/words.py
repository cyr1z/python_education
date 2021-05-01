"""
WordsDictionary().get_random() - return a random word from dictionary.

"""
import urllib.request
from random import choice


class WordsDictionary:
    """
    working with word list? and select random word class.
    :word_dictionary: contains word dictionary
    :get_random(): returns random word

    """

    def __init__(self, url: str, word_dict_file: str):
        self.url = url
        self.word_dict_file = word_dict_file

    def _get_dictionary_from_web(self) -> tuple:
        """
        returns uppercase words longer then 4 letters
        from dictionary url
        :return: tuple
        """
        response = urllib.request.urlopen(self.url)
        long_txt = response.read().decode()
        words = (word for word in long_txt.splitlines() if len(word) > 4)
        words = tuple(word.upper() for word in words)
        return words

    def _get_dictionary_from_file(self) -> tuple:
        """
        returns words from dictionary file
        :return: tuple
        """
        with open(self.word_dict_file, "r") as read_file:
            return tuple(read_file.readlines())

    def _dump_words_to_file(self):
        """
        dump words from url to file
        """
        with open(self.word_dict_file, 'w') as writer:
            for word in self._get_dictionary_from_web():
                writer.write(word + '\n')

    @property
    def word_dictionary(self) -> tuple:
        """
        returns words from file or put words from url to file and then returns
        words from file

        :return: tuple
        """
        try:
            words = self._get_dictionary_from_file()
        except FileNotFoundError:
            self._dump_words_to_file()
            words = self._get_dictionary_from_file()

        return tuple(_.strip() for _ in words)

    def get_random(self):
        """
        return random word from dictionary
        """
        return choice(self.word_dictionary)

    def __len__(self) -> int:
        return len(self.word_dictionary)

    def __str__(self) -> str:
        return ', '.join(self.word_dictionary)

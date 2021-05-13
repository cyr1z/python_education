"""
work with word and word mask in game.

"""
from .settings import MASK_SYMBOL


class GameWord:
    """
    work with word, wrong letters and word mask in game.

    :word_string: for print game formatted word
    :wrong_letters_string: for print game formatted wrong letters
    :word_mask_string: for print game formatted word mask

    :is_letter_in_word: check is letter in word
    :put_letter_to_mask: put them to word mask
    :put_letter_to_wrong_list: or wrong letters list

    :is_word_mask_clean: check is word mask clean
    """

    def __init__(self, in_word: str):
        self.word = in_word.strip()
        self.word_mask = [MASK_SYMBOL] * len(self.word)
        self.wrong_letters = []

    @property
    def word_string(self) -> str:
        """
        game formatted word
        :return: str
        """
        return ' '.join(self.word)

    @property
    def wrong_letters_string(self) -> str:
        """
        game formatted wrong letters
        :return: str
        """
        return ' '.join(self.wrong_letters)

    @property
    def word_mask_string(self) -> str:
        """
        game formatted word mask
        :return: str
        """
        return ' '.join(self.word_mask)

    @staticmethod
    def _clean_letter(letter):
        return letter.upper().strip()[0]

    def is_letter_in_word(self, letter: str) -> bool:
        """
        check is letter in word
        :param letter: str
        :return: bool
        """
        letter = self._clean_letter(letter)
        result = True
        if letter not in self.word:
            result = False
        return result

    def put_letter_to_mask(self, letter):
        """
        put letter to word mask
        :param letter:
        :return: list
        """
        letter = self._clean_letter(letter)
        for num, item in enumerate(self.word):
            if letter == item:
                self.word_mask[num] = letter
        return self.word_mask

    def put_letter_to_wrong_list(self, letter):
        """
        put letter to wrong letters list
        :param letter:
        :return: list
        """
        letter = self._clean_letter(letter)
        self.wrong_letters.append(letter)
        return self.wrong_letters

    def is_word_mask_clean(self) -> bool:
        """
        check is word mask clean
        :return: boolean
        """
        return MASK_SYMBOL not in self.word_mask

    def __str__(self):
        return self.word_string

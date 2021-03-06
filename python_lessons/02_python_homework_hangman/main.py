"""
main game module

"""

from utils.settings import WORD_DICT_FILENAME, WORD_URL, \
     WIN_PHRASE, LOSE_PHRASE, WORD_PHRASE, WRONG_LETTERS_PHRASE
from utils.words import WordsDictionary
from utils.game_word import GameWord
from utils.ascii_pictures import PICTURES
from utils.color import cli_color
from utils.inputs import get_letter

if __name__ == "__main__":
    words_dict = WordsDictionary(WORD_URL, WORD_DICT_FILENAME)
    game_word = GameWord(words_dict.get_random())

    while True:
        print(cli_color(PICTURES[len(game_word.wrong_letters)], 'c'))
        print(cli_color(WORD_PHRASE.format(game_word.word_mask_string), 'w'))
        print(WRONG_LETTERS_PHRASE.format(game_word.wrong_letters_string))

        letter = get_letter()

        if game_word.is_letter_in_word(letter):
            game_word.put_letter_to_mask(letter)
        else:
            game_word.put_letter_to_wrong_list(letter)

        if game_word.is_word_mask_clean():
            print(cli_color(game_word.word_string, 'g'))
            print(WIN_PHRASE)
            break

        if len(game_word.wrong_letters) == len(PICTURES):
            print(cli_color(PICTURES[-1], 'r'))
            print(cli_color(game_word.word_string, 'y'))
            print(LOSE_PHRASE)
            break

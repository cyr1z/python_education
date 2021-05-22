"""
Game module.
"""
from app.model.table import GameTable
from app.view.table_view import TableView


class Game:
    """
    Game play class
    """

    def __init__(self, numbers_map, player1, player2):
        self.table = GameTable(numbers_map)
        self.players = []
        self.players.append(player1)
        self.players.append(player2)

    def play_step(self, player):
        """
        play step for player
        :param player: Player
        :return:
        """
        print(TableView(**self.table.choices))
        number = player.get_choice(self.table)
        result = self.table.choice_handler(number, player)

        return result

    def iteration(self) -> dict:
        """
        running game step for player
        :return: bool
        """
        request = {}
        for player in self.players:
            request = self.play_step(player)
            if request:
                break
        return request

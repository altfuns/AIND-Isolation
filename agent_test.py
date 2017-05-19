"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
                        custom_score_2, custom_score_3)
from sample_players import (RandomPlayer, open_move_score,
                            improved_score, center_score)
from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.AB_custom_score = AlphaBetaPlayer(score_fn=custom_score)
        self.AB_custom_score_2 = AlphaBetaPlayer(score_fn=custom_score_2)
        self.AB_custom_score_3 = AlphaBetaPlayer(score_fn=custom_score_3)
        self.AB_Improved = AlphaBetaPlayer(score_fn=improved_score)

    def test_minimax(self):
        self.player1 = MinimaxPlayer(timeout=0.)
        self.player2 = MinimaxPlayer(timeout=0.)
        self.game = isolation.Board(self.player1, self.player2)
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))

    def test_alphabeta_custom_score(self):
        print("AB_custom_score as Player 1")
        self.play(self.AB_custom_score, self.AB_Improved)
        print("AB_custom_score as Player 2")
        self.play(self.AB_Improved, self.AB_custom_score)

    def test_alphabeta_custom_score_2(self):
        print("AB_custom_score2 as Player 1")
        self.play(self.AB_custom_score_2, self.AB_Improved)
        print("AB_custom_score2 as Player 2")
        self.play(self.AB_Improved, self.AB_custom_score_2)

    def test_alphabeta_custom_score_3(self):
        print("AB_custom_score3 as Player 1")
        self.play(self.AB_custom_score_2, self.AB_Improved)
        print("AB_custom_score3 as Player 2")
        self.play(self.AB_Improved, self.AB_custom_score_2)

    def play(self, player_1, player_2):
        game = isolation.Board(player_1, player_2)
        winner, history, outcome = game.play()
        print("\nWinner: {}\nOutcome: {}".format('Player 1' if winner == player_1 else 'Player 2', outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))





if __name__ == '__main__':
    unittest.main()

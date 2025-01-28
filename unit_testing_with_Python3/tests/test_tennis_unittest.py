import unittest

from unit_testing_with_Python3.src.score_tennis import Tennis


class TennisTest(unittest.TestCase):
    def test_score_tennis(self):
        test_case = [
            (0, 0, "Love-All"),
            (1, 1, "Fifteen-All"),
            (2, 2, "Thirty-All"),
            # (2, 1, "Thirty-Fifteen"),
            # (3, 1, "Forty-Fifteen"),
            # (4, 1, "Win for Player 1"),
        ]
        for player1_points, player2_points, expected_score in test_case:
            with self.subTest(f"{player1_points} - {player2_points} -> {expected_score}"):
                self.assertEqual(
                    Tennis.score_tennis(player1_points, player2_points), expected_score
                )
# if _name_ == "_main_":
#     unittest.main()

import pytest
from playwright.sync_api import expect

from unit_testing_with_Python3.src.score_tennis import Tennis

@pytest.mark.parametrize("player1_points, player2_points, expected", [
    (0, 0, "Love-All"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
])
def test_0_0_love_all(player1_points, player2_points, expected):
    assert Tennis.score_tennis(player1_points, player2_points) == expected

# don`t need
# def test_1_1_fifteen_all():
#     assert Tennis.score_tennis(1, 1) == "Fifteen-All"
#
# def test_2_2_thirty_all():
#     assert Tennis.score_tennis(2, 2) == "Thirty-All"

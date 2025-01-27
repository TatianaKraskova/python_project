import pytest

from testing_In__python.src.dice_count import full_house, dice_counts


@pytest.mark.parametrize(
    "dice, expected",
    [
        # Test case 1: All dice are the same
        ([1, 1, 1, 1, 1], {1: 5, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}),

        # Test case 2: No dice roll
        ([], {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}),

        # Test case 3: Each die value occurs once
        ([1, 2, 3, 4, 5, 6], {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),

        # Test case 4: Mixed dice with duplicates
        ([1, 2, 2, 3, 3, 3], {1: 1, 2: 2, 3: 3, 4: 0, 5: 0, 6: 0}),

        # Test case 5: Dice with only one value
        ([4, 4, 4, 4, 4], {1: 0, 2: 0, 3: 0, 4: 5, 5: 0, 6: 0}),

        # Test case 6: All dice are different
        ([1, 2, 3, 4, 5], {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0}),
    ]
)
def test_dice_counts(dice, expected):
    result = dice_counts(dice)
    assert result == expected
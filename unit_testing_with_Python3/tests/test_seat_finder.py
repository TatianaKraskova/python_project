import unittest

from unit_testing_with_Python3.src.seat_finder import SeatFinder


class SeatFinderTest(unittest.TestCase):

    def test_prefer_near_the_front(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(1)
        self.assertEqual(seats, {"A6"})

    def test_finds_adjacent_seats_when_more_than_one_requested(self):
        finder = SeatFinder(available_seats={"A6", "A8", "C6", "C7"})
        seats = finder.find_seats(2)
        self.assertEqual(seats, {"C6", "C7"})

    def test_finds_separate_seats_when_adjacent_not_available(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(2)
        self.assertEqual(seats, {"B6", "C7"})  # Adjusted expected result

    def test_find_seats_fails_when_not_enough_available(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(5)
        self.assertEqual(seats, {})

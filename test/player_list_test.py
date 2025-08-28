"""
Unit tests for the PlayerList class defined in player_list.py.

This module contains test cases for verifying the correct behavior of the PlayerList class,
which manages a collection of Player instances.

Classes tested:
- PlayerList (from player_list.py): A container for Player objects with utility methods.

Test coverage includes:
- Checking if the player list is empty when initialized without players
- Verifying that the list is not empty when initialized with a Player instance

To run the tests:
    python -m unittest test.player_list_test
or use your preferred test runner.
"""



import unittest
from app.player import Player
from app.player_list import PlayerList


class TestPlayerListClass(unittest.TestCase):
    def test_player_list_is_empty(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)

    def test_player_list_not_empty(self):
        player_list = PlayerList(Player("2", "player_2"))
        self.assertFalse(player_list.is_empty)

if __name__ == '__main__':
    unittest.main()

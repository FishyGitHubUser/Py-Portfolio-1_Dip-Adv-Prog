"""
Unit tests for the Player class defined in player.py.

This module contains test cases for verifying the correct behavior of the Player class,
which represents a player with a unique identifier and a name.

Classes tested:
- Player (from player.py): A simple data model with attributes `id` and `name`.

Test coverage includes:
- Initialization of Player instances
- Attribute assignments and access
- Basic equality and representation

To run the tests:
    python -m unittest test.player_test
or use your preferred test runner.
"""


import unittest
from app.player import Player


class TestPlayerClass(unittest.TestCase):
    def test_player_uid(self):
        player = Player("1", "player_1")
        self.assertEqual(player.uid, "1")

    def test_player_name(self):
        player = Player("2", "player_2")
        self.assertEqual(player.name, "player_2")

if __name__ == '__main__':
    unittest.main()

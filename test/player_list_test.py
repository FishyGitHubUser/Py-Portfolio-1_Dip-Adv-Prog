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
        player_list = PlayerList()
        player_list.new_node_at_head(Player("1", "player_1"))
        self.assertFalse(player_list.is_empty)

    def test_player_list_new_head_is_tail_when_one_player(self):
        player_list = PlayerList()
        player_list.new_node_at_head(Player("1", "player_1"))

        self.assertEqual(player_list._head, player_list._tail)

    def test_player_list_new_head_not_tail_when_multiple_players(self):
        player_list = PlayerList()
        player_list.new_node_at_head(Player("1", "player_1"))
        player_list.new_node_at_head(Player("2", "player_2"))

        self.assertNotEqual(player_list._head, player_list._tail)

    def test_player_list_add_multiple_node(self):
        player_list = PlayerList()
        player_list.new_node_at_head(Player("1", "player_1"))
        player_list.new_node_at_head(Player("2", "player_2"))

        # Counts nodes in Playerlist
        list_count = 0
        current_node = player_list.head
        while current_node:
            list_count += 1
            current_node = current_node.next_node

        self.assertEqual(list_count, 2)

    def test_player_list_new_tail_is_head_when_one_player(self):
        player_list = PlayerList()
        player = Player("1", "player_1")
        player_list.new_node_at_tail(player)

        self.assertEqual(player_list._tail.player, player)

    def test_player_list_new_tail_not_head_when_multiple_players(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))
        player_list.new_node_at_tail(Player("2", "player_2"))

        self.assertNotEqual(player_list._head, player_list._tail)

if __name__ == '__main__':
    unittest.main()

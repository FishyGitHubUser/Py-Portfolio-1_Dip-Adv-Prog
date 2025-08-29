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

References:
- 'with' statement: Use cases
    https://www.geeksforgeeks.org/python/with-statement-in-python/
    https://builtin.com/software-engineering-perspectives/what-is-with-statement-python
"""


import unittest

from app.player import Player
from app.player_list import PlayerList, EmptyPlayerListError


class TestPlayerListClass(unittest.TestCase):
    def test_is_empty(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)

    def test_not_empty_when_one_player(self):
        player_list = PlayerList()
        player_list.new_node_at_head(Player("1", "player_1"))
        self.assertFalse(player_list.is_empty)

    def test_not_empty_when_multiple_players(self):
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

    def test_new_head_is_tail_when_one_player(self):
        player_list = PlayerList()
        player_list.new_node_at_head(Player("1", "player_1"))

        self.assertEqual(player_list.head, player_list.tail)

    def test_new_head_not_tail_when_multiple_players(self):
        player_list = PlayerList()
        player_list.new_node_at_head(Player("1", "player_1"))
        player_list.new_node_at_head(Player("2", "player_2"))

        self.assertNotEqual(player_list.head, player_list.tail)

    def test_new_tail_is_head_when_one_player(self):
        player_list = PlayerList()
        player = Player("1", "player_1")
        player_list.new_node_at_tail(player)

        self.assertEqual(player_list.tail.player, player)

    def test_new_tail_not_head_when_multiple_players(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))
        player_list.new_node_at_tail(Player("2", "player_2"))

        self.assertNotEqual(player_list.head, player_list.tail)

    def test_delete_node_at_head_raises_error_when_empty(self):
        player_list = PlayerList()

        with self.assertRaises(EmptyPlayerListError):
            player_list.delete_node_at_head()

    def test_delete_node_at_head_when_one_player(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))

        removed_node = player_list.delete_node_at_head()

        self.assertTrue(player_list.is_empty)
        self.assertEqual(removed_node.player.uid, "1")
        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)

    def test_delete_node_at_head_when_multiple_players(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))
        player_list.new_node_at_tail(Player("2", "player_2"))

        removed_head_node = player_list.delete_node_at_head()

        self.assertFalse(player_list.is_empty)
        self.assertEqual(removed_head_node.player.uid, "1")
        self.assertEqual(player_list.head.player.uid, "2" )
        self.assertIsNone(player_list.head.previous_node)

    def test_delete_node_at_tail_raises_error_when_empty(self):
        player_list = PlayerList()

        with self.assertRaises(EmptyPlayerListError):
            player_list.delete_node_at_tail()

    def test_delete_node_at_tail_when_one_player(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))

        removed_tail_node = player_list.delete_node_at_tail()

        self.assertTrue(player_list.is_empty)
        self.assertEqual(removed_tail_node.player.uid, "1")
        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)

    def test_delete_node_at_tail_when_multiple_players(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))
        player_list.new_node_at_tail(Player("2", "player_2"))

        removed_tail_node = player_list.delete_node_at_tail()

        self.assertFalse(player_list.is_empty)
        self.assertEqual(removed_tail_node.player.uid, "2")
        self.assertEqual(player_list.tail.player.uid, "1")
        self.assertIsNone(player_list.head.previous_node)

    def test_delete_node_at_key_when_empty(self):
        player_list = PlayerList()

        with self.assertRaises(EmptyPlayerListError):
            player_list.delete_node_at_key("1")

    def test_delete_node_at_key_when_one_player(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))

        removed_key_node = player_list.delete_node_at_key("1")

        self.assertTrue(player_list.is_empty)
        self.assertEqual(removed_key_node.player.uid, "1")
        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)

    def test_delete_node_at_key_when_multiple_players(self):
        player_list = PlayerList()
        player_list.new_node_at_tail(Player("1", "player_1"))
        player_list.new_node_at_tail(Player("2", "player_2"))
        player_list.new_node_at_tail(Player("3", "player_3"))
        player_list.new_node_at_tail(Player("4", "player_4"))

        removed_node = player_list.delete_node_at_key("3")

        self.assertEqual(removed_node.player.uid, "3")

        # Checks node references updated in Playerlist
        current_node = player_list.head
        while current_node:
            if current_node.player.uid == "2" and current_node.next_node is not None:
                # Check previous node reference for the next node links to current node
                self.assertEqual(current_node.player.uid, current_node.next_node.previous_node.player.uid)
            elif current_node.player.uid == "4" and current_node.previous_node is not None:
                # Check next node reference for the previous node links to current node
                self.assertEqual(current_node.player.uid, current_node.previous_node.next_node.player.uid)

            current_node = current_node.next_node


if __name__ == '__main__':
    unittest.main()

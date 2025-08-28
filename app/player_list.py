"""
Defines the PlayerList class, representing a list of players.

The class utilises linked list functionality for handling player objects.
"""

from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def new_node_at_head(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next_node = self._head
            self._head.previous_node = new_node
            self._head = new_node

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def is_empty(self):
        return self._head is None

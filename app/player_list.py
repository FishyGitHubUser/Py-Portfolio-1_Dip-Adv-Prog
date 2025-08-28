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
            new_node.next_node = self._head         # New node links to head
            self._head.previous_node = new_node     # Head links to new node
            self._head = new_node                   # New node is now new head

    def new_node_at_tail(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next_node = new_node         # Tail links to new node
            new_node.previous_node = self._tail     # New node links to tail
            self._tail = new_node                   # New node is now new tail

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def is_empty(self):
        return self._head is None

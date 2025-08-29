"""
Defines the PlayerList class, representing a list of players.

The class utilises linked list functionality for handling player objects.
"""

from app.player import Player
from app.player_node import PlayerNode


class EmptyPlayerListError(Exception):
    """Error raised when actions are performed on empty PlayerList."""
    pass


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

    def delete_node_at_head(self):
        if self.is_empty:
            raise EmptyPlayerListError("Cannot delete from head: PlayerList is empty.")

        removed_node = self._head                   # Deleted node saved to return

        if self._head is self._tail:
            self._head = None                       # Dereferences last node from head
            self._tail = None                       # Dereferences last node from tail
        else:
            self._head = self._head.next_node       # Next node is now new head
            self._head.previous_node = None         # Dereferencing old head

        return removed_node

    def delete_node_at_tail(self):
        if self.is_empty:
            raise EmptyPlayerListError("Cannot delete from tail: PlayerList is empty.")

        removed_node = self._tail

        if self._head is self._tail:
            self._head = None                       # Dereferences last node from head
            self._tail = None                       # Dereferences last node from tail
        else:
            self._tail = self._tail.previous_node   # Previous node is now new tail
            self._tail.next_node = None             # Dereferencing old head

        return removed_node


    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def is_empty(self):
        return self._head is None and self._tail is None

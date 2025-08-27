"""
Defines the PlayerNode class, representing a node with a player object.

The class node stores data for a list, referencing a previous and
forthcoming node for bidirectional linked list capabilities.
"""


from app.player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._previous_node = None
        self._next_node = None

    def __str__(self):
        return f'PlayerNode({self._player}, {self._previous_node}, {self._next_node})'

    @property
    def player(self):
        return self._player

    @property
    def previous_node(self):
        return self._previous_node

    @previous_node.setter
    def previous_node(self, previous_node):
        self._previous_node = previous_node

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    @property
    def key(self):
        return self._player.uid

"""
Defines the Player class, representing a player with a unique ID and name.

The class uses properties to encapsulate access to the `uid` and `name` attributes,
allowing for validation or controlled access when necessary.
"""


class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Player({self._uid}, {self._name})"

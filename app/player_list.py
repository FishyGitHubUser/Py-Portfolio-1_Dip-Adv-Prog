"""
Defines the PlayerList class, representing a list of players.

The class utilises linked list functionality for handling player objects.

References:
- In-line 'if' statement
    https://www.geeksforgeeks.org/python/different-ways-of-using-inline-if-in-python/
- Iterating with generator 'yields'
    https://www.w3schools.com/python/ref_keyword_yield.asp
    https://www.reddit.com/r/learnpython/comments/rzukrb/what_is_the_idea_of_using_yield_in_python/
    https://www.youtube.com/watch?v=7lmCu8wz8ro&t=4560s
- Reverse list with 'reversed()'
    https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
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

    def __iter__(self):
        current_node = self._head

        while current_node:
            yield current_node                      # List of iterated values per yield
            current_node = current_node.next_node

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

    def delete_node_at_key(self, key):
        if self.is_empty:
            raise EmptyPlayerListError("Cannot delete from key: PlayerList is empty.")

        current_node = self._head

        while current_node:
            if current_node.player.uid == key:
                removed_node = current_node

                if self._head is self._tail:
                    self._head = None
                    self._tail = None
                elif current_node is self._head:
                    self._head = current_node.next_node
                    self._head.previous_node = None
                elif current_node is self._tail:
                    self._tail = current_node.previous_node
                    self._tail.next_node = None
                else:
                    # Change the next_node reference for node prior to the current
                    current_node.previous_node.next_node = current_node.next_node
                    # Change the previous_node reference for node after the current
                    current_node.next_node.previous_node = current_node.previous_node

                return removed_node
            current_node = current_node.next_node
        return None

    def display(self, forward=True):
        if self.is_empty:
            raise EmptyPlayerListError("Cannot display list: PlayerList is empty.")

        displayed_list = []

        for player_node in self:
            displayed_list.append(f"Player({player_node.player.uid}, {player_node.player.name})")

        if forward:
            return displayed_list
        else:
            return list(reversed(displayed_list))


    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def is_empty(self):
        return self._head is None and self._tail is None


if __name__ == '__main__':
    player_list = PlayerList()
    player_list.new_node_at_tail(Player("1", "player_1"))
    player_list.new_node_at_tail(Player("2", "player_2"))
    player_list.new_node_at_tail(Player("3", "player_3"))

    print(player_list.display())
    print(player_list.display(False))

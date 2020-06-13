import time
from typing import Dict

class Cache:
    """ Cache is the caching manager. It stores information.
    """
    def __init__(self) -> None:
        """ Constructor for the cache.
        """
        self._store: Dict = dict()

    def search(self, key: str) -> object:
        """ Searches the cache for the appropriate key, and returns the value if found.

        Args:
            key (str): The key to search with.

        Returns:
            object: The value associated with the key, or None.
        """
        if key not in self._store:
            return None

        if not self._is_fresh(key):
            # Remove from cache as it has expired.
            self._store.pop(key)
            return None

        return self._store[key].item

    def add(self, key: str, item: object, ttl: int) -> None:
        """ Adds an item to the cache, or updates the item if it already exists.

        Args:
            key (str): The key for the item.
            item (object): The item itself.
            ttl (int): The time to live for the item.
        """
        self._store[key] = CacheItem(item, time.time(), ttl)

    def clean_up(self) -> None:
        """ Cleans up any expired items in the cache.
        """
        self._store = {k: v for k, v in self._store.items() if self._is_fresh(k)}

    def _is_fresh(self, key: str) -> bool:
        if key not in self._store:
            return False
        
        life: float = (time.time() - self._store[key].start) # This is in seconds
        return life <= self._store[key].ttl

class CacheItem:
    """ CacheItem is a wrapped data container for the cache items.
    """

    def __init__(self, item: object, start: float, ttl: int) -> None:
        """ Constructor for the cache item.

        Args:
            item (object): The item is what will actually be cached.
            start (float): The start time for when the item was first cached.
            ttl (int): The time to live for the item.
        """
        self.item: object = item
        self.start: float = start
        self.ttl: int = ttl
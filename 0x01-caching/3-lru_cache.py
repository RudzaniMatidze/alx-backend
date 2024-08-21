#!/usr/in/env python3
"""
Create a class LRUCache that inherits from BaseCaching
and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements
    a Least Recently Used (LRU) eviction policy.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance.
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Add an item to the cache, following LRU eviction policy.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                        self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {:s}". format(discard))

    def get(self, key):
        """
         Retrieve an item from the cache by key

         Args:
            key (str):  Retrieve an item from the cache by key
            Return:
                any: The value associated with the key,
                or None if the key does not exist.
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None

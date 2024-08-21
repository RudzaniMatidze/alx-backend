#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching
and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    Initialize the LIFOCache instance.
    """

    def __init__(self):
        """
        Inherits from BaseCaching and implements
        a Last-In-First-Out (LIFO) eviction policy.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache, following LIFO eviction policy.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            last_key, last_value = self.cache_data.popitem()
            print("DISCORD: {}".format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to be retrieved.
        Return:
            any: The value associated with the key,
            or None if the key does not exist.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

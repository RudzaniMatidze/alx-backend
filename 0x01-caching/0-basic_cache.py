#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and provides the caching functionality
    """

    def __init__(self):
        """
        Initializes the BasicCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Stores an item in the cache.

        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): The key of the item to be retrieved.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

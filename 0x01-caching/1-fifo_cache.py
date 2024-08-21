#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching
and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and implements
    a First-In-First-Out (FIFO) eviction policy
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache, following FIFO eviction policy.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

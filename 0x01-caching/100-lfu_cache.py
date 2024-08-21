#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching
and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that implements a Least Frequently
    Used (LFU) cache eviction policy.
    """

    def __init__(self):
        """
        Initialize the LUFCache instance.
        """
        super().__init__()
        self.frequency = {}
        self.usage_order = {}

    def put(self, key, item):
        """
        Add an item to the cache with LFU eviction policy.

        Args:
            Key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [
                        k for k, v in self.frequency.items() if v == min_freq]

                if len(lfu_keys) > 1:
                    oldest_key = min(
                            lfu_keys, key=lambda k: self.usage_order[k])
                else:
                    oldest_key = lfu[0]

                print(f"DISCARD: {oldest}")
                del self.cache_data[oldest_key]
                del self.cache_frequency[oldest_key]
                del self.usage_order[oldest_key]

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = len(self.usage_order)

    def get(self, key):
        """
        Retrieve an item from the cache by key

        Args:
             key (str): The key of the item to be retrieved.
        Return:
            any: The value associated with the key,
            or None if the key does not exist.
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order[key] = len(self.usage_order)
            return self.cache_data[key]
        return None

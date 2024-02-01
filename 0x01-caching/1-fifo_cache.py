#!/usr/bin/env python3
"""0x01. Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache implementation"""

    def __init__(self):
        """Constructor function for FIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Put a key into the cache for this"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        i = list(self.cache_data.keys())
        if len(i) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(i[0])
            print("DISCARD: {}".format(i[0]))

    def get(self, key):
        """retrieves a key from the cache dictionary"""
        if key is None:
            return None

        return self.cache_data.get(key)

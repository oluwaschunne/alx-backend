#!/usr/bin/env python3
"""0x01. Caching"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """LIFOCache implementation"""

    def __init__(self):
        """Constructor for LIFOCache implementation"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put a key into the cache object"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                val, _ = self.cache_data.popitem()
                print("DISCARD: {}".format(val))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """retrieves a key from the cache dictionary"""
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)

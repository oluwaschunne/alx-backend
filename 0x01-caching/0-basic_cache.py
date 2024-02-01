#!/usr/bin/env python3
"""0x01. Caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherit from BaseCaching class"""

    def put(self, key, item):
        """adds a key and value to the cache dictionary"""
        if item is None or key is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """retrieves a key from the cache dictionary"""
        if key is None:
            return None

        return self.cache_data.get(key)

#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ Least Frequently Used (LFU) caching system"""

    def __init__(self):
        """ Initialize LFU cache"""
        super().__init__()
        # Dictionary to keep track of item frequencies
        self.freq_counter = defaultdict(int)

    def put(self, key, item):
        """ Add an item to the LFU cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._discard_item()
            self.cache_data[key] = item
            self.freq_counter[key] += 1

    def get(self, key):
        """ Get an item from the LFU cache"""
        if key is not None and key in self.cache_data:
            self.freq_counter[key] += 1
            return self.cache_data[key]
        return None

    def _discard_item(self):
        """ Discard the least frequently used item (LFU algorithm)"""
        min_freq = min(self.freq_counter.values())
        items_to_discard = [
            k for k, v in self.freq_counter.items() if v == min_freq]

        if len(items_to_discard) > 1:
            # If more than one item has the same frequency, use LRU to decide
            lru_key = min(self.freq_counter, key=self.freq_counter.get)
            items_to_discard.remove(lru_key)

        discarded_key = items_to_discard[0]
        print(f"DISCARD: {discarded_key}\n")
        del self.cache_data[discarded_key]
        del self.freq_counter[discarded_key]

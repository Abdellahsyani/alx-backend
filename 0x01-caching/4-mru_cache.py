#!/usr/bin/env python3
'''mru caching'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU cache implementation."""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.insert(0, key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop(0)
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
            self.order.insert(0, key)

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key: The key of the item.

        Returns:
            The cached item if found, None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.insert(0, key)
        return self.cache_data[key]

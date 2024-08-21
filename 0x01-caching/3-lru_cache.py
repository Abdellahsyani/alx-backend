#!/usr/bin/env python3
'''LRU caching'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''start URL caching'''
    def __init__(self):
        '''the constractor method'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''the put method'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item

            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        '''the get method'''
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]

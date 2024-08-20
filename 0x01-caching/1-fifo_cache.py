#!/usr/bin/env python3
'''FIFO caching'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''start class fifo caching'''

    def __init__(self):
        '''The init methjod'''
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
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        '''the get method '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

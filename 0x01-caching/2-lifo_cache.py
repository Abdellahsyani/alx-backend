#!/usr/bin/env python3
'''LIFO cache'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''start caching by using lifo algorithm'''

    def __init__(self):
        '''the constractor method'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''the put method '''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item

            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                old_key = self.order.pop()
                del self.cache_data[old_key]
                print("DISCARD: {}".format(old_key))
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        '''the get method'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

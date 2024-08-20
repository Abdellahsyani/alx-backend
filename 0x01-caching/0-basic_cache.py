#!/usr/bin/env python3
'''Basic cache'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''caching system'''
    def put(self, key, item):
        '''put method'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''return the value'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

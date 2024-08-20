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


my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

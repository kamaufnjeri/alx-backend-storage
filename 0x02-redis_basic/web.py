#!/usr/bin/env python3
'''Module with tools for request caching and tracking.
'''

import redis
import requests
from functools import wraps
from typing import Callable

redis_instance = redis.Redis()
'''The module-level Redis instance.
'''


def cache_data(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoke_and_cache(url) -> str:
        '''Wrapper function for caching the output.
        '''
        redis_instance.incr(f'request_count:{url}')
        cached_result = redis_instance.get(f'cached_result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
        redis_instance.set(f'request_count:{url}', 0)
        redis_instance.setex(f'cached_result:{url}', 10, result)
        return result
    return invoke_and_cache


@cache_data
def fetch_page_content(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text

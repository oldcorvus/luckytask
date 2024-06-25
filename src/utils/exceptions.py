""""
This module defines custom exceptions for the Redis client operations.

Classes:
    RedisConnectionError: Raised when a Redis connection error occurs.
    RedisOperationError: Raised when a Redis operation error occurs.
"""


class RedisConnectionError(Exception):
    """Raised when a Redis connection error occurs."""

    pass


class RedisOperationError(Exception):
    """Raised when a Redis operation error occurs."""

    pass

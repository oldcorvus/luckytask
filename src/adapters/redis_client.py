"""
This module defines a Redis client abstraction to handle connection management and common operations.

Classes:
    RedisClient: A class to manage the Redis connection and handle exceptions.
"""

import redis

from src.utils.exceptions import RedisConnectionError


class RedisClient:
    """
    A class to manage the Redis connection and handle exceptions.

    Methods:
        connect() -> None: Connects to the Redis server.
        get_client() -> redis.Redis: Returns the Redis client instance.
    """

    def __init__(self, host="localhost", port=6379, db=0):
        """
        Initializes the Redis client.

        Args:
            host (str): The Redis server host.
            port (int): The Redis server port.
            db (int): The Redis database number.
        """
        self.host = host
        self.port = port
        self.db = db
        self.client = None

    def connect(self) -> None:
        """
        Connects to the Redis server.

        Raises:
            RedisConnectionError: If there is an error connecting to Redis.
        """
        try:
            self.client = redis.Redis(host=self.host, port=self.port, db=self.db)
            # Test the connection
            self.client.ping()
        except redis.RedisError as e:
            raise RedisConnectionError(f"Failed to connect to Redis: {e}")

    def get_client(self) -> redis.Redis:
        """
        Returns the Redis client instance.

        Returns:
            redis.Redis: The Redis client instance.

        Raises:
            RedisConnectionError: If the client is not connected.
        """
        if not self.client:
            raise RedisConnectionError(
                "Redis client is not connected. Call connect() first."
            )
        return self.client

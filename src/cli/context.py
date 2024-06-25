"""
This module initializes and manages shared resources such as database connections and services.
It defines the ApplicationContext class which holds instances of services and repositories
used across different commands in the CLI application.
"""

from src.adapters.redis_client import RedisClient
from src.repositories.redis_repository import RedisTaskRepository
from src.services.task_service import TaskService
from src.utils.config_handler import load_config


class ApplicationContext:
    """
    Application context for managing services and repositories.

    Attributes:
        redis_client (RedisClient): Redis client for database connections.
        task_repository (RedisTaskRepository): Repository for managing task data.
        task_service (TaskService): Service for task business logic.
    """

    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        """
        Initializes the application context with necessary services and repositories.

        Args:
            host (str): Redis server host.
            port (int): Redis server port.
            db (int): Redis database number.
        """
        config = load_config()
        host = config.get("host", "localhost")
        port = config.get("port", 6379)
        db = config.get("db", 0)
        self.redis_client = RedisClient(host=host, port=port, db=db)
        self.redis_client.connect()
        self.task_repository = RedisTaskRepository(self.redis_client)
        self.task_service = TaskService(repository=self.task_repository)

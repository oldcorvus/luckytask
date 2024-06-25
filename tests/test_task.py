"""
This module contains unit tests for the Task class defined in task_module.py.
It uses the unittest framework to validate the functionality and data integrity
of the Task model, ensuring proper creation, validation, and automatic timestamp
setting.

Tests:
    TestTask: A unittest.TestCase subclass that includes various tests for the Task model.
"""

import time
import unittest

from pydantic import ValidationError

from src.entities.task import Task


class TestTask(unittest.TestCase):
    """
    Test case for the Task model.

    This class contains tests to ensure that the Task model behaves as expected.
    It checks for valid creation, proper validation of priority and name fields,
    and automatic setting of the timestamp.
    """

    def test_task_creation_valid(self):
        """Test creating a valid Task object"""
        task = Task(name="Sample Task", priority=5, description="A sample task")
        self.assertEqual(task.name, "Sample Task")
        self.assertEqual(task.priority, 5)
        self.assertEqual(task.description, "A sample task")
        self.assertIsInstance(task.timestamp, float)

    def test_task_creation_invalid_priority(self):
        """Test creating a Task with an invalid priority"""
        with self.assertRaises(ValidationError) as context:
            Task(name="Sample Task", priority=15, description="A sample task")
        self.assertTrue("Priority must be between 1 and 10" in str(context.exception))

    def test_task_creation_empty_name(self):
        """Test creating a Task with an empty name"""
        with self.assertRaises(ValidationError) as context:
            Task(name="", priority=5, description="A sample task")
        self.assertTrue("Name cannot be empty" in str(context.exception))

    def test_task_creation_without_timestamp(self):
        """Test creating a Task without explicitly providing a timestamp"""
        task = Task(name="Sample Task", priority=5, description="A sample task")
        self.assertIsInstance(task.timestamp, float)
        self.assertAlmostEqual(task.timestamp, time.time(), delta=1)


if __name__ == "__main__":
    unittest.main()

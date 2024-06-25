# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code to the container
COPY . /app/

# Build the package using Poetry
RUN poetry build

# Install the built package
RUN pip install dist/luckytask-0.1.0.tar.gz

# Configure Redis
RUN luckytask config-redis --host lucky_task_redis --port 6379 --db 1

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]

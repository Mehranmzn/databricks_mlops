# Start with the official Astronomer Airflow image
FROM quay.io/astronomer/astro-runtime:7.3.0

# Set the working directory
WORKDIR /usr/local/airflow

# Install Pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock ./

# Install dependencies with Pipenv
RUN pipenv install --system --deploy

# Copy all project files
COPY . .

# Set environment variable for Airflow
ENV AIRFLOW_HOME=/usr/local/airflow

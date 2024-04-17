# Use an official Python runtime as the base image
FROM python:3.9

# Copy the current directory contents into the container at / (root directory)
COPY . /

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "main.py"]

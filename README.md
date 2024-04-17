# Dockerizing a Python Text Analysis Script

This guide will walk you through the process of Dockerizing a Python script for text analysis.

## Step 1: Create Your Python Script

Create a Python script for text analysis.

## Step 2: Create a requirements.txt File

Create a requirements.txt file listing all Python dependencies.

## Step 3: Create a Dockerfile

Create a Dockerfile specifying the environment and commands to run the script.

## Step 4: Build the Docker Image

Build the Docker image using the Dockerfile:

```bash
docker build -t text-analysis-app .
```
## step 5 : Run the Docker Container

```bash
docker run -it text-analysis-app "how are you"
```

